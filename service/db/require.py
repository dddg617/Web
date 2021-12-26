from typing import List
from bson import ObjectId
from .database import database

require_collection = database.get_collection("require")


def require_detail(require: dict) -> dict:
    return {
        "type": require["type"],
        "topic": require["topic"],
        "description": require["description"],
        # "doc": require["doc"],
        "number": require["number"],
        "time": require["create_time"],
        "state": require["state"],
    }


def extend_require_data(require: dict) -> dict:
    time = require.pop("time")
    new_data: dict = {
        "update_time": time,
        "create_time": time,
        "state": 0,
        "confirm_number": 0,
    }
    require.update(new_data)
    return require


def add_require_id(require: dict) -> dict:
    require["require_ID"] = str(require.pop("_id"))
    return require


async def post_require(require: dict):
    require = extend_require_data(require)
    result = await require_collection.insert_one(require)
    new_require = await require_collection.find_one(
        {"_id": result.inserted_id}
    )
    return add_require_id(new_require)


async def find_requires(data: dict) -> List[str]:
    requires = require_collection.find(data)
    return [
        str(require["_id"]) for require in await requires.to_list(length=None)
    ]


async def get_require_detail(require_ID: str) -> dict:
    require = await require_collection.find_one({"_id": ObjectId(require_ID)})
    return require_detail(require)


async def change_require(require_data: dict) -> bool:
    require_ID = require_data.pop("require_ID")
    result = await require_collection.update_one(
        {"_id": ObjectId(require_ID)}, {"$set": require_data}
    )
    return result.matched_count == 1


async def delete_require(require_ID: str) -> bool:
    result = await require_collection.delete_one({"_id": ObjectId(require_ID)})
    return result.deleted_count == 1


async def find_require_by_id(require_ID: str) -> dict:
    return add_require_id(
        await require_collection.find_one({"_id": ObjectId(require_ID)})
    )
