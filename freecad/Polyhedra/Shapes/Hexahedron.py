

import FreeCADGui
import FreeCAD
import Part
import math
import os

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Vertexes import horizontal_regular_polygon_vertexes
from ..Utils.Files import icons_dir


QT_TRANSLATE_NOOP = FreeCAD.Qt.QT_TRANSLATE_NOOP


class Hexahedron:

    radiusvalue = 0

    def __init__(self, obj, radius=5):
        obj.addProperty(
            "App::PropertyLength",
            "Radius",
            "Hexahedron",
            QT_TRANSLATE_NOOP("App::Property", "Radius of the hexahedron"),
        ).Radius = radius
        obj.addProperty(
            "App::PropertyLength",
            "Side",
            "Hexahedron",
            QT_TRANSLATE_NOOP("App::Property", "Sidelength of the hexahedron"),
        )
        obj.Proxy = self

    def execute(self, obj):

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            side = radius * 2 / math.sqrt(3)
            obj.Side = side
            self.radiusvalue = radius
        else:
            self.radiusvalue = obj.Side / 2 * math.sqrt(3)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue
            side = obj.Side

        faces = []
        vertexes_bottom = horizontal_regular_polygon_vertexes(4,math.sqrt(side ** 2 / 2),- side/2, math.pi/4)
        vertexes_top    = horizontal_regular_polygon_vertexes(4,math.sqrt(side ** 2 / 2), side/2, math.pi/4)

        for i in range(4):
            vertexes_side=[vertexes_bottom[i],vertexes_bottom[i+1],vertexes_top[i+1],vertexes_top[i],vertexes_bottom[i]]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        polygon_bottom=Part.makePolygon(vertexes_bottom)
        faces.append(Part.Face(polygon_bottom))

        polygon_top=Part.makePolygon(vertexes_top)
        faces.append(Part.Face(polygon_top))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid


class HexahedronCommand:

    def GetResources(self):
        return {
            "Pixmap": os.path.join(icons_dir, "hexahedron.svg"),
            "Accel": "Shift+H",
            "MenuText": QT_TRANSLATE_NOOP("Hexahedron", "Hexahedron"),
            "ToolTip": QT_TRANSLATE_NOOP("Hexahedron", "Generate a Hexahedron"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Hexahedron")
        Hexahedron(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Hexahedron")
        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        return

    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

