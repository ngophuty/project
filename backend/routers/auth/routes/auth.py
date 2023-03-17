from .. import router

from ..models.requests import LoginRequest

@router.get("/login/", tags=["auth"])
async def login(data: LoginRequest):
    return {
        "success": True,
        "token": "Some token"
    }
