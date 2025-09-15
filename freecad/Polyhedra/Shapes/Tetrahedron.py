

import FreeCADGui
import FreeCAD
import Part
import math
import os

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Vertexes import horizontal_regular_polygon_vertexes
from ..Utils.Files import icons_dir


QT_TRANSLATE_NOOP = FreeCAD.Qt.QT_TRANSLATE_NOOP


class Tetrahedron:
        # == basics ==
        #R = z / 4 * sqrt(6)
        #ro = z / 12 * sqrt(6)    -->   ro = R / 3
        #z = 4 * R / sqrt(6)
        #h = z / 3 * sqrt(6) = 4 * R / sqrt(6) /3 * sqrt(6) = 4 * R / 3  = ro + R
        #radius at level = z / 2 / cos(30) = (4 * R / sqrt(6)) / 2 / sqrt(3) * 2 = 4 * R / (sqrt(6) * sqrt(3))= 4 * R / (3 * sqrt(2)

    radiusvalue = 0
    def __init__(self, obj, radius=5):
        obj.addProperty(
            "App::PropertyLength",
            "Radius",
            "Tetrahedron",
            QT_TRANSLATE_NOOP("App::Property", "Radius of the tetrahedron"),
        ).Radius = radius
        obj.addProperty(
            "App::PropertyLength",
            "Side",
            "Tetrahedron",
            QT_TRANSLATE_NOOP("App::Property", "Sidelength of the tetrahedron"),
        )
        obj.Proxy = self


    def execute (self,obj):

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = radius * 4 / math.sqrt(6)
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side * math.sqrt(6) / 4)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue

        faces = []
        vertexes_bottom = horizontal_regular_polygon_vertexes(3,4*radius/3/math.sqrt(2),- radius / 3)
        vertexes_top    = horizontal_regular_polygon_vertexes(1,0,radius)

        for i in range(3):
            vertexes_side=[vertexes_bottom[i],vertexes_bottom[i+1],vertexes_top[0],vertexes_bottom[i]]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        polygon_bottom=Part.makePolygon(vertexes_bottom)

        faces.append(Part.Face(polygon_bottom))
        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid


class TetrahedronCommand:

    def GetResources(self):
        return {
            "Pixmap": os.path.join(icons_dir, "tetrahedron.svg"),
            "Accel": "Shift+T",
            "MenuText": QT_TRANSLATE_NOOP("Tetrahedron", "Tetrahedron"),
            "ToolTip": QT_TRANSLATE_NOOP("Tetrahedron", "Generate a Tetrahedron"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Tetrahedron")
        Tetrahedron(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Tetrahedron")
        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        return

    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True


