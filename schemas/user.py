# UI에서 입력된 내용을 받을 그릇
# -> B내에 어떤 구조로 데이터에 저장되는가를 나타내는 데이터베이스구조 선언 

from pydantic import BaseModel

class User(BaseModel):
	id: int                              #+ class 구성에 맞춰서 id추가
	name: str
	email: str
	password: str