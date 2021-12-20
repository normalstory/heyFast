#서버를 만들기 위한 세션 설정 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# SQLAlchemy 객체 관계형 매퍼
# 데이터베이스 테이블을 이용해 사용자가 정의한 
# 파이썬 클래스의 메소드와 각각의 행을 나타내는 인스턴스로 표현된다
# engine은 일반적으로 sqlalchemy.engine.create_engine 함수에 의해 생성되는, SQLAlchemy에서 사용되는 lowest level의 객체다. engine은 어플리케이션이 데이터베이스와 통신할 때마다 사용할 수 있는 connection pool을 유지한다. 쿼리를 위해 사용하는 engine.execute는 engine.connect(close_with_result=True)를 수행해 Connection 객체를 얻고, conn.execute를 호출하는 편리한 메소드다
# echo - logging 모듈 사용. 순수 SQL 코드를 제공한다
ENGINE = create_engine("mysql+pymysql://사용자 이름:비번@localhost:포트주소/데이터베이스이름")

conn = ENGINE.connect()

#데이터베이스와 대화가 필요할때 session을 불러서 쓰는것
#session 은 내부적으로 맵구조라서 세션의 반환값은 기존에 집어넣은 인스턴스 구조와 동일
session = scoped_session(
    sessionmaker(
        autocommit=False, #쿼리가 여러줄일때 한번에 반영하기 위함 
        autoflush=False, #상동( 커밋했을 경우만 반영되도록 하기 위해)
        bind=ENGINE
    )
)

# sqlalchemy는 declarative_base를 통해 2가지 일을 동시에 수행
# 몇개고 매핑 클래스를 만들 수 있는 Base 클래스를 생성 + 실제 디비 테이블에 연결
Base = declarative_base()

Base.query = session.query_property()
