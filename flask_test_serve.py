from flask import Flask
from flask import request
import requests

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return open('index.html', 'r').read()

@socketio.on('message')
def message(message):
	print(message)

@socketio.on('do_smth')
def func_call(message):
	print("I'm gonna do smth on server side")
	x = 5
	emit(x * x)


# messages = []

# messages = {
# 	'time': 123123,
# 	'text': 'something'
# }

# @app.route('/chat')
# def index():
#     return generate_html(messages)


@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)