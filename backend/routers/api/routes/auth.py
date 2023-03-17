import pydantic

from .. import router


class LoginInfo(pydantic.BaseModel):
    username: str
    password: str

@router.get("/login/", tags=["auth"])
async def login(info: LoginInfo):
    return {
        "success": True,
        "token": "Some token"
    }
