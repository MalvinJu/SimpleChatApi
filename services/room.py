import base64
from datetime import datetime
import secrets

from fastapi import HTTPException
from models.room import Room

rooms = []
def insert_room(user_name: str, room_name: str):
    if any(existingRoom.room_name == room_name for existingRoom in rooms):
        raise HTTPException(400, detail={"message": "Room already exists", "code": 1})
    room = Room(room_name=room_name, user_name=user_name)
    room.created_at = datetime.now()
    room.secret_key = base64.b64encode(secrets.token_bytes(32))
    room.noche = base64.b64encode(secrets.token_bytes(24))
    # room.members = [user_name] 
    rooms.append(room)
    return room

def get_room(room_name):
   selected_room = next((room for room in rooms if room.room_name == room_name), None)
   print(selected_room)
   if selected_room == None:
       raise HTTPException(400, detail={"message": "Room not exists", "code": 0})
   else:
       return selected_room
