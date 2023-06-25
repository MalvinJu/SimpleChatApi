from datetime import datetime
import json
import uuid
from fastapi import APIRouter, FastAPI, WebSocket
from common.socket_manager import SocketManager
from starlette.websockets import WebSocketState

router = APIRouter()
manager = SocketManager()

@router.websocket("/chat/{room_name}/{user_name}")
async def websocket_endpoint(websocket: WebSocket, room_name, user_name):
    print(room_name + " " + user_name)
    await manager.connect(websocket, room_name, user_name)

    while True:
        if websocket.application_state == WebSocketState.CONNECTED:
            data = await websocket.receive_text()
            message = json.loads(data)
            message["username"] = user_name
            message["id"]=str(uuid.uuid4())
            message["datetime"]=datetime.now().strftime("%H:%M")

            await manager.broadcast(message, room_name, user_name)
        else:
            await manager.connect(websocket, room_name, user_name)

