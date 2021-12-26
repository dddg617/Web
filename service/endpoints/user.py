from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from service.db.response import (
    change_response,
    confirm_response,
    delete_response,
    find_response_by_id,
    find_responses,
    find_responses_by_require_id,
    post_response,
)

from service.models.user import (
    ChangeRequireModel,
    ChangeResponseModel,
    ChangeUserModel,
    DeleteRequire,
    DeleteResponse,
    ResponseConfirmModel,
    ResponseModel,
    UserLoginModel,
    UserModel,
    UserRequireModel,
)
from service.db.user import (
    add_user,
    delete_all_user,
    find_user_by_id,
    find_user_by_login_info,
    find_all_user,
    change_user_info,
    find_users,
)
from service.db.require import (
    change_require,
    delete_require,
    find_require_by_id,
    find_requires,
    get_require_detail,
    post_require,
)

router = APIRouter()


@router.post("/user/register", name="register")
async def register(user_data: UserModel) -> JSONResponse:
    user_data: dict = jsonable_encoder(user_data)
    user: dict = await add_user(user_data)
    return {"success": True, "user_ID": user["user_ID"]}


@router.get("/user/check", name="check")
async def check(user_ID: str) -> JSONResponse:
    user_info: dict = await find_user_by_id(user_ID)
    return user_info


@router.post("/user/change", name="change")
async def change(user: ChangeUserModel) -> JSONResponse:
    new_user_info: dict = jsonable_encoder(user)
    new_user_info = {k: v for k, v in new_user_info.items() if v is not None}
    return {"success": await change_user_info(new_user_info)}


@router.post("/user/login", name="login")
async def login(user_info: UserLoginModel) -> JSONResponse:
    user_info: dict = jsonable_encoder(user_info)
    user_info: dict = await find_user_by_login_info(user_info)
    if not user_info:
        return {"success": False, "user_ID": "", "isAdmin": False}
    return {
        "success": True,
        "user_ID": user_info["user_ID"],
        "isAdmin": user_info["isAdmin"],
    }


@router.post("/user/require", name="require")
async def require(require: UserRequireModel) -> JSONResponse:
    require: dict = jsonable_encoder(require)
    require: dict = await post_require(require)
    return {"success": True, "require_ID": require["require_ID"]}


@router.get("/user/require_check", name="require")
async def check_require(user_ID: str) -> JSONResponse:
    return await find_requires({"user_ID": user_ID})


@router.get("/user/require_check/details", name="require detail")
async def require_detail(require_ID: str) -> JSONResponse:
    return await get_require_detail(require_ID)


@router.get("/user/require_check/response_check", name="response check")
async def response_check(require_ID: str) -> JSONResponse:
    results = await find_responses_by_require_id(require_ID)
    ret = []
    for result in results:
        user = await find_user_by_id(result["user_ID"])
        ret.append({**result, "name": user["username"]})
    return ret


@router.post("/user/require_check/response_confirm", name="response confirm")
async def response_confirm(confirm_data: ResponseConfirmModel) -> JSONResponse:
    result = await confirm_response(
        confirm_data.response_ID, confirm_data.accept
    )
    if result and confirm_data.accept:
        response = await find_response_by_id(confirm_data.response_ID)
        require = await find_require_by_id(response["require_ID"])
        result = await change_require(
            {
                "require_ID": require["require_ID"],
                "confirm_number": max(
                    require["number"], require.get("confirm_number", 0) + 1
                ),
                "state": 1
                if require.get("confirm_number", 0) >= require["number"]
                else require["state"],
            }
        )
    return {"success": result}


@router.post("/user/require_check/require_change", name="require change")
async def require_change(new_require_data: ChangeRequireModel) -> JSONResponse:
    new_require_data: dict = jsonable_encoder(new_require_data)
    new_require_data = {
        k: v for k, v in new_require_data.items() if v is not None
    }
    return {"success": await change_require(new_require_data)}


@router.post("/user/require_check/require_delete", name="delete require")
async def require_delete(require: DeleteRequire) -> JSONResponse:
    return {"success": await delete_require(require.require_ID)}


@router.get("/user/require", name="get require by community")
async def get_require(community: str) -> JSONResponse:
    user_ids: List[str] = await find_users({"community": community})
    ret = []
    for user_id in user_ids:
        ret = ret + await find_requires({"user_ID": user_id})
    return ret


@router.get("/user/response_check", name="response check")
async def check_response(user_ID: str) -> JSONResponse:
    return await find_responses({"user_ID": user_ID})


@router.get("/user/response_check/details", name="check self response detail")
async def response_detail(response_ID: str) -> JSONResponse:
    response = await find_response_by_id(response_ID)
    return {
        "require_ID": response["require_ID"],
        "description": response["description"],
        "time": response["create_time"],
        "state": response["state"],
    }


@router.post("/user/response_change", name="change response")
async def response_change(
    new_response_data: ChangeResponseModel,
) -> JSONResponse:
    new_response_data: dict = jsonable_encoder(new_response_data)
    new_response_data = {
        k: v for k, v in new_response_data.items() if v is not None
    }
    return {"success": await change_response(new_response_data)}


@router.post("/user/response_delete", name="delete response")
async def response_delete(response: DeleteResponse) -> JSONResponse:
    return {"success": await delete_response(response.response_ID)}


@router.post("/user/response", name="response")
async def response(response_data: ResponseModel) -> JSONResponse:
    response_data: dict = jsonable_encoder(response_data)
    response: dict = await post_response(response_data)
    return {"success": True, "response_ID": response["response_ID"]}


# No use
@router.get("/user/all", name="Get All User")
async def all() -> JSONResponse:
    users: list = await find_all_user()
    return users


@router.post("/user/delete/all", name="Delete All User")
async def delete() -> JSONResponse:
    await delete_all_user()
    return {}


@router.post("/user/admin/", name="add admin")
async def add_admin(user_data: UserModel) -> JSONResponse:
    user_data: dict = jsonable_encoder(user_data)
    user: dict = await add_user(user_data, True)
    return {"success": True, "user_ID": user["user_ID"]}
