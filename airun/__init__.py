from flask import Flask
from airun.main.controllers import main
from airun.input.controllers import input

app = Flask(__name__)

app.register_blueprint(main, url_prefix = '/')
app.register_blueprint(input, url_prefix = '/input')
