from flask import Blueprint

input = Blueprint('information',__name__)


@input.route('/')
def index():
    return "Input"
