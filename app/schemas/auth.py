from pydantic import BaseModel


class OnboardingStatusResponse(BaseModel):
    success: bool
    message: str
    data: dict