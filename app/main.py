
from fastapi import FastAPI    #To Run the Server : uvicorn main:app ,  uvicorn main:app --reload  --> to watch the server continuously for any updates
from fastapi.middleware.cors import CORSMiddleware
from . import models
from . database import engine
from .routers import post, user, auth, vote
from .config import Settings

settings = Settings()

# models.Base.metadata.create_all(bind=engine)    --# it's not needed Since we incorporated the Alembic to maintain/create the database tables

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World asd"}




# VIDEO PAUSED @ : 47 : 12 SEC




