from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from models.user import User

class Room(BaseModel):
    def __init__(self, room_name, user_name):
        super().__init__(room_name=room_name, created_by=user_name, created_at = datetime.now())
    created_at: datetime
    room_name: str
    members: Optional[List[User]] = []
    created_by: str
    encryption_key: Optional[str]
    active: bool = False
    noche: Optional[str]
    secret_key: Optional[str]