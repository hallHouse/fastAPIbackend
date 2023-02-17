from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 


app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

class User(BaseModel):
    userame: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password:str

users_db = {
    "xrpew":{
        "username": "xrpew",
        "full_name": "sergio perez",
        "email":"sergio@mail.com",
        "disabled":False,
        "password":"123456"
    },
    "xrpew2":{
        "username": "xrpew2",
        "full_name": "sergio perez 2",
        "email":"sergio2@mail.com",
        "disabled":True,
        "password":"654321"
    }
}

async def current_user(token:str = Depends(oauth2)):
    user= search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='no estás autorizado para esta opcion'
        )

def search_user(username:str):
    if username in users_db:
        return UserDB(users_db[username])

@app.post('/login')
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=404 , detail='el usuario no es correcto')
    
    user = search_user(form.username)
    if not form.password == user_db.password:
        raise HTTPException(
            status_code=400,
            detail='contraseña incorrecta'
        )
    return {
        "acces_token" : user.username , "token_type" : "bearer"
    }

@app.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user