from app import app
from .service import satellitesData,issData
from flask import jsonify
from . import removeFile


@app.route('/satdata/topview/json')
def topjson():
    removeFile.remCall()
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/visual.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/satdata/active/json')
def activejson():
    removeFile.remCall()
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/active.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/satdata/stations/json')
def stationjson():
    removeFile.remCall()
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/stations.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})

@app.route('/satdata/iss/json')
def issjson():
    removeFile.remCall()
    return jsonify({'data':issData.getData()})

@app.route('/satdata/starlink/json')
def starlinkjson():
    removeFile.remCall()
    satellitesData.satList.clear()
    url = 'https://www.celestrak.com/NORAD/elements/starlink.txt'
    satellitesData.getData(url)
    return jsonify({'data':satellitesData.satList,'total':len(satellitesData.satList)})