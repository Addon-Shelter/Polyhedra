# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from math import sqrt


#
#   Approximate experience values!
#   Not all sides are equal!
#

Sides = {
    '10' : 121.550 ,
     '9' : 135.960 ,
     '8' : 152.960 ,
     '7' : 173.530 ,
     '6' : 205.910 ,
     '5' : 245.090 ,
     '4' : 312.870 ,
     '3' : 412.410 ,
     '2' : 618.034
}


def radiusToSide (
    radius : float ,
    divisions : int
):

    divisions = int( round(divisions) )

    if divisions < 0 :
        return 0

    if divisions == 1 :
        return radius * 4 / sqrt( 10 + 2 * sqrt(5) )

    if divisions <= 10 :
        factor = Sides[ str(divisions) ]
        return radius * factor / 1000

    return 0


def sideToRadius (
    side : float ,
    divisions : int
):


    divisions = int(round(divisions))

    if divisions < 0 :
        return 0

    if divisions == 1 :
        return side / 4 * sqrt( 10 + 2 * sqrt(5) )

    if divisions <= 10 :
        factor = Sides[ str(divisions) ]
        return side * 1000 / factor

    return 0

