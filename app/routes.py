from app import app
from .service import satellitesData,issData,iss_crewDragon
from flask import jsonify,url_for,send_file

@app.route('/satdata/topview/json')
def topjson():
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/visual.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/satdata/active/json')
def activejson():
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/active.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/satdata/stations/json')
def stationjson():
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/stations.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/iss/json')
def issjson():
    return jsonify(issData.getData())

@app.route('/iss/map')
def issmap():
    issData.getMap()

@app.route('/satdata/starlink/json')
def starlinkjson():
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/starlink.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/static/issimg.png')
def disp():
    resp = send_file('../issimg.png',mimetype='image/png')
    return resp

@app.route('/cd')
def cd_issMap():
    iss_crewDragon.getMap()