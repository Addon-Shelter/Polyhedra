

import Part
import math

from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import Qt


translated = Qt.QT_TRANSLATE_NOOP


class Icosahedron:

    radiusvalue = 0

    def __init__(self, obj, radius=5):
        obj.addProperty(
            "App::PropertyLength",
            "Radius",
            "Icosahedron",
            translated("App::Property", "Radius of the icosahedron"),
        ).Radius = radius
        obj.addProperty(
            "App::PropertyLength",
            "Side",
            "Icosahedron",
            translated("App::Property", "Sidelength of the icosahedron"),
        )
        obj.Proxy = self


    def execute (self,obj):

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = 4*radius / math.sqrt(10 + 2 * math.sqrt(5))
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side * math.sqrt(10 + 2 * math.sqrt(5)) / 4)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue


        z = 4*radius / math.sqrt(10 + 2 * math.sqrt(5))
        anglefaces = 138.189685104
        r = z/12 * math.sqrt(3) * (3 + math.sqrt(5))


        #radius of a pentagram with the same side
        radius2 = z / math.sin(36 * math.pi/180)/2
        #height of radius2 in the sphere

        angle = math.acos(radius2/radius)
        height = radius * math.sin(angle)

        faces = []

        vertex_bottom = (0,0,-radius)
        vertexes_low = polygon_Vertexes(5,radius2, -height)
        vertexes_high = polygon_Vertexes(5,radius2, height, math.pi/5)
        vertex_top = (0,0,radius)


        for i in range(5):
            vertexes_side=[vertex_bottom,vertexes_low[i],vertexes_low[i+1], vertex_bottom]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            vertexes_side=[vertexes_low[i],vertexes_low[i+1],vertexes_high[i],vertexes_low[i] ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))
            vertexes_side=[vertexes_high[i],vertexes_high[i+1],vertexes_low[i+1],vertexes_high[i] ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            vertexes_side=[vertex_top,vertexes_high[i],vertexes_high[i+1],vertex_top ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid
