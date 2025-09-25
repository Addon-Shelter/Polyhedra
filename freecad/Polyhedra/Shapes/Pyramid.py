
from ..Utils.Vertexes import pyramid_Vertexes

from FreeCAD import DocumentObject , Units , Console , Qt
from typing import Any
from Part import makePolygon , makeSolid , makeShell , Face
from math import sin , pi


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class PyramidPart ( DocumentObject ):

    Sidelength1 : Units.Quantity
    Sidelength2 : Units.Quantity
    Z_rotation : Units.Quantity
    Radius1 : Units.Quantity
    Radius2 : Units.Quantity
    Height : Units.Quantity

    Sidescount : int
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

        object.Z_rotation.Value = angle_z
        object.Radius2.Value = radius_top
        object.Radius1.Value = radius_bottom
        object.Height.Value = height

        object.Sidescount = side_count
        object.Proxy = self


    def execute ( self , object : PyramidPart ):

        sides = object.Sidescount
        angle = 2 * pi / sides

        side_bottom = object.Sidelength1.Value
        side_top = object.Sidelength2.Value

        radius_bottom = object.Radius1.Value
        radius_top = object.Radius2.Value

        angle_z = object.Z_rotation.Value
        height = object.Height.Value

        if radius_bottom != self.radius1value or sides != self.sidescountvalue:

            object.Sidelength1.Value = radius_bottom * sin( angle / 2 ) * 2
            self.radius1value = radius_bottom
            self.side1value = object.Sidelength1.Value

        elif side_bottom != self.side1value:

            self.radius1value = ( object.Sidelength1.Value / 2 ) / sin( angle / 2 )
            object.Radius1.Value = self.radius1value

            radius_bottom = self.radius1value

            self.side1value = object.Sidelength1.Value

        if radius_top != self.radius2value or sides != self.sidescountvalue:

            object.Sidelength2.Value = radius_top * sin( angle / 2 ) * 2
            self.radius2value = radius_top
            self.side2value = object.Sidelength2.Value

        elif side_top != self.side2value:

            self.radius2value = ( object.Sidelength2.Value / 2 ) / sin( angle / 2 )
            object.Radius2.Value = self.radius2value

            radius_top = self.radius2value

            self.side2value = object.Sidelength2.Value

        self.sidescountvalue = sides

        faces = []

        if radius_bottom == 0 and radius_top == 0:
            Console.PrintMessage('Both radiuses are zero' + '\n')
            return

        vertexes_bottom = pyramid_Vertexes(sides,radius_bottom,0,angle_z)
        vertexes_top = pyramid_Vertexes(sides,radius_top,height,angle_z)

        if not radius_bottom == 0:

            polygon = makePolygon(vertexes_bottom)
            face = Face(polygon)

            faces.append(face)

        if not radius_top == 0:

            polygon = makePolygon(vertexes_top)
            face = Face(polygon)

            faces.append(face)

        for side in range( sides ):

            if radius_top == 0:

                vertexes = [
                    vertexes_bottom[ side ] ,
                    vertexes_bottom[ side + 1 ] ,
                    vertexes_top[ 0 ] ,
                    vertexes_bottom[ side ]
                ]

            elif radius_bottom == 0:

                vertexes = [
                    vertexes_bottom[ 0 ] ,
                    vertexes_top[ side + 1 ] ,
                    vertexes_top[ side ] ,
                    vertexes_bottom[ 0 ]
                ]

            else:

                vertexes = [
                    vertexes_bottom[ side ] ,
                    vertexes_bottom[ side + 1 ] ,
                    vertexes_top[ side + 1 ] ,
                    vertexes_top[ side ] ,
                    vertexes_bottom[ side ]
                ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)

        shell = makeShell(faces)
        solid = makeSolid(shell)

        object.Shape = solid

