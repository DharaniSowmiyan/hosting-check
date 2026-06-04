from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard():
    return {
        "success": True,
        "message": "Dashboard API working"
    }