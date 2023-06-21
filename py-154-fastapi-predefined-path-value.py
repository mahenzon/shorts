"""
Install packages:

```
pip install fastapi uvicorn
```
"""
from enum import Enum

import uvicorn
from fastapi import FastAPI

app = FastAPI()


class OptionName(str, Enum):
    django = "Django"
    flask = "Flask"
    fastapi = "FastAPI"


@app.get("/frameworks/{fw_name}")
def get_fw(fw_name: OptionName):
    if fw_name is OptionName.django:
        return {
            "model_name": fw_name,
            "message": "Django is great!",
        }

    if fw_name is OptionName.flask:
        return {
            "model_name": fw_name,
            "message": "Do it yourself.",
        }

    return {
        "model_name": fw_name,
        "message": "FastAPI for the win!",
    }


if __name__ == "__main__":
    uvicorn.run(app)
