import uvicorn
from fastapi import FastAPI
import random


app = FastAPI()


@app.get('/generate_task')
async def generate_task():
    return {
        'first': random.randint(1, 10),
        'znak': '+-*/'[random.randint(0, 3)],
        'second': random.randint(1, 10),
    }


if __name__ == '__main__':
    uvicorn.run(
        'task_generator:app',
        host='localhost',
        port=8082,
        reload=True
    )
