
from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import DocumentObject , Qt
from typing import Any
from Part import makePolygon , makeSolid , makeShell , Face
from math import sqrt , pi


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class HexahedronPart ( DocumentObject ):

    Radius : float
    Side : float

    Shape : Any


class Hexahedron:

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

        object.Radius = radius
        object.Proxy = self


    def execute ( self , object : HexahedronPart ):

        radius = float( object.Radius )

        if radius == self.radius :
            self.radius = object.Side / 2 * sqrt(3)
            object.Radius = self.radius
            radius = self.radius
            side = object.Side
        else:
            side = radius * 2 / sqrt(3)
            object.Side = side
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

