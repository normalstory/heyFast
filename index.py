from fastapi import FastAPI
from route.index import user

app=FastAPI()
app.include_router(user)