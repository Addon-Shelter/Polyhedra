

import FreeCAD
import Part
import math

from ..Utils.Vertexes import pyramid_Vertexes

from FreeCAD import Qt


translated = Qt.QT_TRANSLATE_NOOP


class Pyramid:

    sidescountvalue = 0
    radius1value = 0
    radius2value = 0
    side1value = 0
    side2value = 0
    anglez = 0

    def __init__ (
        self ,
        obj ,
        sidescount = 5 ,
        radius_bottom = 2 ,
        radius_top = 4 ,
        height = 10 ,
        angz = 0
    ):

        obj.addProperty(
            "App::PropertyLength",
            "Radius1",
            "Pyramid",
            translated("App::Property", "Radius of the pyramid"),
        ).Radius1 = radius_bottom

        obj.addProperty(
            "App::PropertyLength",
            "Radius2",
            "Pyramid",
            translated("App::Property", "Radius of the pyramid"),
        ).Radius2 = radius_top

        obj.addProperty(
            "App::PropertyLength",
            "Height",
            "Pyramid",
            translated("App::Property", "Height of the pyramid"),
        ).Height = height

        obj.addProperty(
            "App::PropertyInteger",
            "Sidescount",
            "Pyramid",
            translated("App::Property", "Sidescount of the pyramid"),
        ).Sidescount = sidescount

        obj.addProperty(
            "App::PropertyLength",
            "Sidelength1",
            "Pyramid",
            translated("App::Property", "Sidelength1 of the pyramid"),
        )

        obj.addProperty(
            "App::PropertyLength",
            "Sidelength2",
            "Pyramid",
            translated("App::Property", "Sidelength2 of the pyramid"),
        )

        obj.addProperty(
            "App::PropertyAngle",
            "Z_rotation",
            "Pyramid",
            translated("App::Property", "alfa angle around Z"),
        ).Z_rotation = angz

        obj.Proxy = self


    def execute ( self , object ):

        sidescount = int(object.Sidescount)
        angle = 2 * math.pi / sidescount
        radius_bottom = float(object.Radius1)
        radius_top = float(object.Radius2)
        sidelength_top = float(object.Sidelength2)
        sidelength_bottom = float(object.Sidelength1)
        height = float(object.Height)
        anglez = float(object.Z_rotation)

        if radius_bottom != self.radius1value or sidescount != self.sidescountvalue:
            object.Sidelength1 = radius_bottom * math.sin(angle/2) * 2
            self.radius1value = radius_bottom
            self.side1value = float(object.Sidelength1)
        elif sidelength_bottom != self.side1value:
            self.radius1value = float(object.Sidelength1 / 2) / math.sin(angle/2)
            object.Radius1 = self.radius1value
            radius_bottom = self.radius1value
            self.side1value = float(object.Sidelength1)

        if radius_top != self.radius2value or sidescount != self.sidescountvalue:
            object.Sidelength2 = radius_top * math.sin(angle/2) * 2
            self.radius2value = float(radius_top)
            self.side2value = float(object.Sidelength2)
        elif sidelength_top != self.side2value:
            self.radius2value = float(object.Sidelength2 / 2) / math.sin(angle/2)
            object.Radius2 = self.radius2value
            radius_top = self.radius2value
            self.side2value = float(object.Sidelength2)

        self.sidescountvalue = sidescount

        faces = []

        if radius_bottom == 0 and radius_top == 0:
            FreeCAD.Console.PrintMessage("Both radiuses are zero" + "\n")
            return

        vertexes_bottom = pyramid_Vertexes(sidescount,radius_bottom,0,anglez)
        vertexes_top    = pyramid_Vertexes(sidescount,radius_top,height,anglez)

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

                vertexes_side = [
                    vertexes_bottom[ i ] ,
                    vertexes_bottom[ i + 1 ] ,
                    vertexes_top[ 0 ] ,
                    vertexes_bottom[ i ]
                ]

            elif radius_bottom == 0:

                vertexes_side = [
                    vertexes_bottom[ 0 ] ,
                    vertexes_top[ i + 1 ] ,
                    vertexes_top[ i ] ,
                    vertexes_bottom[ 0 ]
                ]

            else:

                vertexes_side = [
                    vertexes_bottom[ i ] ,
                    vertexes_bottom[ i + 1 ] ,
                    vertexes_top[ i + 1 ] ,
                    vertexes_top[ i ] ,
                    vertexes_bottom[ i ]
                ]

            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)

        object.Shape = solid

