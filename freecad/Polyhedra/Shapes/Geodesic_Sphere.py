# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

import Part

from ..Utils.Geodesic import radiusToSide , sideToRadius
from ..Utils.Vertexes import polygon_Vertexes

from FreeCAD import DocumentObject , Vector , Units , Qt
from typing import Any
from Part import makeSolid , makeShell , Face
from math import sqrt , acos , sin , pi


translate = Qt.translate


class GeodesicSpherePart ( DocumentObject ):

    Radius : Units.Quantity
    Side : Units.Quantity

    DividedBy : int
    Shape : Any


class Geodesic_Sphere:

    __module__ = 'Virtual.Polyhedra.Parts'
    __name__ = 'Geodesic_Sphere'

    divided_by : int = 2
    radius : float = 0


    def __init__ (
        self ,
        object : GeodesicSpherePart ,
        radius : float = 5 ,
        div : int = 2
    ):

        def property (
            description : str ,
            type : str ,
            name : str
        ):
            object.addProperty(
                f'App::Property{ type }',
                name , 'Geodesic' ,
                description
            )

        property(
            description = translate('App::Property','Radius of the sphere') ,
            name = 'Radius' ,
            type = 'Length'
        )

        property(
            description = translate('App::Property','Sidelength of the triangles (approximative!)') ,
            name = 'Side' ,
            type = 'Length'
        )

        property(
            description = translate('Properties tooltips','The sides of the basic polyhedron are divided in ... (value 1 to 10)') ,
            name = 'DividedBy' ,
            type = 'Integer'
        )

        object.Radius.Value = radius
        object.DividedBy = div
        object.Proxy = self


    def geodesic_divide_triangles (
        self ,
        vertex1 ,
        vertex2 ,
        vertex3 ,
        faces
    ):

        vector1 = ( Vector(vertex2) - Vector(vertex1) ) / self.divided_by
        vector2 = ( Vector(vertex3) - Vector(vertex2) ) / self.divided_by

        points = {}


        points[ str(1) ] = Vector(vertex1)


        for level in range( self.divided_by ) :

            l1 = level + 1
            points[ str( l1 * 10 + 1 ) ] = points[ str(1) ] + vector1 * (l1)

            for pt in range( level + 1 ):
                points[ str( l1 * 10 + 2 + pt ) ] = points[ str( l1 * 10 + 1 ) ] + vector2 * ( pt + 1 )


        for level in range( self.divided_by ) :

            for point in range( level + 1 ) :

                vertex1x = points[ str( level * 10 +  1 + point ) ].normalize().multiply(self.radius)
                vertex2x = points[ str( level * 10 + 11 + point ) ].normalize().multiply(self.radius)
                vertex3x = points[ str( level * 10 + 12 + point ) ].normalize().multiply(self.radius)

                vertexes = [ vertex1x , vertex2x , vertex3x , vertex1x ]

                polygon = Part.makePolygon(vertexes)
                face = Face(polygon)

                faces.append(face)


            for point in range(level):

                vertex1x = points[ str( level * 10 +  1 + point ) ].normalize().multiply(self.radius)
                vertex2x = points[ str( level * 10 +  2 + point ) ].normalize().multiply(self.radius)
                vertex3x = points[ str( level * 10 + 12 + point ) ].normalize().multiply(self.radius)

                vertexes = [ vertex1x , vertex2x , vertex3x , vertex1x ]

                polygon = Part.makePolygon(vertexes)
                face = Face(polygon)

                faces.append(face)


        return faces


    def execute ( self , object : GeodesicSpherePart ):

        divisions = object.DividedBy

        divisions = int( round(divisions) )

        divisions = max( 1 , min( divisions , 10 ) )

        object.DividedBy = divisions


        radius = object.Radius.Value
        side = object.Side.Value

        if radius != self.radius or divisions != self.divided_by:
            self.divided_by = divisions
            object.Side.Value = radiusToSide(radius,self.divided_by)
            self.radius = radius
        else:
            self.radius = sideToRadius(side,self.divided_by)
            object.Radius.Value = self.radius
            radius = self.radius

        self.divided_by = divisions

        z = 4 * radius / sqrt( 10 + 2 * sqrt(5) )


        # Radius of a pentagram with the same side

        radius2 = z / sin( 36 * pi / 180 ) / 2

        # Height of radius2 in the sphere

        angle = acos( radius2 / radius )
        height = radius * sin(angle)

        faces = []

        vertexes_high = polygon_Vertexes(5,radius2,height,pi / 5)
        vertexes_low = polygon_Vertexes(5,radius2, -height)

        vertex_bottom = ( 0 , 0 , -radius )
        vertex_top = ( 0 , 0 , radius )

        for i in range(5):
            faces = self.geodesic_divide_triangles(vertex_bottom,vertexes_low[ i + 1 ],vertexes_low[ i ],faces)

        for i in range(5):
            faces = self.geodesic_divide_triangles(vertexes_high[ i ],vertexes_low[ i + 1 ],vertexes_low[ i ],faces)
            faces = self.geodesic_divide_triangles(vertexes_low[ i + 1 ],vertexes_high[ i + 1 ],vertexes_high[ i ],faces)

        for i in range(5):
            faces = self.geodesic_divide_triangles(vertex_top,vertexes_high[ i ],vertexes_high[ i + 1 ],faces)


        shell = makeShell(faces)
        solid = makeSolid(shell)

        object.Shape = solid

