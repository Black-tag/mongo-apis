from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from api import health_router, users_router, test_router
from config import settings


def create_app():
    app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    
    # Include routers
    app.include_router(health_router)
    app.include_router(users_router)
    app.include_router(test_router)
    
    return app


app = create_app()


