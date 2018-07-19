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
        pair = find_coords(form.latitude.data, form.longitude.data, form.distance.data * 0.3, theta)
        r = requests.get("http://api.geonames.org/findNearestIntersectionOSMJSON?lat="+str(pair[0])+"&lng="+str(pair[1])+"&username=efrankel")
        generated_loc = [float(r.json()['intersection']['lat']),float(r.json()['intersection']['lng'])]
        third_point = triangle_point([form.latitude.data, form.longitude.data], generated_loc, form.distance.data * 0.4, theta)
        gmaps = googlemaps.Client(key='AIzaSyBEgWq5G822EXJIgfviFqJRf7vVE6_F5Lc')
        loc1 = gmaps.reverse_geocode((form.latitude.data, form.longitude.data))
        loc2 = gmaps.reverse_geocode((generated_loc[0], generated_loc[1]))
        loc3 = gmaps.reverse_geocode((third_point[0], third_point[1]))
        dir1 = gmaps.directions(loc1, loc2, mode="walking")
        dir2 = gmaps.directions(loc2, loc3, mode="walking")
        dir3 = gmaps.directions(loc3, loc1, mode="walking")
        return
    return render_template('input.html', form=form)

@app.route('/map')
def map(distance, pace, latitude, longitude):
    return render_template('map.html',distance = distance, pace = pace, latitude = latitude, longitude = longitude)
