from typing import List
from bson import ObjectId
from .database import database

response_collection = database.get_collection("response_collection")


def extend_response_data(response_data: dict) -> dict:
    time = response_data.pop("time")
    response_data.update(
        {"state": 0, "create_time": time, "update_time": time}
    )
    return response_data


def add_response_id(response: dict) -> dict:
    response["response_ID"] = str(response.pop("_id"))
    return response


def response_info(response: dict) -> dict:
    return {
        "response_ID": str(response["_id"]),
        "user_ID": response["user_ID"],
        "description": response["description"],
        "time": response["create_time"],
    }


async def post_response(response_data: dict) -> dict:
    result = await response_collection.insert_one(
        extend_response_data(response_data)
    )
    response = await response_collection.find_one({"_id": result.inserted_id})
    return add_response_id(response)


async def find_responses_by_require_id(require_ID: str) -> List[dict]:
    responses = response_collection.find({"require_ID": require_ID})
    return [
        response_info(response)
        for response in await responses.to_list(length=None)
    ]


async def confirm_response(response_ID: str, accept: bool) -> bool:
    result = await response_collection.update_one(
        {"_id": ObjectId(response_ID)}, {"$set": {"state": 1 if accept else 2}}
    )
    return result.matched_count == 1


async def find_responses(data: dict) -> List[str]:
    responses = response_collection.find(data)
    return [
        str(response["_id"])
        for response in await responses.to_list(length=None)
    ]


async def find_response_by_id(response_ID: str) -> dict:
    return add_response_id(
        await response_collection.find_one({"_id": ObjectId(response_ID)})
    )


async def change_response(response_data: dict) -> bool:
    response_id = response_data.pop("response_ID")
    result = await response_collection.update_one(
        {"_id": ObjectId(response_id)}, {"$set": response_data}
    )
    return result.matched_count == 1


async def delete_response(response_id: str) -> bool:
    result = await response_collection.delete_one(
        {"_id": ObjectId(response_id)}
    )
    return result.deleted_count == 1
