from app import app
from flask import render_template, redirect
from app.forms import RunForm

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input',methods=['GET','POST'])
def input():
    form = RunForm()
    if form.validate_on_submit():
        return render_template('map.html', distance=form.distance.data, pace=form.pace.data)
    return render_template('input.html', form=form)

@app.route('/map')
def map(distance, pace):
    return render_template('map.html',distance=distance, pace=pace)
