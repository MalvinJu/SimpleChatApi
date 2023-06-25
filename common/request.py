from pydantic import BaseModel

class RoomRequest(BaseModel):
    username: str
    room_name: str