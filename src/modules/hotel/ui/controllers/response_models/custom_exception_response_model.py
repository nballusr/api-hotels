from pydantic import BaseModel


class CustomExceptionResponseModel(BaseModel):
    message: str
