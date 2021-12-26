from typing import List
from .database import database

from bson import ObjectId

user_collection = database.get_collection("user")


def user_info(user: dict) -> dict:
    return {
        "username": user["username"],
        "name": user["name"],
        "ID": user["ID"],
        "phone": user["phone"],
        "introduction": user["introduction"],
        "city": user["city"],
        "community": user["community"],
    }


def add_time(user_data: dict) -> dict:
    time = user_data.pop("time")
    user_data.update(
        {
            "register_time": time,
            "update_time": time,
        }
    )
    return user_data


def add_user_id(user: dict) -> dict:
    user["user_ID"] = str(user.pop("_id"))
    return user


async def add_user(user_data: dict, is_admin: bool = False) -> dict:
    user_data = add_time(user_data)
    user_data["isAdmin"] = is_admin
    result = await user_collection.insert_one(user_data)
    user = await user_collection.find_one({"_id": result.inserted_id})
    user = add_user_id(user)
    return user


async def find_user_by_id(user_ID: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(user_ID)})
    return user_info(user)


async def change_user_info(new_user_info: dict) -> bool:
    user_ID = new_user_info.pop("user_ID")
    new_user_info = add_time(new_user_info)
    result = await user_collection.update_one(
        {"_id": ObjectId(user_ID)}, {"$set": new_user_info}
    )
    return result.matched_count == 1


async def find_user_by_login_info(user_info: dict) -> dict:
    user = await user_collection.find_one(user_info)
    if not user:
        return None
    user = add_user_id(user)
    return user


async def find_users(data: dict) -> List[str]:
    users = user_collection.find(data)
    return [str(user["_id"]) for user in await users.to_list(length=None)]


# no use
async def find_all_user() -> List[dict]:
    users = user_collection.find({})
    return [add_user_id(user) for user in await users.to_list(length=None)]


async def delete_all_user() -> None:
    await user_collection.delete_many({})
    return
