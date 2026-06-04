from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def products():
    return {
        "success": True,
        "message": "Products API working"
    }