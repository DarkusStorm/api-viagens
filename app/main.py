from fastapi import FastAPI
from app.database import Base, engine
from app.route.viagem import viagem

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(viagem)

@app.get("/")
async def health_check():
    return {"status": "API Online"}