import uvicorn
from fastapi import FastAPI, Depends
import router
from database import Base, engine


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router.router, prefix='/token')


if __name__ == '__main__':
    uvicorn.run(
        'token_service:app',
        host='localhost',
        port=8083,
        reload=True
    )
