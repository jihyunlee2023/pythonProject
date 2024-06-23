import sys
import os
import requests

# 현재 파일의 디렉토리를 기준으로 상위 디렉토리를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Request, Depends, HTTPException, Form
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, constr
from database import SessionLocal, engine
from models import Base, User, Politician
from routes.auth import router as auth_router
from routes.main_page import router as main_page_router
from routes.politicians import router as politicians_router

# 로그 파일 경로 설정
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'debug.log')

# 열린 국회 정보 API 키 설정 (본인의 API 키로 대체해야 합니다)
API_KEY = "02782aac6c114f9dbefed52c72e19664"

# Logger 설정
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(log_file_path),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

app = FastAPI(debug=True)

# Creating all tables in the database
Base.metadata.create_all(bind=engine)  # 테이블 생성

# 비밀번호 해시화를 위한 CryptContext 객체 생성
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

templates = Jinja2Templates(directory="templates")  # 템플릿 디렉토리 설정

class UserCreate(BaseModel):
    username: constr(min_length=1)
    email: EmailStr
    password: constr(min_length=1)
    password_confirm: constr(min_length=1)

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Including routes
app.include_router(auth_router)
app.include_router(main_page_router)
app.include_router(politicians_router)

@app.get("/signup", response_class=HTMLResponse)
async def get_signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup", response_class=JSONResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        if user.password != user.password_confirm:
            raise HTTPException(status_code=400, detail="Passwords do not match")
        db_user = db.query(User).filter(User.username == user.username).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        hashed_password = get_password_hash(user.password)
        db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"message": "User created successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        error_message = f"Database error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=error_message)
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=error_message)

@app.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=JSONResponse)
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    logger.debug(f"Login attempt for username: {username}")
    try:
        db_user = db.query(User).filter(User.username == username).first()
        if not db_user or not verify_password(password, db_user.hashed_password):
            logger.warning(f"Invalid username or password for user: {username}")
            raise HTTPException(status_code=400, detail="Invalid username or password")
        logger.info(f"User {username} logged in successfully.")
        return JSONResponse(content={"message": "User logged in successfully"}, status_code=200)
    except SQLAlchemyError as e:
        error_message = f"Database error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=error_message)
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=error_message)

@app.get("/forgot-password", response_class=HTMLResponse)
async def get_forgot_password_page(request: Request):
    return templates.TemplateResponse("forgot_password.html", {"request": request})

@app.post("/forgot-password", response_class=HTMLResponse)
async def forgot_password(request: Request, username: str, email: str, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.username == username, User.email == email).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="Invalid username or email")
        return templates.TemplateResponse("forgot_password.html", {"request": request, "show_reset_form": True, "username": username, "email": email})
    except SQLAlchemyError as e:
        error_message = f"Database error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        return templates.TemplateResponse("forgot_password.html", {"request": request, "error": error_message, "username": username, "email": email})
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        return templates.TemplateResponse("forgot_password.html", {"request": request, "error": error_message, "username": username, "email": email})

@app.post("/reset-password", response_class=HTMLResponse)
async def reset_password(request: Request, username: str, email: str, new_password: str, confirm_new_password: str, db: Session = Depends(get_db)):
    try:
        if new_password != confirm_new_password:
            raise HTTPException(status_code=400, detail="Passwords do not match")
        db_user = db.query(User).filter(User.username == username, User.email == email).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="Invalid username or email")
        hashed_password = get_password_hash(new_password)
        db_user.hashed_password = hashed_password
        db.commit()
        return RedirectResponse(url="/login", status_code=303)
    except SQLAlchemyError as e:
        error_message = f"Database error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        return templates.TemplateResponse("reset_password.html", {"request": request, "error": error_message, "username": username, "email": email})
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        return templates.TemplateResponse("reset_password.html", {"request": request, "error": error_message, "username": username, "email": email})

@app.get("/main", response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

    @app.get("/api/politician/{member_id}", response_class=JSONResponse)
async def get_politician_info(member_id: int):
    try:
        url = f"https://open.assembly.go.kr/portal/openapi/nqdeptwhratddlsanvld?key={API_KEY}&pIndex=1&pSize=10&dept_cd={member_id}"
        response = requests.get(url)
        response.raise_for_status()  # HTTPError 발생 시 예외 처리
        data = response.json()
        
        if not data.get('nqdeptwhratddlsanvld'):
            raise HTTPException(status_code=404, detail="Politician not found")
        
        return JSONResponse(content=data['nqdeptwhratddlsanvld'][0])
    except requests.RequestException as e:
        error_message = f"Failed to fetch data: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=error_message)
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        logger.error(error_message)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=error_message)