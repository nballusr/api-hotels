import os

from fastapi import APIRouter, status
from fastapi import FastAPI

from src.env import load_by_environment
from src.modules.hotel.ui.controllers.create_hotel import create_hotel_controller
from src.modules.hotel.ui.controllers.get_hotel import get_hotel_controller
from src.modules.hotel.ui.controllers.get_hotels import get_hotels_controller
from src.modules.hotel.ui.controllers.remove_hotel import remove_hotel_controller
from src.modules.hotel.ui.controllers.update_hotel import update_hotel_controller
from src.shared.infrastructure.exception_handlers.exception_handlers import register_exception_handlers
from src.shared.infrastructure.http_middlewares.middlewares import register_middlewares

load_by_environment(os.environ.get("APP_ENV", "dev"))

main_router = APIRouter(prefix="/api")


@main_router.get("/health-check")
def health_check():
    return status.HTTP_200_OK


main_router.include_router(create_hotel_controller.router)
main_router.include_router(get_hotel_controller.router)
main_router.include_router(get_hotels_controller.router)
main_router.include_router(update_hotel_controller.router)
main_router.include_router(remove_hotel_controller.router)

app = FastAPI(title="API-Hotels", docs_url="/api/docs", redoc_url="/api/redoc")
app.include_router(main_router)

register_middlewares(app)
register_exception_handlers(app)
