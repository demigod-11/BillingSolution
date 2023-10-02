from typing import Dict

from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/api/")  # type: ignore
async def root() -> Dict[str, str]:
    return {"message": "Hello, World!"}
