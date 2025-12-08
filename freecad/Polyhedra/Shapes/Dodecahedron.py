# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import DocumentObject , Units , Qt
from typing import Any
from Part import makePolygon , makeSolid , makeShell , Face
from math import sqrt , sin , cos , pi


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class DodecahedronPart ( DocumentObject ):

    Radius : Units.Quantity
    Side : Units.Quantity

    Shape : Any


class Dodecahedron:

    __module__ = 'Virtual.Polyhedra.Parts'
    __name__ = 'Dodecahedron'

    radius = 0

    def __init__ (
        self ,
        object : DodecahedronPart ,
        radius : float = 5
    ):


        def property (
            description : str ,
            type : str ,
            name : str
        ):
            object.addProperty(
                f'App::Property{ type }',
                name , 'Dodecahedron' ,
                description
            )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of the dodecahedron') ,
            name = 'Radius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Sidelength of the dodecahedron') ,
            name = 'Side' ,
            type = 'Length'
        )

        object.Radius.Value = radius
        object.Proxy = self


    def execute ( self , object : DodecahedronPart ):

        anglefaces = 116.565051177
        angleribs = 121.717474411

        radius = object.Radius.Value
        side = object.Side.Value

        if radius == self.radius :
            self.radius = side * ( sqrt(3) * ( 1 + sqrt(5) ) ) / 4
            object.Radius.Value = self.radius
            radius = self.radius
        else:
            object.Side.Value = 4 * radius /  ( sqrt(3) * ( 1 + sqrt(5) ) )
            self.radius = radius

        faces = []

        z = 4 * radius /  ( sqrt(3) * ( 1 + sqrt(5) ) )
        r = z / 2 * sqrt( ( 25 + ( 11 * sqrt(5) ) )  / 10 )

        # int sphere r is height / 2

        h2 = z * sin( angleribs / 180 * pi )

        # height of the side-tips

        radius1 = z / 2 / sin( 36 * pi / 180 )

        # height of the tops

        h5h = ( radius1 + radius1 * cos( 36 * pi / 180 ) )   \
            * sin( anglefaces * pi / 180 )

        radius2 = radius1 - z * cos( angleribs * pi / 180 )

        # XXX to make it fit!
        r = ( h2 + h5h ) / 2


        vertexes_bottom = polygon_Vertexes(5,radius1,-r)

        polygon = makePolygon(vertexes_bottom)
        face = Face(polygon)

        faces.append(face)


        vertexes_top = polygon_Vertexes(5,radius1,r, pi / 5 )

        polygon = makePolygon(vertexes_top)
        face = Face(polygon)

        faces.append(face)


        vertexes_low = polygon_Vertexes(5,radius2,-r + h2)
        vertexes_high = polygon_Vertexes(5,radius2,-r + h5h,pi / 5)

        for side in range(5):

            vertexes = [
                vertexes_bottom[ side ] ,
                vertexes_bottom[ side + 1 ] ,
                vertexes_low[ side + 1 ] ,
                vertexes_high[ side ] ,
                vertexes_low[ side ],
                vertexes_bottom[ side ]
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)


        for side in range(5):

            vertexes = [
                vertexes_top[ side ] ,
                vertexes_top[ side + 1 ] ,
                vertexes_high[ side + 1 ] ,
                vertexes_low[ side + 1 ] ,
                vertexes_high[ side ] ,
                vertexes_top[ side ]
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)

        shell = makeShell(faces)
        solid = makeSolid(shell)

        object.Shape = solid
