from fastapi import APIRouter
from app.schemas.auth import OnboardingStatusResponse

router = APIRouter(
    prefix="/onboarding",
    tags=["Onboarding"]
)


@router.get("/status", response_model=OnboardingStatusResponse)
def get_onboarding_status():
    return {
        "success": True,
        "message": "Onboarding status fetched",
        "data": {
            "current_step": 2,
            "completed_steps": [1],
            "onboarding_status": "in_progress",
            "saved_values": {
                "role_type": "brand_owner",
                "brand_name": "ABC Fashions"
            }
        }
    }