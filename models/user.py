from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base                  

# DB로 옮겨담을 그릇  
# 매핑 클래스 - Base를 통해 몇개고 매핑 클래스를 만들 수 있다.
class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)