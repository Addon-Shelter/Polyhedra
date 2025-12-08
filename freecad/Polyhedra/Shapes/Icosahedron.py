# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import DocumentObject , Units , Qt
from typing import Any
from Part import makePolygon , makeSolid , makeShell , Face
from math import sqrt , acos , sin , pi


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class IcosahedronPart ( DocumentObject ):

    Radius : Units.Quantity
    Side : Units.Quantity

    Shape : Any


class Icosahedron:

    __module__ = 'Virtual.Polyhedra.Parts'
    __name__ = 'Icosahedron'

    radius = 0

    def __init__ (
        self ,
        object : IcosahedronPart ,
        radius : float = 5
    ):

        def property (
            description : str ,
            type : str ,
            name : str
        ):
            object.addProperty(
                f'App::Property{ type }',
                name , 'Icosahedron' ,
                description
            )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of the icosahedron') ,
            name = 'Radius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Sidelength of the icosahedron') ,
            name = 'Side' ,
            type = 'Length'
        )

        object.Radius.Value = radius
        object.Proxy = self


    def execute ( self , object : IcosahedronPart ):

        radius = object.Radius.Value
        side = object.Side.Value


        if radius == self.radius :
            self.radius = side * sqrt( 10 + 2 * sqrt(5) ) / 4
            object.Radius.Value = self.radius
            radius = self.radius
        else:
            object.Side.Value = 4 * radius / sqrt( 10 + 2 * sqrt(5) )
            self.radius = radius


        z = 4 * radius / sqrt( 10 + 2 * sqrt(5) )


        # radius of a pentagram with the same side

        radius2 = z / sin( 36 * pi / 180 ) / 2

        # height of radius2 in the sphere

        angle = acos( radius2 / radius )
        height = radius * sin(angle)

        faces = []

        vertex_bottom = ( 0 , 0 , - radius )

        vertexes_low = polygon_Vertexes(5,radius2, - height)

        for i in range(5):

            vertexes = [
                vertex_bottom ,
                vertexes_low[ i ] ,
                vertexes_low[ i + 1 ] ,
                vertex_bottom
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)


        vertexes_high = polygon_Vertexes(5,radius2, height, pi / 5)

        for i in range(5):

            vertexes = [
                vertexes_low[ i ] ,
                vertexes_low[ i + 1 ] ,
                vertexes_high[ i ] ,
                vertexes_low[ i ]
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)

            vertexes = [
                vertexes_high[ i ] ,
                vertexes_high[ i + 1 ] ,
                vertexes_low[ i + 1 ] ,
                vertexes_high[ i ]
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)


        vertex_top = ( 0 , 0 , radius )

        for i in range(5):

            vertexes = [
                vertex_top ,
                vertexes_high[ i ] ,
                vertexes_high[ i + 1 ] ,
                vertex_top
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)


        shell = makeShell(faces)
        solid = makeSolid(shell)

        object.Shape = solid
