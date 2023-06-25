from fastapi import APIRouter
from models.user import User
from services.user import insert_user

router = APIRouter()

@router.post("/user", tags=["Users"])
async def create_user(
    request: User
):
    return insert_user(request)
