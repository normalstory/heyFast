from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.user import User

user = APIRouter()

@user.get("/")
async def read_data():
	return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id: int):
	return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def write_data(user: User):
	conn.execute(users.insert().values(
		name=user.name,
		email=user.email,
		password=user.password
	)).fetchall()
	return conn.execute(users.select()).fetchall()

@user.put("/{id}")
async def update_data(id:int, user:User):
	conn.execute(users.update(
		name=user.name,
		email=user.email,
		password=user.password
	)).where(user.c.id ==id)
	return conn.execute(users.select()).fetchall()

@user.delete("/")
async def delete_data():	
	conn.execute(users.delete()).where(user.c.id ==id)
	return conn.execute(users.select).fetchall()


# fetch 메서드
#	fetchall() 메서드는 모든 데이타를 한꺼번에 클라이언트로 가져올 때 사용
#	fetchone()은 한번 호출에 하나의 Row 만을 가져올 때 사용
#	fetchone()을 여러 번 호출하면, 호출 때 마다 한 Row 씩 데이타를 가져올 때 사용
#	fetchmany(n) 메서드는 n개 만큼의 데이타를 한꺼번에 가져올 때 사용