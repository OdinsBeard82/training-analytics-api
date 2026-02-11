from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.workouts import router as workouts_router
from app.db.init_db import init_db

app = FastAPI(title=settings.APP_NAME)

app.include_router(workouts_router)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

from app.core.config import settings
print("BOOT DATABASE_URL =", settings.DATABASE_URL)
