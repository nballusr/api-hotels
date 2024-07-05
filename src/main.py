from fastapi import APIRouter, status
from fastapi import FastAPI

main_router = APIRouter(prefix="/api")


@main_router.get("/health-check")
def health_check():
    return status.HTTP_200_OK


app = FastAPI(title="API-Hotels")
app.include_router(main_router)
