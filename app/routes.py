from app import app
from flask import render_template, jsonify, request
from app.forms import RunForm
from app.scripts import find_coords, triangle_point
import requests, random
import googlemaps

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/')
def data():
    clat = float(request.args.get('lat'))
    clng = float(request.args.get('lng'))
    cdist = float(request.args.get('dist'))
    theta = random.uniform(0.0,360.0)
    pair = find_coords(clat, clng, cdist * 0.3 * 1609.34, theta)
    r = requests.get("http://api.geonames.org/findNearestIntersectionOSMJSON?lat="+str(pair[0])+"&lng="+str(pair[1])+"&username=efrankel")
    generated_loc = [float(r.json()['intersection']['lat']),float(r.json()['intersection']['lng'])]
    third_point = triangle_point([clat, clng], generated_loc, cdist * 0.3 * 1609.34, theta)
    gmaps = googlemaps.Client(key='AIzaSyBEgWq5G822EXJIgfviFqJRf7vVE6_F5Lc')
    print([clat,clng], generated_loc, third_point)
    dir1 = gmaps.directions([clat, clng], generated_loc, mode="walking")
    dir2 = gmaps.directions(generated_loc, third_point, mode="walking")
    dir3 = gmaps.directions(third_point, [clat, clng], mode="walking")
    fin_list = [dir1[0]['legs'][0]['steps'][0]['start_location']]
    for line in dir1[0]['legs'][0]['steps']:
        fin_list.append(line['end_location'])
    for line in dir2[0]['legs'][0]['steps']:
        fin_list.append(line['end_location'])
    for line in dir3[0]['legs'][0]['steps']:
        fin_list.append(line['end_location'])
    return jsonify(fin_list)
