# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import DocumentObject , Units , Qt
from typing import Any
from Part import makePolygon , makeSolid , makeShell , Face
from math import sqrt , pi


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class HexahedronPart ( DocumentObject ):

    Radius : Units.Quantity
    Side : Units.Quantity

    Shape : Any


class Hexahedron:

    __module__ = 'Virtual.Polyhedra.Parts'
    __name__ = 'Hexahedron'

    radius = 0

    def __init__ (
        self ,
        object : HexahedronPart ,
        radius : float = 5
    ):

        def property (
            description : str ,
            type : str ,
            name : str
        ):
            object.addProperty(
                f'App::Property{ type }',
                name , 'Hexahedron' ,
                description
            )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of the hexahedron') ,
            name = 'Radius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Sidelength of the hexahedron') ,
            name = 'Side' ,
            type = 'Length'
        )

        object.Radius.Value = radius
        object.Proxy = self


    def execute ( self , object : HexahedronPart ):

        print('Side',type(object.Side))

        radius = object.Radius.Value
        side = object.Side.Value

        if radius == self.radius :
            self.radius = side / 2 * sqrt(3)
            object.Radius.Value = self.radius
            radius = self.radius
            side = object.Side.Value
        else:
            side = radius * 2 / sqrt(3)
            object.Side.Value = side
            self.radius = radius

        faces = []

        vertexes_bottom = polygon_Vertexes(4,sqrt(side ** 2 / 2),- side / 2, pi / 4)
        vertexes_top    = polygon_Vertexes(4,sqrt(side ** 2 / 2), side / 2, pi / 4)

        for i in range(4):

            vertexes = [
                vertexes_bottom[ i ] ,
                vertexes_bottom[ i + 1 ] ,
                vertexes_top[ i + 1 ] ,
                vertexes_top[ i ] ,
                vertexes_bottom[ i ]
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)

        polygon = makePolygon(vertexes_bottom)
        face = Face(polygon)

        faces.append(face)


        polygon = makePolygon(vertexes_top)
        face = Face(polygon)

        faces.append(face)


        shell = makeShell(faces)
        solid = makeSolid(shell)

        object.Shape = solid

