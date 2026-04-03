from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#db url설정
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/jsy"

#엔진 생성(sqlalchemy에서 db와 연결할 엔진 생성)
engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

#sqlalchemy orm의 부모클래스
Base=declarative_base() 