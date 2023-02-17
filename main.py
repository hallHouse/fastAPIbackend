from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root():
    return 'Hola FastAPI'
    
@app.get("/url")
async def url():
    return {'url':'www.google.com', 'edad':34, 'name':'sergio'}