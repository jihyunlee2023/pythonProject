from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from myapi.database import get_db
from myapi.models import Politician

router = APIRouter()
templates = Jinja2Templates(directory="myapi/templates")

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("main_page.html", {"request": request})

@router.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: str, db: Session = Depends(get_db)):
    results = db.query(Politician).filter(Politician.name.contains(query)).all()
    return templates.TemplateResponse("main_page.html", {"request": request, "results": results, "query": query})
