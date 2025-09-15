
from math import cos , sin , pi


def horizontal_regular_polygon_vertexes(sidescount,radius,z, startangle = 0):
    vertexes = []
    if radius != 0 :
        for i in range(0,sidescount+1):
            angle = 2 * pi * i / sidescount + pi + startangle
            vertex = (radius * cos(angle), radius * sin(angle), z)
            vertexes.append(vertex)
    else:
        vertex = (0,0,z)
        vertexes.append(vertex)
    return vertexes



def horizontal_regular_pyramid_vertexes(sidescount,radius,z, anglez = 0): # anglez in degrees
    vertexes = []
    odd = 0
    if (sidescount % 2) == 0:
        odd = 1
    if radius != 0 :
        for i in range(0,sidescount+1):
            angle = 2 * pi * i / sidescount + (pi * (odd/sidescount + 1/2)) + anglez * pi / 180
            vertex = (radius * cos(angle), radius * sin(angle), z)
            vertexes.append(vertex)
    else:
        vertex = (0,0,z)
        vertexes.append(vertex)
    return vertexes
