from app import app
from flask import render_template, redirect
from app.forms import RunForm
from app.scripts import find_coords, triangle_point
import requests
import json

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET','POST'])
def input():
    form = RunForm()
    if form.validate_on_submit():
        print([form.latitude.data, form.longitude.data])
        pair = find_coords(form.latitude.data, form.longitude.data, form.distance.data * 0.3)
        print(pair)
        r = requests.get("http://api.geonames.org/findNearestIntersectionOSMJSON?lat="+str(round(pair[0],3))+"&lng="+str(round(pair[1],2))+"&username=efrankel")
        generated_loc = [float(r.json()['intersection']['lat']),float(r.json()['intersection']['lng'])]
        print(generated_loc)
        third_point = triangle_point([form.latitude.data, form.longitude.data], generated_loc, form.distance.data * 0.4)
        print(third_point)
        return [[form.latitude.data, form.longitude.data], generated_loc, third_point]
    return render_template('input.html', form=form)

@app.route('/map')
def map(distance, pace, latitude, longitude):
    return render_template('map.html',distance = distance, pace = pace, latitude = latitude, longitude = longitude)
