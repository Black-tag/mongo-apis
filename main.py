from bson import ObjectId
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel




MONGO_URI="mongodb://localhost:27017"
DB_NAME="digicollect"

app = FastAPI()
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]


class UserModel(BaseModel):
    name: str
    role: str


def validate_object_id(id_str: str) -> ObjectId:
    try:
        return ObjectId(id_str)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user id")


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/users")
async def create_user(user: UserModel):
    result = await db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id), "message": "User created"}


@app.put("/users/{user_id}")
async def update_user(user_id: str, user: UserModel):
    oid = validate_object_id(user_id)
    result = await db.users.update_one({"_id": oid}, {"$set": user.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated", "modified_count": result.modified_count}


@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    oid = validate_object_id(user_id)
    result = await db.users.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}


@app.get("/users")
async def get_all_users():
    users = []
    async for user in db.users.find({}):
        user["_id"] = str(user["_id"])
        users.append(user)

    return users

@app.get("/users/{user_id}")
async def get_user_with_id(user_id: str):
    oid = validate_object_id(user_id)
    result = await db.users.find_one({"_id": oid})

    if not result:
        return {"message": "User not found"}

    result["_id"] = str(result["_id"])
    return result



@app.get("/insert")
async def test_db():
    await db.users.insert_one({
        "name": "Anand",
        "role": "backend dev"
    })

    return {"message": "Inserted successfully"}


@app.get("/insertmany")
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