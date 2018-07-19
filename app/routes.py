from app import app
from flask import render_template
from app.forms import RunForm
from app.scripts import find_coords, triangle_point
import requests, random
import googlemaps

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET','POST'])
def input():
    form = RunForm()
    if form.validate_on_submit():
        theta = random.uniform(0.0,360.0)
        pair = find_coords(form.latitude.data, form.longitude.data, form.distance.data * 0.3 * 1609.34, theta)
        r = requests.get("http://api.geonames.org/findNearestIntersectionOSMJSON?lat="+str(pair[0])+"&lng="+str(pair[1])+"&username=efrankel")
        generated_loc = [float(r.json()['intersection']['lat']),float(r.json()['intersection']['lng'])]
        third_point = triangle_point([form.latitude.data, form.longitude.data], generated_loc, form.distance.data * 0.4 * 1609.34, theta)
        gmaps = googlemaps.Client(key='AIzaSyBEgWq5G822EXJIgfviFqJRf7vVE6_F5Lc')
        dir1 = gmaps.directions([form.latitude.data, form.longitude.data], generated_loc, mode="walking")
        dir2 = gmaps.directions(generated_loc, third_point, mode="walking")
        dir3 = gmaps.directions(third_point, [form.latitude.data, form.longitude.data], mode="walking")
        print([form.latitude.data, form.longitude.data], generated_loc, third_point)
        return
    return render_template('input.html', form=form)

@app.route('/map')
def map(distance, pace, latitude, longitude):
    return render_template('map.html',distance = distance, pace = pace, latitude = latitude, longitude = longitude)
