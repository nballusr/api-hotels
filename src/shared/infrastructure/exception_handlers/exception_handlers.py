from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.shared.domain.exception.domain_exception import DomainException
from src.shared.domain.exception.not_found_exception import NotFoundException


async def not_found_exception_handler(_: Request, exception: NotFoundException):
    return JSONResponse(status_code=404, content={"message": exception.message})


async def domain_exception_handler(_: Request, exception: DomainException):
    return JSONResponse(status_code=400, content={"message": exception.message})


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(NotFoundException, not_found_exception_handler)
    app.add_exception_handler(DomainException, domain_exception_handler)
