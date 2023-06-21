"""
Install packages:

```
pip install fastapi uvicorn
```
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
def read_user_me():
    return {
        "user_id": "current user",
    }


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run(app)
