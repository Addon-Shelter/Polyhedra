

import Part
import math

from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import Qt


translated = Qt.QT_TRANSLATE_NOOP


class Octahedron:
    # Z = R * sqrt(2)
    radiusvalue = 0

    def __init__(self, obj, radius=5):
        obj.addProperty(
            "App::PropertyLength",
            "Radius",
            "Octahedron",
            translated("App::Property", "Radius of the octahedron"),
        ).Radius = radius
        obj.addProperty(
            "App::PropertyLength",
            "Side",
            "Octahedron",
            translated("App::Property", "Sidelength of the octahedron"),
        )
        obj.Proxy = self

    def execute (self,obj):

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = radius * math.sqrt(2)
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side / math.sqrt(2))
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue



        faces = []
        vertexes_middle = polygon_Vertexes(4,radius,0)
        vertexes_bottom = polygon_Vertexes(1,0,-radius)
        vertexes_top    = polygon_Vertexes(1,0,radius)

        for i in range(4):
            vertexes_side=[vertexes_middle[i],vertexes_middle[i+1],vertexes_top[0],vertexes_middle[i]]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        for i in range(4):
            vertexes_side=[vertexes_middle[i],vertexes_middle[i+1],vertexes_bottom[0],vertexes_middle[i]]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid

