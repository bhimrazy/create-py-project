from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import api

app = FastAPI()

app.include_router(api.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["home"])
def get_home():
    """Root Endpoint """
    return {"message": "Hello World"}
