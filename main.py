from typing import Union

from fastapi import FastAPI

environment = os.environ.get('environment', 'dev')

app = FastAPI(redoc_url='/docs')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    if environment == 'dev':
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=9000, log_level="debug", reload=True, workers=3)
