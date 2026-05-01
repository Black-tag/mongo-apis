from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

router = APIRouter(tags=["test"])


@router.get("/insert")
async def test_db():
    await db.users.insert_one({
        "name": "Anand",
        "role": "backend dev"
    })
    return {"message": "Inserted successfully"}


@router.get("/insertmany")
async def test_db_many_insert():
    await db.users.insert_many([{
        "name": "Anand",
        "role": "backend dev",

    }, {
        "name": "A",
        "role": "backend dev"
    }, {
        "name": "An",
        "role": "backend dev"
    }, {
        "name": "Ana",
        "role": "backend dev"
    }, {
        "name": "Anan",
        "role": "backend dev"
    }])
    return {"message": "insert many succeed"}
