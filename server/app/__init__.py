from flask import Flask
from app.test_module.routes import test_module

app = Flask(__name__)

app.register_blueprint(test_module)

