from app import app
from .service import satellitesData,issData,orbitOverlap
from flask import jsonify,render_template,url_for
from . import removeFile

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/topview')
def topjson():
    removeFile.remCall()
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/visual.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/api/active')
def activejson():
    removeFile.remCall()
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/active.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/api/stations')
def stationjson():
    removeFile.remCall()
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/stations.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/api/iss')
def issjson():
    removeFile.remCall()
    return jsonify({'data':issData.getLocationData()})

@app.route('/api/issOrbit')
def issOrbit():
    removeFile.remCall()
    return jsonify({'data':issData.getOrbits()})

@app.route('/api/starlink')
def starlinkjson():
    removeFile.remCall()
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/starlink.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/api/orbitOverlap')
def orbitOverlapGet():
    removeFile.remCall()
    return jsonify({'data':orbitOverlap.getData()})