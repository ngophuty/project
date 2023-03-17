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

# pylint: disable=unused-import, wrong-import-position
from .routes import index
