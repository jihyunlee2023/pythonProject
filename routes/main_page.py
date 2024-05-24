from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from myapi.database import get_db
from myapi.models import Politician, User

router = APIRouter()
templates = Jinja2Templates(directory="myapi/templates")

def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Token missing")

    db_user = db.query(User).filter(User.token == token).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return db_user

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})

@router.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: str, db: Session = Depends(get_db)):
    results = db.query(Politician).filter(Politician.name.contains(query)).all()
    return templates.TemplateResponse("main_page.html", {"request": request, "results": results, "query": query})
