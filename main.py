from fastapi import FastAPI, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import SessionLocal, engine, Base
from models import UserOut
from passlib.context import CryptContext
from models import User
from pydantic import BaseModel, EmailStr, constr
import traceback

app = FastAPI()

Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

templates = Jinja2Templates(directory="templates")

class UserIn(BaseModel):
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

@app.get("/signup/", response_class=HTMLResponse)
async def get_signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup/", response_class=HTMLResponse)
async def create_user(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...), password_confirm: str = Form(...), db: Session = Depends(get_db)):
    try:
        if password != password_confirm:
            return templates.TemplateResponse("signup.html", {"request": request, "error": "Passwords do not match", "username": username, "email": email})
        db_user = db.query(User).filter(User.username == username).first()
        if db_user:
            return templates.TemplateResponse("signup.html", {"request": request, "error": "Username already registered", "username": username, "email": email})
        hashed_password = get_password_hash(password)
        db_user = User(username=username, email=email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return templates.TemplateResponse("signup.html", {"request": request, "success": "User created successfully"})
    except SQLAlchemyError as e:
        db.rollback()
        error_message = f"Database error: {e}"
        print(error_message)
        print(traceback.format_exc())
        return templates.TemplateResponse("signup.html", {"request": request, "error": error_message, "username": username, "email": email})
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        print(error_message)
        print(traceback.format_exc())
        return templates.TemplateResponse("signup.html", {"request": request, "error": error_message, "username": username, "email": email})

@app.get("/login/", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login/", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})
    return templates.TemplateResponse("login.html", {"request": request, "success": "Login successful"})

@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
