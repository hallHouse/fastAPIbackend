from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Entidad user
class User(BaseModel):
    id: int
    name:str
    surname:str
    url:str
    edad:int

user_list = [User(id=1,name='sergio',surname='xrpew',url='www.com',edad=23),
            User(id=2,name='sergio',surname='xrpew',url='www.com',edad=23),
            User(id=3,name='sergio',surname='xrpew',url='www.com',edad=23)]

@router.get('/json')
async def usersjson():
    return [{'name':'sergio', 'surname':'xrpew', 'url':'xrpew.com', 'edad':34},
    {'name':'gaby', 'surname':'any', 'url':'xrpew.com', 'edad':34},
    {'name':'alejandro', 'surname':'ale', 'url':'google.com', 'edad':34},
    {'name':'perez', 'surname':'pew', 'url':'xrpew.com', 'edad':34}]

@router.get('/users')
async def users():
    return user_list

# Path
@router.get('/user/{id}')
async def user(id:int):
    return search_user(id)

# Query
@router.get('/user/')
async def user(id:int):
    return search_user(id)

@router.post('/user/', status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail='El usuario ya existe')

    user_list.append(user) 
    return {'ok':'Usuario agregado'}

@router.put('/user/')
async def user(user:User):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True    
    if not found:
        raise HTTPException(status_code=404, detail='El usuario no existe')
        
    return {'ok':'usuario actualizado' }

@router.delete('/user/{id}')
async def user(id:int):

    found = False

    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True

    if not found:
        return {'error':'usuario no encontrado'}

    return {'ok':'usuario eliminado'}


def search_user(id:int):
    user= filter(lambda user:user.id == id, user_list)
    try:
        return list(user)[0]
    except:
        return {'error':'usuario no encontrado'}
