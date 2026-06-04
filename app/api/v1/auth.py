from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.get("/test")
def auth_test():
    return {
        "success": True,
        "message": "Auth API working"
    }