from datetime import datetime
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


def convert_to_datetime(time_string: str) -> datetime:
    try:
        date_obj = datetime.strptime(time_string, "%Y-%m-%d")
    except Exception as err:
        print(str(err))
        return None
    return date_obj


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
            cost += 4 * require["number"]
    return cost


async def get_statistics(
    start: str, end: str, city: str, community: str, type: str
) -> List[dict]:
    start = convert_to_datetime(start)
    end = convert_to_datetime(end)
    if not start or not end:
        return []
    month_dict = {}
    async for user in user_collection.find(
        {"community": community, "city": city}
    ):
        user_id = str(user["_id"])
        async for require in require_collection.find(
            {"type": type, "user_ID": user_id}
            if type
            else {"user_ID": user_id}
        ):
            if require.get("confirm_number", 0) < require["number"]:
                continue
            start_time = convert_to_datetime(require["create_time"])
            end_time = convert_to_datetime(require["end_time"])
            if not start_time or not end_time:
                continue
            if start_time >= start and end_time <= end:
                month = require["create_time"][:7]
                month_dict[month] = (
                    month_dict.get(month, 0) + 4 * require["number"]
                )

    return [{"time": k, "money": v} for k, v in month_dict.items()]
