from skyfield.api import load
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import requests


ts = load.timescale()


satellites = load.tle_file('https://www.celestrak.com/NORAD/elements/stations.txt')
sat = satellites[0]
print('Loaded', sat)

def getData():
    t = ts.now()
    geocentric = sat.at(t)
    subpoint = geocentric.subpoint()
    iss = ({'name':str(sat.name),'number':str(sat.model.satnum),'Latitude': str(subpoint.latitude),
        'Longitude': str(subpoint.longitude),
        'Elevation-m': str(round(subpoint.elevation.m)),
        'Inclination-rad':str(sat.model.inclo)
    })
    # print('Latitude:', subpoint.latitude)
    # print('Longitude:', subpoint.longitude)
    # print('Elevation (m):', int(subpoint.elevation.m))

    return iss


def getMap():

    time_url = 'http://worldtimeapi.org/api/timezone/Etc/UTC'
    req = requests.get(time_url)
    time_data = req.json()
    year = int(time_data['utc_datetime'][:4])
    month = int(time_data['utc_datetime'][5:7])
    date = int(time_data['utc_datetime'][8:10])
    hour = int(time_data['utc_datetime'][11:13])
    print(year,month,date,hour)

    minutes = np.arange(0, 200, 0.1) # about two orbits
    times   = ts.utc(year,month, date, hour, minutes)
    times1 = times[:1000]
    times2 = times[1000:]

    # print(np.where(times == ts.now()))
    # print(times1)
    # print(times2)

    plt.ion()
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    ax.stock_img()
    while True:
        # current orbit
        geocentric = sat.at(times1)
        subsat = geocentric.subpoint()
        plt.scatter(subsat.longitude.degrees, subsat.latitude.degrees, transform=ccrs.PlateCarree(),
                    color='red')

        # next orbit (+90 mins)
        geocentric = sat.at(times2)
        subsat = geocentric.subpoint()
        plt.scatter(subsat.longitude.degrees, subsat.latitude.degrees, transform=ccrs.PlateCarree(),
                    color='green')

        # current location of ISS
        t = ts.now()
        geocentric = sat.at(t)
        subsat = geocentric.subpoint()
        sc = plt.scatter(subsat.longitude.degrees, subsat.latitude.degrees, transform=ccrs.PlateCarree(),
                    color='yellow',s=300)

        plt.draw()
        plt.pause(4)
        sc.remove()


