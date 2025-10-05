

import Part
import math

from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import Qt


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class Icosahedron_Truncated:

    __module__ = 'Virtual.Polyhedra.Parts'
    __name__ = 'Icosahedron_Truncated'

    radiusvalue = 0

    def __init__(self, obj, radius=5):
        obj.addProperty(
            "App::PropertyLength",
            "Radius",
            "Icosahedron_truncated",
            QT_TRANSLATE_NOOP("App::Property", "Radius"),
        ).Radius = radius
        obj.addProperty(
            "App::PropertyLength",
            "Side",
            "Icosahedron_truncated",
            QT_TRANSLATE_NOOP("App::Property", "Sidelength"),
        )
        obj.Proxy = self

    def execute (self,obj):

        radius = float(obj.Radius) * 1.144  # correction for Icosohedron --> truncated
        if (radius != self.radiusvalue):
            obj.Side = 4*radius / math.sqrt(10 + 2 * math.sqrt(5)) / 3
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side * math.sqrt(10 + 2 * math.sqrt(5)) / 4) * 3
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue


        z =  float(4*radius)  / math.sqrt(10 + 2 * math.sqrt(5)) # z of base icosahedron
        anglefaces = 138.189685104
        r = z/12 * math.sqrt(3) * (3 + math.sqrt(5))

        #radius of a pentagram with the same side
        radius2 = z / math.sin(36 * math.pi/180)/2

        #height of radius2 in the sphere
        angle = math.acos(radius2/radius)
        height = radius * math.sin(angle)

        faces = []

        vertex_bottom = (0,0,-radius)
        vertexes_low =  polygon_Vertexes(5,radius2 , -height)
        vertexes_high = polygon_Vertexes(5,radius2 , height ,  -math.pi/5)
        vertex_top = (0,0,radius)

        vertexes_bottom = []
        vertexes_top = []

        for i in range(6):
            new_vertex = ((vertex_bottom[0]+vertexes_low[i][0])/3 , (vertex_bottom[1]+vertexes_low[i][1])/3 , vertex_bottom[2]-(vertex_bottom[2]-vertexes_low[i][2])/3)
            vertexes_bottom.append(new_vertex)
        polygon_side=Part.makePolygon(vertexes_bottom)
        faces.append(Part.Face(polygon_side))

        for i in range(6):
            new_vertex = ((vertex_top[0]+vertexes_high[i][0])/3 , (vertex_top[1]+vertexes_high[i][1])/3 , vertex_top[2]-(vertex_top[2]-vertexes_high[i][2])/3)
            vertexes_top.append(new_vertex)
        polygon_side=Part.makePolygon(vertexes_top)
        faces.append(Part.Face(polygon_side))

        pg6_bottom = []
        for i in range(5):
            vertex1=vertexes_bottom[i]
            vertex2=vertexes_bottom[i+1]
            vertex3=(vertexes_bottom[i+1][0] + (vertexes_low[i+1][0] - vertexes_bottom[i+1][0])/2, vertexes_bottom[i+1][1] + (vertexes_low[i+1][1] - vertexes_bottom[i+1][1])/2, (vertexes_low[i+1][2] + vertexes_bottom[i+1][2])/2)
            vertex4=((vertexes_low[i+1][0]*2 +vertexes_low[i][0])/3, (vertexes_low[i+1][1]*2 +vertexes_low[i][1])/3, -height)
            vertex5=((vertexes_low[i+1][0]+vertexes_low[i][0]*2)/3, (vertexes_low[i+1][1] +vertexes_low[i][1]*2)/3, -height)
            vertex6=(vertexes_bottom[i][0] + (vertexes_low[i][0] - vertexes_bottom[i][0])/2, vertexes_bottom[i][1] + (vertexes_low[i][1] - vertexes_bottom[i][1])/2, (vertexes_low[i][2] + vertexes_bottom[i][2])/2)
            vertexes = [vertex1,vertex2,vertex3,vertex4,vertex5,vertex6,vertex1]
            pg6_bottom.append(vertexes)
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        pg6_top = []
        for i in range(5):
            vertex1=vertexes_top[i]
            vertex2=vertexes_top[i+1]
            vertex3=(vertexes_top[i+1][0] + (vertexes_high[i+1][0] - vertexes_top[i+1][0])/2, vertexes_top[i+1][1] + (vertexes_high[i+1][1] - vertexes_top[i+1][1])/2, (vertexes_high[i+1][2] + vertexes_top[i+1][2])/2)
            vertex4=((vertexes_high[i+1][0]*2 +vertexes_high[i][0])/3, (vertexes_high[i+1][1]*2 +vertexes_high[i][1])/3, height)
            vertex5=((vertexes_high[i+1][0]+vertexes_high[i][0]*2)/3, (vertexes_high[i+1][1] +vertexes_high[i][1]*2)/3, height)
            vertex6=(vertexes_top[i][0] + (vertexes_high[i][0] - vertexes_top[i][0])/2, vertexes_top[i][1] + (vertexes_high[i][1] - vertexes_top[i][1])/2, (vertexes_high[i][2] + vertexes_top[i][2])/2)
            vertexes = [vertex1,vertex2,vertex3,vertex4, vertex5,vertex6,vertex1]
            pg6_top.append(vertexes)
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        pg6_low = []
        for i in range(5):
            vertex1 = pg6_bottom[i][3]
            vertex2 = pg6_bottom[i][4]
            vertex3 = ((vertexes_low[i][0]*2 + vertexes_high[i+1][0])/3,(vertexes_low[i][1]*2 + vertexes_high[i+1][1])/3, (vertexes_low[i][2]*2 + vertexes_high[i+1][2])/3)
            vertex4 = ((vertexes_low[i][0] + vertexes_high[i+1][0]*2)/3,(vertexes_low[i][1] + vertexes_high[i+1][1]*2)/3, (vertexes_low[i][2] + vertexes_high[i+1][2]*2)/3)
            vertex5 = ((vertexes_low[i+1][0] + vertexes_high[i+1][0]*2)/3,(vertexes_low[i+1][1] + vertexes_high[i+1][1]*2)/3, (vertexes_low[i+1][2] + vertexes_high[i+1][2]*2)/3)
            vertex6 = ((vertexes_low[i+1][0]*2 + vertexes_high[i+1][0])/3,(vertexes_low[i+1][1]*2 + vertexes_high[i+1][1])/3, (vertexes_low[i+1][2]*2 + vertexes_high[i+1][2])/3)
            vertexes = [vertex1,vertex2,vertex3,vertex4, vertex5,vertex6,vertex1]
            pg6_low.append(vertexes)
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        pg6_high = []
        for i in range(5):
            vertex1 = pg6_top[i][3]
            vertex2 = pg6_top[i][4]
            vertex3 = pg6_low[i-1][4]
            vertex4 = pg6_low[i-1][5]
            vertex5 = pg6_low[i][2]
            vertex6 = pg6_low[i][3]
            vertexes = [vertex1,vertex2, vertex3, vertex4,vertex5,vertex6 ,vertex1]
            pg6_high.append(vertexes)
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            vertex1 = pg6_top[i][4]
            vertex2 = pg6_top[i][5]
            vertex3 = pg6_high[i-1][6]
            vertex4 = pg6_high[i-1][5]
            vertex5 = pg6_low[i-1][4]
            vertexes = [vertex1,vertex2, vertex3,vertex4,vertex5,vertex1]
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            vertex1 = pg6_bottom[i][4]
            vertex2 = pg6_bottom[i][5]
            vertex3 = pg6_low[i-1][6]
            vertex4 = pg6_low[i-1][5]
            vertex5 = pg6_high[i][4]
            vertexes = [vertex1,vertex2, vertex3,vertex4,vertex5, vertex1]
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))


        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid

