from app import *

@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
def clientToServer(sid, data):
    print("message ", data['text'])
    response = chatbot.chat(data['text'])
    sio.emit("serverToClient", response)
    print("response ", response)


@sio.event
def disconnect(sid):
    print("disconnect ", sid)

