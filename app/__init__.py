from flask import Flask
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex()
app.config["TEMPLATES_AUTO_RELOAD"] = True

from app import routes