from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from starlette.types import ASGIApp

from src.di.container_builder import ContainerBuilder


class CreateContainerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request.state.container = ContainerBuilder.build_container()

        try:
            return await call_next(request)
        except Exception as e:
            response = Response(status_code=500)
        finally:
            request.state.container.shutdown_resources()

        return response
