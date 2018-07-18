from app import app
from flask import render_template
from app.forms import RunForm

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def input():
    form = RunForm()
    return render_template('input.html')
