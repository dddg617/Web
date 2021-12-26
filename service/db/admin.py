from typing import List
from .database import database

from bson import ObjectId

user_collection = database.get_collection("user")
require_collection = database.get_collection("require")
response_collection = database.get_collection("response_collection")


def user_info(data: dict) -> dict:
    return {
        "username": data["username"],
        "name": data["name"],
        "ID_type": data["ID_type"],
        "ID": data["ID"],
        "phone": data["phone"],
        "introduction": data["introduction"],
        "city": data["city"],
        "community": data["community"],
        "time": data["register_time"],
    }


async def is_admin(admin_id: str) -> bool:
    info = await user_collection.find_one({"_id": ObjectId(admin_id)})
    return info["isAdmin"]


async def find_all_users(admin_id: str) -> List[dict]:
    if not await is_admin(admin_id):
        return []
    infos = user_collection.find({"isAdmin": False})
    return [user_info(user) for user in await infos.to_list(length=None)]


async def count_cost(admin_id: str) -> int:
    if not await is_admin(admin_id):
        return 0
    requires = require_collection.find({})
    cost = 0
    for require in await requires.to_list(length=None):
        if require["number"] <= require.get("confirm_number", 0):
            cost += 3 * require["number"]
    responses = response_collection.find({"state": 1})
    cost += len(await responses.to_list(length=None))
    return cost
