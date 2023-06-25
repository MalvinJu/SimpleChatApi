from fastapi import HTTPException
from models.user import User

users = []
def insert_user(user: User):
    if any(existingUser.username == user.username for existingUser in users):
        raise HTTPException(400, detail={"message": "Room already exists", "code": 1})
    users.append(user)
    return user
