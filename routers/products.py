from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/products', tags=['products'], responses={404:{'message':'no encontrado'}})

product_list = ['pro','duc','tos','ideales']

@router.get('/')
async def products():
    return product_list

@router.get('/{id}')
async def products(id:int):
    try:
        return product_list[id]
    except:
        raise HTTPException(status_code=404, detail='No existen usuarios con ese ID')