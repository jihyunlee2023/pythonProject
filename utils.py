# myapi/utils.py
#네이버 뉴스 오픈 api 코드
import urllib.request
import json
import logging

# Logger 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search_news(politician_name):
    client_id = "_S4AQdq8fSMrNdnoYeqH"
    client_secret = "tuscBxCTsD"
    encText = urllib.parse.quote(politician_name)
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        news_data = json.loads(response_body.decode('utf-8'))
        logger.info(f"News data: {news_data}")  # 디버깅 로그 추가
        return news_data['items'][:3]  # 상위 3개 뉴스만 반환
    else:
        logger.error(f"Error Code: {rescode}")  # 에러 로그 추가
        return None
