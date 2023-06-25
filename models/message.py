import datetime
from pydantic import BaseModel
from user import User

class Message(BaseModel):
    user: User
    content: str = None
    timestamp: datetime = datetime.utcnow