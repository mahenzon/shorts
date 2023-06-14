import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello, world!"}


@app.get("/add")
def add_nums(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "total": a + b,
    }


if __name__ == "__main__":
    uvicorn.run(app)
