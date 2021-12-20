from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base 				#+ Base 추가 


#클라이언트용 
class UserTable(Base):                 #+ 클래스로 변경, 이름변경 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)