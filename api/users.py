from fastapi import APIRouter, HTTPException
from models import UserModel
from utils import validate_object_id
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

router = APIRouter(prefix="/users", tags=["users"])


@router.post("")
async def create_user(user: UserModel):
    result = await db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id), "message": "User created"}


@router.put("/{user_id}")
async def update_user(user_id: str, user: UserModel):
    oid = validate_object_id(user_id)
    result = await db.users.update_one({"_id": oid}, {"$set": user.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated", "modified_count": result.modified_count}


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    oid = validate_object_id(user_id)
    result = await db.users.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}


@router.get("")
async def get_all_users():
    users = []
    async for user in db.users.find({}):
        user["_id"] = str(user["_id"])
        users.append(user)
    return users


@router.get("/{user_id}")
async def get_user_with_id(user_id: str):
    oid = validate_object_id(user_id)
    result = await db.users.find_one({"_id": oid})

    if not result:
        return {"message": "User not found"}

    result["_id"] = str(result["_id"])
    return result
