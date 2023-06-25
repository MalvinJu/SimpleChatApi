from pydantic import BaseModel

class User(BaseModel):
    username: str
    client_id: str
