from fastapi import FastAPI

from src.shared.infrastructure.http_middlewares.create_container import CreateContainerMiddleware

middlewares = [
    [
        CreateContainerMiddleware,
        {},
    ]
]


def register_middlewares(app: FastAPI):
    for cls, params in middlewares:
        app.add_middleware(cls, **params)
