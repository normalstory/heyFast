from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# SQLAlchemy 객체 관계형 매퍼
ENGINE = create_engine("mysql+pymysql://사용자 이름:비번@localhost:포트주소/데이터베이스이름")
 
conn = ENGINE.connect()

#session을 통해 데이터베이스와 통신
session = scoped_session(
    sessionmaker(
        autocommit=False, 
        autoflush=False, 
        bind=ENGINE
    )
)

#Base 클래스를 생성 + 실제 디비 테이블에 연결
Base = declarative_base()
Base.query = session.query_property()