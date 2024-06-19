## chat gpt 사용해서 코드 작성
import os
from datetime import datetime, timedelta
from jwcrypto import jwt, jwk
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수 로드 확인을 위한 디버그 출력
SECRET_KEY = os.getenv("SECRET_KEY")
print(f"Loaded SECRET_KEY: {SECRET_KEY}")  # 디버그 메시지 추가

# JWT 비밀키 설정
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for JWT.")

key = jwk.JWK.generate(kty='oct', size=256, kid=SECRET_KEY)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)  # 액세스 토큰 수명 설정

    # datetime 객체를 문자열로 변환
    to_encode.update({"exp": expire.isoformat()})

    token = jwt.JWT(header={"alg": "HS256"}, claims=to_encode)
    token.make_signed_token(key)
    return token.serialize()


def decode_access_token(token: str):
    decoded_token = jwt.JWT(key=key, jwt=token)
    claims = decoded_token.claims
    return claims
