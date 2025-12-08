# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from math import cos , sin , pi


def polygon_Vertexes (
    sides : int ,
    radius : float ,
    z : float ,
    startangle : float = 0
):

    if radius == 0:
        return [ ( 0 , 0 , z ) ]

    vertexes = []

    for index in range(0, sides + 1 ):

        angle = 2 * pi * index / sides + pi + startangle

        x = radius * cos(angle)
        y = radius * sin(angle)

        vertex = ( x , y , z )

        vertexes.append(vertex)

    return vertexes



def pyramid_Vertexes (
    sides : int ,
    radius : float ,
    z : float ,
    angle_z : float = 0
):

    if radius == 0:
        return [ ( 0 , 0 , z ) ]

    odd = ( sides % 2 ) != 0

    vertexes = []

    for index in range(0, sides + 1 ):

        angle =                                 \
            ( pi * ( odd / sides + 0.5 ) ) +    \
            2 * pi * index / sides +            \
            angle_z * pi / 180

        x = radius * cos(angle)
        y = radius * sin(angle)

        vertex = ( x , y , z )

        vertexes.append(vertex)

    return vertexes
