from ..models.Satellite import Satellite

sat = Satellite('x',5,8,4,8,4,2,5,2)
sat2 = Satellite('y',5,8,4,8,4,2,5,2)
sat3 = Satellite('z',5,8,4,8,4,2,5,2)

saTlist = []
saTlist.append(sat.getSatDataText())
saTlist.append(sat2.getSatDataText())
saTlist.append(sat3.getSatDataText())