from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine

app = FastAPI(
    title=settings.APP_NAME
)

@app.on_event("startup")
def dbInitialization():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}    
    