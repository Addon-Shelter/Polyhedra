

import FreeCAD
import Part
import math

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class Hexahedron:

    radiusvalue = 0

    def __init__(self, obj, radius=5):
        obj.addProperty(
            "App::PropertyLength",
            "Radius",
            "Hexahedron",
            translated("App::Property", "Radius of the hexahedron"),
        ).Radius = radius
        obj.addProperty(
            "App::PropertyLength",
            "Side",
            "Hexahedron",
            translated("App::Property", "Sidelength of the hexahedron"),
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
        vertexes_bottom = polygon_Vertexes(4,math.sqrt(side ** 2 / 2),- side/2, math.pi/4)
        vertexes_top    = polygon_Vertexes(4,math.sqrt(side ** 2 / 2), side/2, math.pi/4)

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
            "Pixmap": icon('Shapes/Hexahedron') ,
            "Accel": "Shift+H",
            "MenuText": translated("Hexahedron", "Hexahedron"),
            "ToolTip": translated("Hexahedron", "Generate a Hexahedron"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Hexahedron")
        Hexahedron(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Hexahedron")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        return

    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

