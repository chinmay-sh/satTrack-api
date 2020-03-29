from app import app
#from .models.Satellite import Satellite
from .service import satellitesData
from flask import jsonify, render_template

@app.route('/satdata/topview/json')
def top100json():
    return jsonify({'data':satellitesData.satList})

@app.route('/satdata/topview/table')
def top100table():
    data = ''
    total = len(satellitesData.satList)
    return render_template('index.html',title='Home',total=total,data=data,sat_list = satellitesData.satList)