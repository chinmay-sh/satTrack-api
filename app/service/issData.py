from skyfield.api import Topos, load
import numpy as np

ts = load.timescale()

satellites = load.tle_file('https://www.celestrak.com/NORAD/elements/stations.txt')
sat = satellites[0]

def getLocationData():
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

def getOrbits():
    t_utc = ts.now().utc_datetime()
    minutes = np.arange(0, 200, 0.1) # about two orbits
    year = int(t_utc.strftime("%Y"))
    month = int(t_utc.strftime("%m"))
    date = int(t_utc.strftime("%d"))
    hour = int(t_utc.strftime("%H"))
    #print(year,month,date,hour,minutes)
    times = ts.utc(year,month,date,hour,minutes)
    # times1 = times[:1000]
    # times2 = times[1000:]

    # current orbit
    geocentric = sat.at(times)
    subsatLat = geocentric.subpoint().latitude.degrees
    subsatLong = geocentric.subpoint().longitude.degrees

    coordinateArr = []

    for i in range(len(subsatLat)):
        coordinateArr.append([subsatLong[i],subsatLat[i]])
    
    # print(coordinateArr)

    return ({'name':str(sat.name),'number':str(sat.model.satnum),
        'orbitalData': coordinateArr
    })

    # # next orbit (+90 mins)
    # geocentric = sat.at(times2)
    # subsat = geocentric.subpoint()
    # plt.scatter(subsat.longitude.degrees, subsat.latitude.degrees, transform=ccrs.PlateCarree(),
    #             color='green')

    # # current location of ISS
    # t = ts.now()
    # geocentric = sat.at(t)
    # subsat = geocentric.subpoint()
    # sc = plt.scatter(subsat.longitude.degrees, subsat.latitude.degrees, transform=ccrs.PlateCarree(),
    #             color='violet',s=300)
