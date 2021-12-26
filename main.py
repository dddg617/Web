from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


from service.endpoints import user, admin

routers = APIRouter()
routers.include_router(user.router)
routers.include_router(admin.router)


def init_app() -> FastAPI:
    app = FastAPI(title="API Service", debug=True)
    app.include_router(routers, prefix="/api")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # app.mount("/", StaticFiles(directory="static", html=True), name="static")
    return app


app = init_app()
