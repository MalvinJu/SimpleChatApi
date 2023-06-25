from fastapi import WebSocket
from starlette.websockets import WebSocketState

class SocketManager:
    def __init__(self):
        self.connections = {}

    async def connect(self, websocket: WebSocket, room_name: str, username: str):
        await websocket.accept()
        if self.connections.get(room_name, None) == None:
            self.connections[room_name] = []
        self.connections[room_name].append((websocket,username))

    def disconnect(self, websocket: WebSocket, room_name:str, username: str):
        self.connections[room_name].remove((websocket,username))
    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, data, room_name: str, sender: str):
        living_connections = []
        target_sockets = self.connections.get(room_name)
        while len(target_sockets) > 0:
            active_user_connection = self.connections[room_name].pop()
            user_socket: WebSocket = active_user_connection[0]
            if (user_socket.application_state == WebSocketState.CONNECTED):
                # if (active_user_connection[1] != sender):
                await user_socket.send_json(data) 
            living_connections.append(active_user_connection)
        self.connections[room_name] = living_connections