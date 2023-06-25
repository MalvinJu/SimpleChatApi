from fastapi import APIRouter
from api.room import router as room_router
from api.user import router as user_router
from api.chat import router as chat_router

router = APIRouter()
router.include_router(room_router)
router.include_router(user_router)
router.include_router(chat_router)
