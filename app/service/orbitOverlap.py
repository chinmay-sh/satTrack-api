from skyfield.api import Topos, load
import numpy as np
from flask import jsonify

ts = load.timescale()

satellites = load.tle_file('https://www.celestrak.com/NORAD/elements/stations.txt')
# sat = satellites[0]

def getData():
    satOrbits = []
    for sat in satellites:
        satOrbits.append(getOrbits(sat))
    return satOrbits

def getOrbits(sat):
    t_utc_now = ts.now().utc_datetime()
    # t_utc_now = ts.utc(2020,7,4,12,0,0)
    minutes = np.arange(0, 90, 0.1) # about one orbit
    year = int(t_utc_now.strftime("%Y"))
    month = int(t_utc_now.strftime("%m"))
    date = int(t_utc_now.strftime("%d"))
    # hour = int(t_utc_now.strftime("%H"))

    # manually set time specs
    # year = 2020
    # month = 7
    # date = 4
    hour = 12

    t_utc_now = ts.utc(year,month,date,hour,0,0).utc_datetime()

    # times for orbits
    times = ts.utc(year,month,date,hour,minutes)

    # current orbit
    geocentric = sat.at(times)
    subsatLat = geocentric.subpoint().latitude.degrees
    subsatLong = geocentric.subpoint().longitude.degrees

    coordinateArr = []

    for i in range(len(subsatLat)):
        coordinateArr.append([subsatLong[i],subsatLat[i]])
    
    # print(coordinateArr)
    return ({'name':str(sat.name),'number':str(sat.model.satnum),
        'timestamp': str(t_utc_now),
        'orbitalData': coordinateArr
    })