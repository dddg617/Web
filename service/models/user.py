from pydantic import BaseModel, Field, constr
from typing import Optional


class UserModel(BaseModel):
    username: str = Field(...)
    name: str = Field(...)
    ID_type: str = Field(...)
    ID: str = Field(...)
    password: str = Field(...)
    phone: constr(min_length=11, max_length=11)
    introduction: str = Field(...)
    city: str = Field(...)
    community: str = Field(...)
    time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "dddg617",
                "name": "Yaoqi Liu",
                "ID_type": "マイナンバー",
                "ID": "1234567890D",
                "password": "dddg617",
                "phone": "12345678901",
                "introduction": "仁王2が好き",
                "city": "Osaka",
                "community": "Game",
                "time": "21-11-20",
            }
        }


class ChangeUserModel(BaseModel):
    user_ID: str = Field(...)
    phone: Optional[constr(min_length=11, max_length=11)]
    password: Optional[str]
    introduction: Optional[str]
    time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_ID": "61c85b58a333886260a1ac32",
                "phone": "12345678901",
                "password": "123456",
                "introduction": "仁王1が好き",
                "time": "21-12-20",
            }
        }


class UserLoginModel(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {"username": "716gdddd", "password": "123456"}
        }


class UserRequireModel(BaseModel):
    user_ID: str = Field(...)
    type: str = Field(...)
    topic: str = Field(...)
    description: str = Field(...)
    number: int = Field(..., gt=0)
    end_time: str = Field(...)
    time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_ID": "61c85b58a333886260a1ac32",
                "type": "社区志愿者",
                "topic": "帮忙搬物资",
                "description": "Stronger is better",
                "number": 3,
                "end_time": "21-12-01",
                "time": "21-11-30",
            }
        }


class ResponseConfirmModel(BaseModel):
    response_ID: str = Field(...)
    accept: bool = Field(...)

    class Config:
        schema_extra = {"example": {"response_ID": "1234", "accept": True}}


class ChangeRequireModel(BaseModel):
    require_ID: str = Field(...)
    type: Optional[str]
    topic: Optional[str]
    description: Optional[str]
    number: Optional[int]
    time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "require_ID": "1234",
                "type": "社区志愿者",
                "topic": "帮忙搬物资",
                "description": "Stronger is better",
                "number": 3,
                "time": "21-11-30",
            }
        }


class ResponseModel(BaseModel):
    user_ID: str = Field(...)
    require_ID: str = Field(...)
    description: str = Field(...)
    time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_ID": "61c80f87138933b4f15636f6",
                "require_ID": "61c80dc5966d65613dd83234",
                "description": "I can!",
                "time": "21-11-30",
            }
        }


class ChangeResponseModel(BaseModel):
    response_ID: str = Field(...)
    description: Optional[str]
    time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "response_ID": "61c80f87138933b4f15636f6",
                "description": "I can with another one's help!",
                "time": "21-12-01",
            }
        }


class DeleteRequire(BaseModel):
    require_ID: str = Field(...)


class DeleteResponse(BaseModel):
    response_ID: str = Field(...)
