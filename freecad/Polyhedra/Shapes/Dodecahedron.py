
import Part
import math

from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import Qt


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class Dodecahedron:

    radiusvalue = 0

    def __init__(self, obj, radius=5):
        obj.addProperty(
            "App::PropertyLength",
            "Radius",
            "Dodecahedron",
            QT_TRANSLATE_NOOP("App::Property", "Radius of the dodecahedron"),
        ).Radius = radius
        obj.addProperty(
            "App::PropertyLength",
            "Side",
            "Dodecahedron",
            QT_TRANSLATE_NOOP("App::Property", "Sidelength of the dodecahedron"),
        )
        obj.Proxy = self


    def execute (self,obj):

        angleribs = 121.717474411
        anglefaces = 116.565051177

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = 4 * radius /  (math.sqrt(3) * ( 1 + math.sqrt(5)))
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side * (math.sqrt(3) * ( 1 + math.sqrt(5))) / 4)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue

        faces = []
        z = 4 * radius /  (math.sqrt(3) * ( 1 + math.sqrt(5)))
        r = z/2 * math.sqrt((25 + (11 * math.sqrt(5)))/10)
        # int sphere r is height / 2

        h2 = z * math.sin(angleribs/180 * math.pi)

        #height of the side-tips
        radius1 = z / 2 / math.sin(36 * math.pi / 180)
        h5h = (radius1 + radius1 * math.cos(36 * math.pi / 180))   * math.sin(anglefaces * math.pi / 180) #height of the tops

        radius2 = radius1 - z * math.cos(angleribs * math.pi / 180 )

        r=(h2 + h5h)/2  # XXX to make it fit!




        vertexes_bottom = polygon_Vertexes(5,radius1,-r)
        vertexes_low = polygon_Vertexes(5,radius2, -r + h2)
        vertexes_high = polygon_Vertexes(5,radius2, -r + h5h,  math.pi/5)
        vertexes_top = polygon_Vertexes(5,radius1, r, math.pi/5)

        polygon_bottom = Part.makePolygon(vertexes_bottom)
        face_bottom = Part.Face(polygon_bottom)
        faces.append(face_bottom)

        polygon_top = Part.makePolygon(vertexes_top)
        face_top = Part.Face(polygon_top)
        faces.append(face_top)

        for i in range(5):
            vertexes_side=[vertexes_bottom[i],vertexes_bottom[i+1],vertexes_low[i+1],vertexes_high[i],vertexes_low[i], vertexes_bottom[i] ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            #vertexes_side=[vertexes_top[i],vertexes_top[i+1],vertexes_high[i+1],vertexes_high2[i], vertexes_high[i],vertexes_top[i] ]
            vertexes_side=[vertexes_top[i],vertexes_top[i+1],vertexes_high[i+1],vertexes_low[i+1],vertexes_high[i],vertexes_top[i] ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid
