

from ..Utils.Vertexes import pyramid_Vertexes

from FreeCAD import DocumentObject , Console , Part , Qt
from typing import Any
from math import sin , pi


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class PyramidPart ( DocumentObject ):

    Sidelength1 : float
    Sidelength2 : float
    Z_rotation : float
    Sidescount : int
    Radius1 : float
    Radius2 : float
    Height : float

    Shape : Any


class Pyramid :

    sidescountvalue = 0
    radius1value = 0
    radius2value = 0
    side1value = 0
    side2value = 0
    anglez = 0

    def __init__ (
        self ,
        object : PyramidPart ,
        side_count : int = 5 ,
        radius_bottom : float = 2 ,
        radius_top : float = 4 ,
        height : float = 10 ,
        angle_z : float  = 0
    ):

        def property (
            description : str ,
            type : str ,
            name : str
        ):
            object.addProperty(
                f'App::Property{ type }',
                name , 'Pyramid' ,
                description
            )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of the pyramid') ,
            name = 'Radius1' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of the pyramid') ,
            name = 'Radius2' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Height of the pyramid') ,
            name = 'Height' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Sidescount of the pyramid') ,
            name = 'Sidescount' ,
            type = 'Integer'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Sidelength1 of the pyramid') ,
            name = 'Sidelength1' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Sidelength2 of the pyramid') ,
            name = 'Sidelength2' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','alfa angle around Z') ,
            name = 'Z_rotation' ,
            type = 'Angle'
        )

        object.Sidescount = side_count
        object.Z_rotation = angle_z
        object.Radius2 = radius_top
        object.Radius1 = radius_bottom
        object.Height = height
        object.Proxy = self


    def execute ( self , object : PyramidPart ):

        sidescount = object.Sidescount
        angle = 2 * pi / sidescount

        sidelength_bottom = float(object.Sidelength1)
        sidelength_top = float(object.Sidelength2)
        radius_bottom = float(object.Radius1)
        radius_top = float(object.Radius2)
        anglez = float(object.Z_rotation)
        height = float(object.Height)

        if radius_bottom != self.radius1value or sidescount != self.sidescountvalue:

            object.Sidelength1 = radius_bottom * sin( angle / 2 ) * 2
            self.radius1value = radius_bottom
            self.side1value = object.Sidelength1

        elif sidelength_bottom != self.side1value:

            self.radius1value = ( object.Sidelength1 / 2 ) / sin( angle / 2 )
            object.Radius1 = self.radius1value

            radius_bottom = self.radius1value

            self.side1value = object.Sidelength1

        if radius_top != self.radius2value or sidescount != self.sidescountvalue:

            object.Sidelength2 = radius_top * sin( angle / 2 ) * 2
            self.radius2value = radius_top
            self.side2value = object.Sidelength2

        elif sidelength_top != self.side2value:

            self.radius2value = ( object.Sidelength2 / 2 ) / sin( angle / 2 )
            object.Radius2 = self.radius2value

            radius_top = self.radius2value

            self.side2value = object.Sidelength2

        self.sidescountvalue = sidescount

        faces = []

        if radius_bottom == 0 and radius_top == 0:
            Console.PrintMessage('Both radiuses are zero' + '\n')
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

        for i in range( sidescount ):

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

            polygon_side = Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)

        object.Shape = solid

