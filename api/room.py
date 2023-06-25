from fastapi import APIRouter
from services import insert_room
from common.request import RoomRequest
from services.room import get_room

router = APIRouter()

@router.post("/room", tags=["Rooms"])
async def create_room(
    request: RoomRequest
):
    return insert_room(request.username, request.room_name)

@router.get("/room/{room_name}", tags=["Rooms"])
async def fetch_room(
    room_name: str
):
    return get_room(room_name)   

