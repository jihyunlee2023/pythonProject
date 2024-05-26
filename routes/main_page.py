from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import get_db  # 경로 수정
from models import Politician, User  # 경로 수정

router = APIRouter()
templates = Jinja2Templates(directory="templates")  # 경로 수정

def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Token missing")

    db_user = db.query(User).filter(User.token == token).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return db_user

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request, db: Session = Depends(get_db)):
    politicians = db.query(Politician).all()
    return templates.TemplateResponse("main_page.html", {"request": request, "politicians": politicians})

@router.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: str, db: Session = Depends(get_db)):
    results = db.query(Politician).filter(Politician.name.contains(query)).all()
    return templates.TemplateResponse("main_page.html", {"request": request, "results": results, "query": query})
