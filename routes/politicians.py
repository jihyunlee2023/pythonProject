## chat gpt 사용해서 코드 작성
from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from myapi.database import get_db
from myapi.models import Politician, User  # User 모델을 import합니다.
from myapi.utils import search_news  # 추가된 부분
from fastapi.responses import JSONResponse
import logging  # 이 줄을 추가합니다.

router = APIRouter()
# Logger 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

templates = Jinja2Templates(directory="myapi/templates")


# get_current_user 함수 정의 또는 import
def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = db.query(User).filter(User.token == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user

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

        return templates.TemplateResponse("politician_detail.html", {
            "request": request,
            "politician": politician,
            "news_data": news_data
        })
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

#@router.post("/politicians/{politician_id}/favorite", response_class=JSONResponse)
#async def favorite_politician(politician_id: int, request: Request, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#    politician = db.query(Politician).filter(Politician.id == politician_id).first()
#    if not politician:
#        raise HTTPException(status_code=404, detail="Politician not found")

#    if str(politician_id) not in current_user.favorite_politicians.split(','):
#        if current_user.favorite_politicians:
#            current_user.favorite_politicians += f",{politician_id}"
#        else:
#            current_user.favorite_politicians = str(politician_id)
#        db.commit()

    #return {"message": "Politician added to favorites"}
