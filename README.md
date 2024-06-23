<백엔드 실행하기>
https://wikidocs.net/175214 이 링크 참고해서 FastAPI 실행환경 구성하기
$env:SECRET_KEY="my-very-secure-and-long-secret-key" = powershell 인 경우 이 명령어 치고 서버 실행하기
set SECRET_KEY=my-very-secure-and-long-secret-key = cmd는 이 명령어 입력하고 서버 실행하기
uvicorn myapi.main:app --reload 를 myapi가 있는 프로젝트에서 실행하기
 $env:SECRET_KEY="your_secret_key"; uvicorn myapi.main:app --reload 이 명령어로 백엔드 실행하기


<프론트엔드>
front 폴더에서 "npm run dev" 실행하기
