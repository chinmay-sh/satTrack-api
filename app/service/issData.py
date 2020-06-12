from skyfield.api import Topos, load
#from . import removeFile

ts = load.timescale()


def getData():
    #removeFile.remFile("stations")
    satellites = load.tle_file('https://www.celestrak.com/NORAD/elements/stations.txt')
    sat = satellites[0]
    print('Loaded', sat)
    t = ts.now()
    geocentric = sat.at(t)
    subpoint = geocentric.subpoint()
    return ({'name':str(sat.name),'number':str(sat.model.satnum),'Latitude': str(subpoint.latitude.degrees),
        'Longitude': str(subpoint.longitude.degrees),
        'altitude': str(round(subpoint.elevation.m)),
        'Inclination-rad':str(sat.model.inclo),
        'position-GCRS':str(geocentric.position.km)
    })
    # print('Latitude:', subpoint.latitude)
    # print('Longitude:', subpoint.longitude)
    # print('Elevation (m):', int(subpoint.elevation.m))