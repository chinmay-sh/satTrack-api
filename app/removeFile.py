import os
from skyfield.api import load

ts = load.timescale()

todayNum = ts.now().utc_datetime().strftime("%j")
prevDayNum = ts.utc(2020,6,7).utc_datetime().strftime("%j")

def remFile(fileName):
    if os.path.exists("./" + fileName):
        os.remove("./" + fileName)
        print([ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ])
        print('Files removed')
    else:
        print("The file does not exist") 


def dateChange():
    global prevDayNum
    if(todayNum > prevDayNum):
        print('Dates Changed')
        prevDayNum = ts.now().utc_datetime().strftime("%j")
        return True
    else:
        print('No changes in dates')
        return False

def remCall():
    if(dateChange()):
        files = ["visual.txt","active.txt","starlink.txt","stations.txt",'deltat.data', 'deltat.data.download', 'deltat.preds', 'Leap_Second.dat']
        for i in files:
            remFile(i)
    else:
        print("Files already up-to-date")

