from fastapi import APIRouter
from fastapi.responses import JSONResponse

from service.db.admin import count_cost, find_all_users, get_statistics

router = APIRouter()


@router.get("/admin/check/user", name="get all users")
async def users(admin_ID: str) -> JSONResponse:
    return await find_all_users(admin_ID)


@router.get("/admin/cost", name="count cost")
async def cost(admin_ID: str) -> JSONResponse:
    return {"money": await count_cost(admin_ID)}


@router.get("/statistics", name="statistics")
async def statistics(
    start: str, end: str, city: str, community: str, type: str
) -> JSONResponse:
    return await get_statistics(start, end, city, community, type)
