from ..models.Satellite import Satellite

sat = Satellite('x',5,8,4,8,4,2,5,2)
sat2 = Satellite('y',6,8,4,8,4,2,5,2)
sat3 = Satellite('z',7,8,4,8,4,2,5,2)

satList = []
satList.append(sat.getSatData())
satList.append(sat2.getSatData())
satList.append(sat3.getSatData())