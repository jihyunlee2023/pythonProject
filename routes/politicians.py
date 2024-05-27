from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from myapi.database import get_db
from myapi.models import Politician
from myapi.utils import search_news  # 추가된 부분
import logging  # 이 줄을 추가합니다.

router = APIRouter()
templates = Jinja2Templates(directory="myapi/templates")
# Logger 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/politicians", response_class=HTMLResponse)
async def read_politicians(request: Request, db: Session = Depends(get_db)):
    politicians = db.query(Politician).all()
    return templates.TemplateResponse("politicians.html", {"request": request, "politicians": politicians})

@router.get("/politicians/search", response_class=HTMLResponse)
async def search_politicians(request: Request, query: str, db: Session = Depends(get_db)):
    results = db.query(Politician).filter(Politician.name.contains(query)).all()
    return templates.TemplateResponse("politicians.html", {"request": request, "results": results, "query": query})

@router.get("/politicians/{politician_id}", response_class=HTMLResponse)
async def politician_detail(request: Request, politician_id: int, db: Session = Depends(get_db)):
    try:
        politician = db.query(Politician).filter(Politician.id == politician_id).first()
        if not politician:
            raise HTTPException(status_code=404, detail="Politician not found")

        politician_name = politician.name
        news_data = search_news(politician_name)
        if not news_data:
            logger.error("No news data found for politician: %s", politician_name)
        else:
            logger.info(f"News data for {politician_name}: {news_data}")

        return templates.TemplateResponse("politician_detail.html", {"request": request, "politician": politician, "news_data": news_data})
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
