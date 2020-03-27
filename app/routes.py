from app import app
#from .models.Satellite import Satellite
from .service import satellitesData
from flask import jsonify

@app.route('/satdata/top100/json')
def top100json():
    return jsonify({'data':satellitesData.saTlist})

@app.route('/satdata/top100/text')
def top100text():
    data = ''
    for sat in satellitesData.saTlist:
        data += str(sat)+'<br><br>'
        
    return '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Satellite Data</h1>
                <p> ''' + data + ''' </p>
            </body>
        </html>'''