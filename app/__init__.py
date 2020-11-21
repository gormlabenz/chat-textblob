import socketio
from app.chatbot import Chatbot

sio = socketio.Server(cors_allowed_origins="http://localhost:8080")
app = socketio.WSGIApp(sio)
chatbot = Chatbot('app/intents.json')

from app import events