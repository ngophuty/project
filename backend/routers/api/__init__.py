from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    responses={
        404: {
            "success": False,
            "error": "Not found"
        }
    },
)

from .routes import index