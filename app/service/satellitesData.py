from ..models.Satellite import Satellite
import urllib.request


satList = []

resp_topView = urllib.request.urlopen('https://www.celestrak.com/NORAD/elements/visual.txt')
#print(x.read())
resp_topView = str(resp_topView.read())
resp_topView = resp_topView.split('\\r\\n')

# response cleaning
resp_topView = resp_topView[:-1]
resp_topView[0] = resp_topView[0][2:]

count = 0
for sat in range(int(len(resp_topView)/3)):
    #line 1
    name = resp_topView[count]
    count += 1
    #line 2
    classification = resp_topView[count][7]
    launchYear = resp_topView[count][9:11]
    yearlylaunchNum = resp_topView[count][11:14]
    count += 1
    #line 3
    catNum = resp_topView[count][2:7]
    inclination = resp_topView[count][8:16]
    periArg = resp_topView[count][34:42]
    revsPerDay = resp_topView[count][52:63]
    revsTillEpoch = resp_topView[count][63:68]
    count += 1

    sat = Satellite(name,catNum,classification,launchYear,yearlylaunchNum,inclination,periArg,revsPerDay,revsTillEpoch)
    satList.append(sat.getSatData())


#sat = Satellite('x',5,8,4,8,4,2,5,2)
#sat2 = Satellite('y',6,8,4,8,4,2,5,2)
#sat3 = Satellite('z',7,8,4,8,4,2,5,2)


#satList.append(sat.getSatData())
#satList.append(sat2.getSatData())
#satList.append(sat3.getSatData())