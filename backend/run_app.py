import uvicorn
from config.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.FAPP_HOST,
        port=settings.FAPP_PORT,
        reload=settings.FAPP_RELOAD,
    )
