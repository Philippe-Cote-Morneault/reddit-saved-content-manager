from flask import Flask
from app.saved_content.controller import test_module

app = Flask(__name__)

app.register_blueprint(test_module)

