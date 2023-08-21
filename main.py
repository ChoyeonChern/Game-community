# fastapi main
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import user
from app.database import engine
from app.api import login
from app.config import settings


# models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(post.router)
app.include_router(user.router)

app.include_router(auth.router)
app.include_router(vote.router)
# @app.get("/")
# def root():
#     return {"message": "Hello World"}
