"""
Install packages:
```
pip install fastapi uvicorn
pip install "pydantic[email]"
```
"""
import uvicorn
from fastapi import FastAPI
from pydantic import EmailStr

app = FastAPI()

# a sample user database or storage
users_db = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
]

users_map = {
    info["email"]: info
    for info in users_db
}


@app.get("/users/")
def search_user_by_email(email: EmailStr):
    if user_info := users_map.get(email):
        return user_info
    return {"message": "User not found"}


if __name__ == "__main__":
    uvicorn.run(app)
