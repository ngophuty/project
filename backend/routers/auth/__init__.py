from fastapi import APIRouter

router = APIRouter(
    prefix="/api/auth",
    responses={
        404: {
            "success": False,
            "error": "Not found"
        }
    },
)

# pylint: disable=unused-import, wrong-import-position
from .routes import auth
