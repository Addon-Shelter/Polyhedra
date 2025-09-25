
from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import DocumentObject , Units , Qt
from typing import Any
from Part import makePolygon , makeSolid , makeShell , Face
from math import sqrt


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class OctahedronPart ( DocumentObject ):

    Radius : Units.Quantity
    Side : Units.Quantity

    Shape : Any


class Octahedron:

    # Z = R * sqrt(2)
    radius = 0

    def __init__ (
        self ,
        object : OctahedronPart ,
        radius : float = 5
    ):

        def property (
            description : str ,
            type : str ,
            name : str
        ):
            object.addProperty(
                f'App::Property{ type }',
                name , 'Octahedron' ,
                description
            )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of the octahedron') ,
            name = 'Radius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Sidelength of the octahedron') ,
            name = 'Side' ,
            type = 'Length'
        )

        object.Radius.Value = radius
        object.Proxy = self


    def execute ( self , object : OctahedronPart ):

        radius = object.Radius.Value
        side = object.Side.Value

        if radius == self.radius :
            self.radius = side / sqrt(2)
            object.Radius.Value = self.radius
            radius = self.radius
        else:
            object.Side.Value = radius * sqrt(2)
            self.radius = radius


        faces = []

        vertexes_middle = polygon_Vertexes(4,radius,0)


        #   Top Sides

        vertexes_top = polygon_Vertexes(1,0,radius)

        for i in range(4):

            vertexes = [
                vertexes_middle[ i ] ,
                vertexes_middle[ i + 1 ] ,
                vertexes_top[ 0 ] ,
                vertexes_middle[ i ]
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)


        #   Bottom Sides

        vertexes_bottom = polygon_Vertexes(1,0,-radius)

        for i in range(4):

            vertexes = [
                vertexes_middle[ i ] ,
                vertexes_middle[ i + 1 ] ,
                vertexes_bottom[ 0 ] ,
                vertexes_middle[ i ]
            ]

            polygon = makePolygon(vertexes)
            face = Face(polygon)

            faces.append(face)

        shell = makeShell(faces)
        solid = makeSolid(shell)
        object.Shape = solid

