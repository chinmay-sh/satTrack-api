from app import app
#from .models.Satellite import Satellite
from .service import satellitesData
from flask import jsonify

@app.route('/satdata/top100/json')
def top100json():
    return jsonify({'data':satellitesData.satList})

@app.route('/satdata/top100/table')
def top100table():
    data = ''
    total = len(satellitesData.satList)
    for sat in satellitesData.satList:
        data += '''<tr>
                        <td> ''' + str(sat['name']) + '''</td>
                        <td> ''' + str(sat['catalog_number']) + '''</td>
                        <td> ''' + str(sat['classification']) + '''</td>
                        <td> ''' + str(sat['launch_year']) + '''</td>
                        <td> ''' + str(sat['launch_number_of_the_year']) + '''</td>
                        <td> ''' + str(sat['inclination(deg)']) + ''' </td>
                        <td> ''' + str(sat['argument_perigee']) + ''' </td>
                        <td> ''' + str(sat['daily_revolutions']) + ''' </td>
                        <td> ''' + str(sat['total_revs_till_epoch']) + ''' </td>
                    </tr>'''

    return '''
        <html>
            <head>
                <title>Home Page - SatTrack</title>
                <style>
                    table, td, th {
                        border: 1px solid black
                    }
                </style>
            </head>
            <body>
                <h1>Satellite Data</h1>
                <h2>Total sats: ''' + str(total) + '''
                <table style="width:100%"> 
                    <tr>
                        <th>Name</th>
                        <th>Catalog Number</th>
                        <th>Classification</th>
                        <th>Launch Year</th>
                        <th>Launch Num of the Year</th>
                        <th>Inclination (deg)</th>
                        <th>Argument of Perigee (deg)</th>
                        <th>Revolutions /day</th>
                        <th>Total Revs till Epoch</th>
                    </tr>
                ''' + data + ''' </table>
            </body>
        </html>'''