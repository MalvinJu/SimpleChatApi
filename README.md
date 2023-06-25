# Simple Chat API

A simple Chat API develop using FastAPI+websocket.

## Running the project

Before running the application, please make sure you have the following package installed.

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

Running the project.

```bash
uvicorn app:app --reload      
```

## Documentation

You can found the swagger docs at:
> base_url/docs

Below is the enpoint for chat websocket:
> ws://base_url/api/chat/{room_name}/{user_name}
