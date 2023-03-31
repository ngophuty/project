from fastapi import FastAPI
from routers.router_a.views import router

app = FastAPI()
app.include_router(router)
