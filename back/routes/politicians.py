# myapi/routes/politicians.py

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from myapi.database import get_db
from myapi.models import Politician

router = APIRouter()
templates = Jinja2Templates(directory="myapi/templates")

@router.get("/politicians", response_class=HTMLResponse)
async def read_politicians(request: Request, db: Session = Depends(get_db)):
    politicians = db.query(Politician).all()
    return templates.TemplateResponse("politicians.html", {"request": request, "politicians": politicians})

@router.get("/politicians/search", response_class=HTMLResponse)
async def search_politicians(request: Request, query: str, db: Session = Depends(get_db)):
    results = db.query(Politician).filter(Politician.name.contains(query)).all()
    return templates.TemplateResponse("politicians.html", {"request": request, "results": results, "query": query})
