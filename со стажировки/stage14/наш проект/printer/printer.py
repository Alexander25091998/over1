import uvicorn
from fastapi import FastAPI
import requests


app = FastAPI()


@app.get('/print/{idd}')
async def test_api(idd: int = None):
    res = requests.get(f'http://localhost:8083/token/use/{idd}').json()
    if 'token_count' in res and res['token_count'] < res['token_limit']:
        task = requests.get(f'http://localhost:8082/generate_task').json()
        print(f"{task['first']} {task['znak']} {task['second']} = ?")
        return task
    else:
        print(res)
        return res


if __name__ == '__main__':
    uvicorn.run(
        'printer:app',
        host='localhost',
        port=8081,
        reload=True
    )
