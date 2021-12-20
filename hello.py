from fastapi import FastAPI

app = FastAPI()

@app.get('/favicon.ico', include_in_schema=False)

@app.get("/")
async def root():
    return {"message": "Hello World"}