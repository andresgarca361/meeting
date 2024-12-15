from flask import Flask, render_template
from flask_socketio import SocketIO

# Create a Flask application
app = Flask(__name__)
# Initialize SocketIO with the Flask app
socketio = SocketIO(app)

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an index.html in your templates directory

# Define a simple SocketIO event (example)
@socketio.on('message')
def handle_message(message):
    print('Received message: {}'.format(message))
    # You can emit back to the client if needed
    socketio.send('Message received: {}'.format(message))

# The main section to run the app for both development and production
if __name__ == '__main__':
    # This allows you to use allow_unsafe_werkzeug=True for development, if you want
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)  # Use this for local development
