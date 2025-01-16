from fastapi import FastAPI
from database import engine
import modelos
from router import router

modelos.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)