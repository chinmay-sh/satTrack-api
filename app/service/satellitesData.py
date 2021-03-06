from skyfield.api import Topos, load
#from . import removeFile

ts = load.timescale()

satList = []

def getData(sat_url):
    #removeFile.remCall()
    satellites = load.tle_file(sat_url)
    print('Loaded', len(satellites), 'satellites')
    t = ts.now()
    for sat in satellites:
        geocentric = sat.at(t)
        subpoint = geocentric.subpoint()
        satList.append({'name':str(sat.name),'number':str(sat.model.satnum),'Latitude': str(subpoint.latitude.degrees),
            'Longitude': str(subpoint.longitude.degrees),
            'altitude': str(round(subpoint.elevation.m)),
            'Inclination-rad':str(sat.model.inclo),
            'position-GCRS':str(geocentric.position.km)
        })
        # print('Latitude:', subpoint.latitude)
        # print('Longitude:', subpoint.longitude)
        # print('Elevation (m):', int(subpoint.elevation.m))