from fastapi import APIRouter, status
from fastapi import FastAPI

from src.modules.hotel.ui.controllers.get_hotel import get_hotel_controller

main_router = APIRouter(prefix="/api")


@main_router.get("/health-check")
def health_check():
    return status.HTTP_200_OK


main_router.include_router(get_hotel_controller.router)

app = FastAPI(title="API-Hotels")
app.include_router(main_router)
