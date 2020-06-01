import os
from skyfield.api import load

ts = load.timescale()

def remFile(fileName):
    if os.path.exists("./" + fileName):
        os.remove("./" + fileName)
        print([ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ])
        print('Files removed')
    else:
        print("The file does not exist") 

def dateChange():
    todayNum = ts.now().utc_datetime().strftime("%j")
    previousDayNum = ts.utc(2020,5,31).utc_datetime().strftime("%j")

    if(todayNum > previousDayNum):
        print('Dates Changed')
        return True
    else:
        print('No changes in dates')
        return False

def remCall():
    files = ["visual.txt","active.txt","starlink.txt","stations.txt",'deltat.data', 'deltat.data.download', 'deltat.preds', 'Leap_Second.dat']
    for i in files:
        remFile(i)

