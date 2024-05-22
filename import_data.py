# myapi/import_data.py

import pandas as pd
from sqlalchemy.orm import Session
from myapi.database import SessionLocal
from myapi.models import Politician

# 엑셀 파일 경로를 지정하세요
excel_file_path = 'C:\\Users\\ni730\\OneDrive\\바탕 화면\\opensw_project\\국회의원정보.xlsx'

# 엑셀 파일 읽기
df = pd.read_excel(excel_file_path)

# 열 이름 확인 (데이터프레임의 열 이름 출력)
print(df.columns)

# 데이터베이스 세션 생성
db = SessionLocal()

try:
    for index, row in df.iterrows():
        # 데이터베이스에 저장할 객체 생성 (열 이름을 실제 엑셀 파일의 열 이름과 일치시킵니다)
        politician = Politician(
            name=row['의원명'],
            party=row['정당'],
            constituency=row['지역'],
            contact=row['소속위원회'],
            gender=row['성별'],
            election_count=row['당선횟수'],
            election_method=row['당선방법']
        )
        # 데이터베이스에 객체 추가
        db.add(politician)

        # 데이터베이스에 변경사항 커밋
    db.commit()
except Exception as e:
        print(f"Error occurred: {e}")
        db.rollback()
finally:
    # 세션 종료
    db.close()

print("Data imported successfully!")
