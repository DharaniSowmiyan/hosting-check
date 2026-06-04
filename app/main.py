from fastapi import FastAPI

from app.api.v1 import auth
from app.api.v1 import onboarding
from app.api.v1 import dashboard
from app.api.v1 import products

app = FastAPI(
    title="VASTRA Backend API",
    description="Production-ready core engine API documentation for VASTRA",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(onboarding.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "VASTRA Backend Running"}