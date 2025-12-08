# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import DocumentObject , Units , Qt
from typing import Any
from Part import makePolygon , makeSolid , makeShell , Face
from math import sqrt


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class TetrahedronPart ( DocumentObject ):

    Radius : Units.Quantity
    Side : Units.Quantity

    Shape : Any


class Tetrahedron:

    __module__ = 'Virtual.Polyhedra.Parts'
    __name__ = 'Tetrahedron'

    # == basics ==
    #R = z / 4 * sqrt(6)
    #ro = z / 12 * sqrt(6)    -->   ro = R / 3
    #z = 4 * R / sqrt(6)
    #h = z / 3 * sqrt(6) = 4 * R / sqrt(6) /3 * sqrt(6) = 4 * R / 3  = ro + R
    #radius at level = z / 2 / cos(30) = (4 * R / sqrt(6)) / 2 / sqrt(3) * 2 = 4 * R / (sqrt(6) * sqrt(3))= 4 * R / (3 * sqrt(2)

    radius = 0

    def __init__ (
        self ,
        object : TetrahedronPart ,
        radius : float = 5
    ):

        def property (
            description : str ,
            type : str ,
            name : str
        ):
            object.addProperty(
                f'App::Property{ type }',
                name , 'Tetrahedron' ,
                description
            )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of the tetrahedron') ,
            name = 'Radius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Sidelength of the tetrahedron') ,
            name = 'Side' ,
            type = 'Length'
        )

        object.Radius.Value = radius
        object.Proxy = self


    def execute ( self , object : TetrahedronPart ):

        radius = object.Radius.Value
        side = object.Side.Value

        if radius == self.radius :
            self.radius = side * sqrt(6) / 4
            object.Radius.Value = self.radius
            radius = self.radius
        else:
            object.Side.Value = radius * 4 / sqrt(6)
            self.radius = radius


        vertexes_bottom = polygon_Vertexes(3,4 * radius / 3 / sqrt(2),- radius / 3)
        vertexes_top = polygon_Vertexes(1,0,radius)

        faces = []

        for side in range(3):

            vertexes = [
                vertexes_bottom[ side ] ,
                vertexes_bottom[ side + 1 ] ,
                vertexes_top[ 0 ] ,
                vertexes_bottom[ side ]
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)

        polygon_bottom = makePolygon(vertexes_bottom)
        face = Face(polygon_bottom)

        faces.append(face)

        shell = makeShell(faces)
        solid = makeSolid(shell)

        object.Shape = solid

