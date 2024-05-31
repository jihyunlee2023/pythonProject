from fastapi import APIRouter, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, constr
from myapi.database import get_db
from myapi.models import User
from myapi.jwt_utils import create_access_token, decode_access_token
import traceback

router = APIRouter()
templates = Jinja2Templates(directory="myapi/templates")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserIn(BaseModel):
    username: constr(min_length=1)
    email: EmailStr
    password: constr(min_length=1)
    password_confirm: constr(min_length=1)

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user(request: Request):
    user = request.session.get('user')
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user

@router.get("/signup/", response_class=HTMLResponse)
async def get_signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.post("/signup/", response_class=HTMLResponse)
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

@router.get("/login/", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login/", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})
    access_token = create_access_token(data={"sub": db_user.username})
    response = RedirectResponse(url="/", status_code=302)
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return response

@router.get("/logout/", response_class=HTMLResponse)
async def logout(request: Request):
    response = RedirectResponse(url="/")
    response.delete_cookie("access_token")
    return response

@router.get("/forgot-password", response_class=HTMLResponse)
async def get_forgot_password_page(request: Request):
    return templates.TemplateResponse("forgot_password.html", {"request": request})

@router.post("/forgot-password", response_class=HTMLResponse)
async def forgot_password(request: Request, username: str, email: str, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.username == username, User.email == email).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="Invalid username or email")

        return templates.TemplateResponse("forgot_password.html",
                                          {"request": request, "show_reset_form": True, "username": username,
                                           "email": email})
    except SQLAlchemyError as e:
        error_message = f"Database error: {e}"
        print(error_message)
        print(traceback.format_exc())
        return templates.TemplateResponse("forgot_password.html", {"request": request, "error": error_message, "username": username, "email": email})
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        print(error_message)
        print(traceback.format_exc())
        return templates.TemplateResponse("forgot_password.html", {"request": request, "error": error_message, "username": username, "email": email})

@router.post("/reset-password", response_class=HTMLResponse)
async def reset_password(request: Request, username: str, email: str,
                         new_password: str, confirm_new_password: str, db: Session = Depends(get_db)):
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
        print(error_message)
        print(traceback.format_exc())
        return templates.TemplateResponse("reset_password.html", {"request": request, "error": error_message, "username": username, "email": email})
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        print(error_message)
        print(traceback.format_exc())
        return templates.TemplateResponse("reset_password.html", {"request": request, "error": error_message, "username": username, "email": email})
