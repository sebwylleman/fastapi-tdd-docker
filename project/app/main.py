from fastapi import Depends, FastAPI

from app.config import Settings, getSettings

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(getSettings)):
    return {"ping": "pong", "environment": settings.environment, "testing": settings.testing}
