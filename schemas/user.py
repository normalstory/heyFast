from pydantic import BaseModel

class User(BaseModel):
	id: int                       #+ class 구성에 맞춰서 id추가
	name: str
	email: str
	password: str