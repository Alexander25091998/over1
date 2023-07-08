from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import service

router = APIRouter()


@router.post('/create/{token_limit}')
async def create(token_limit: int, db: Session = Depends(get_db)):
    return service.create_token(token_limit, db)


@router.get('/use/{idd}')
async def use(idd: int = None, db: Session = Depends(get_db)):
    return service.use(idd, db)


@router.get('/list')
async def get_list(db: Session = Depends(get_db)):
    return service.get_all(db)
