from fastapi import APIRouter, Request 			#+ Request 
from config.db import session 					#+ session 
from models.index import UserTable				#+ UserTable
	
from fastapi.templating import Jinja2Templates 
templates = Jinja2Templates(directory="templates")

user = APIRouter()

@user.get("/helloJinja")
async def read_data(request: Request):		
    context = {}								# <- 이전에 배열로 출력되는 부분
    users = session.query(UserTable).all()		#+ 
    context['request'] = request
    context['users'] = users

    return templates.TemplateResponse("helloJinja.html", context)	#+ 