from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attention', methods=['POST'])
def set_attention():
    url = request.form.get('url')
    socketio.emit('attention', {'url': url})
    return 'OK', 200

@app.route('/normal', methods=['POST'])
def set_normal():
    content = request.form.get('content')
    socketio.emit('normal', {'content': content})
    return 'OK', 200

if __name__ == '__main__':
    socketio.run(app, debug=True)
