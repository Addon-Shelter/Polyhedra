

import FreeCADGui
import FreeCAD
import Part
import math
import os

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Utils.Vertexes import horizontal_regular_pyramid_vertexes

from FreeCADGui import Command


QT_TRANSLATE_NOOP = FreeCAD.Qt.QT_TRANSLATE_NOOP


class Pyramid:

    radius1value = 0
    radius2value = 0
    sidescountvalue = 0
    side1value = 0
    side2value = 0
    anglez = 0

    def __init__(self, obj, sidescount=5, radius_bottom=2, radius_top=4, height=10, angz=0):
        obj.addProperty(
            "App::PropertyLength",
            "Radius1",
            "Pyramid",
            QT_TRANSLATE_NOOP("App::Property", "Radius of the pyramid"),
        ).Radius1 = radius_bottom
        obj.addProperty(
            "App::PropertyLength",
            "Radius2",
            "Pyramid",
            QT_TRANSLATE_NOOP("App::Property", "Radius of the pyramid"),
        ).Radius2 = radius_top
        obj.addProperty(
            "App::PropertyLength",
            "Height",
            "Pyramid",
            QT_TRANSLATE_NOOP("App::Property", "Height of the pyramid"),
        ).Height = height
        obj.addProperty(
            "App::PropertyInteger",
            "Sidescount",
            "Pyramid",
            QT_TRANSLATE_NOOP("App::Property", "Sidescount of the pyramid"),
        ).Sidescount = sidescount
        obj.addProperty(
            "App::PropertyLength",
            "Sidelength1",
            "Pyramid",
            QT_TRANSLATE_NOOP("App::Property", "Sidelength1 of the pyramid"),
        )
        obj.addProperty(
            "App::PropertyLength",
            "Sidelength2",
            "Pyramid",
            QT_TRANSLATE_NOOP("App::Property", "Sidelength2 of the pyramid"),
        )
        obj.addProperty(
            "App::PropertyAngle",
            "Z_rotation",
            "Pyramid",
            QT_TRANSLATE_NOOP("App::Property", "alfa angle around Z"),
        ).Z_rotation = angz

        obj.Proxy = self


    def execute (self,obj):

        sidescount = int(obj.Sidescount)
        angle = 2 * math.pi / sidescount
        radius_bottom = float(obj.Radius1)
        radius_top = float(obj.Radius2)
        sidelength_top = float(obj.Sidelength2)
        sidelength_bottom = float(obj.Sidelength1)
        height = float(obj.Height)
        anglez = float(obj.Z_rotation)

        if radius_bottom != self.radius1value or sidescount != self.sidescountvalue:
            obj.Sidelength1 = radius_bottom * math.sin(angle/2) * 2
            self.radius1value = radius_bottom
            self.side1value = float(obj.Sidelength1)
        elif sidelength_bottom != self.side1value:
            self.radius1value = float(obj.Sidelength1 / 2) / math.sin(angle/2)
            obj.Radius1 = self.radius1value
            radius_bottom = self.radius1value
            self.side1value = float(obj.Sidelength1)

        if radius_top != self.radius2value or sidescount != self.sidescountvalue:
            obj.Sidelength2 = radius_top * math.sin(angle/2) * 2
            self.radius2value = float(radius_top)
            self.side2value = float(obj.Sidelength2)
        elif sidelength_top != self.side2value:
            self.radius2value = float(obj.Sidelength2 / 2) / math.sin(angle/2)
            obj.Radius2 = self.radius2value
            radius_top = self.radius2value
            self.side2value = float(obj.Sidelength2)

        self.sidescountvalue = sidescount
        faces = []
        if radius_bottom == 0 and radius_top == 0:
            FreeCAD.Console.PrintMessage("Both radiuses are zero" + "\n")
        else:
            vertexes_bottom = horizontal_regular_pyramid_vertexes(sidescount,radius_bottom,0     ,anglez)
            vertexes_top    = horizontal_regular_pyramid_vertexes(sidescount,radius_top   ,height,anglez)

            if radius_bottom != 0:
                polygon_bottom = Part.makePolygon(vertexes_bottom)
                face_bottom = Part.Face(polygon_bottom)
                faces.append(face_bottom)
            if radius_top != 0:
                polygon_top = Part.makePolygon(vertexes_top)
                face_top = Part.Face(polygon_top)
                faces.append(face_top)

            for i in range(sidescount):
                if radius_top == 0:
                    vertexes_side=[vertexes_bottom[i],vertexes_bottom[i+1],vertexes_top[0],vertexes_bottom[i]]
                elif radius_bottom == 0:
                    vertexes_side=[vertexes_bottom[0],vertexes_top[i+1],vertexes_top[i],vertexes_bottom[0]]
                else:
                    vertexes_side=[vertexes_bottom[i],vertexes_bottom[i+1],vertexes_top[i+1],vertexes_top[i],vertexes_bottom[i]]
                polygon_side=Part.makePolygon(vertexes_side)
                faces.append(Part.Face(polygon_side))

            shell = Part.makeShell(faces)
            solid = Part.makeSolid(shell)
            obj.Shape = solid

class PyramidCommand ():

    def GetResources ( self ):
        return {
            'Pixmap' : icon('Shapes/Pyramid') ,
            "Accel": "Shift+P",
            "MenuText": QT_TRANSLATE_NOOP("Pyramid", "Pyramid"),
            "ToolTip": QT_TRANSLATE_NOOP("Pyramid", "Generate a Pyramid with any number of sides"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Pyramid")   # see https://www.freecadweb.org/wiki/Creating_a_FeaturePython_Box,_Part_II
        Pyramid(obj)
        ViewProviderBox(obj.ViewObject, "Pyramid")
        #obj.ViewObject.Proxy=0
        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        return


    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

