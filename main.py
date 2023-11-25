from fastapi import FastAPI
from routes.routes import tourism


app = FastAPI()
app.include_router(tourism)

