from .. import router

@router.get("/index/", tags=["index"])
async def index(name: str = "Prime Labo"):
    return {
        "success": True,
        "content": f"Hello {name}!",
    }
