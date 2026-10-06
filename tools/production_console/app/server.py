import secrets
from flask import Flask
from config import HOST, PORT
from routes_session import bp as session_bp
from routes_qualification import bp as qualification_bp
from routes_drive import bp as drive_bp

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.register_blueprint(session_bp)
app.register_blueprint(qualification_bp)
app.register_blueprint(drive_bp)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)
