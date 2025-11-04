# SPDX-License-Identifier: GPL-3.0-or-later

from math import sqrt


#
#   Approximate experience values!
#   Not all sides are equal!
#

Sides = {
    '2' : 618.034 ,
    '3' : 412.41 ,
    '4' : 312.87 ,
    '5' : 245.09 ,
    '6' : 205.91 ,
    '7' : 173.53 ,
    '8' : 152.96 ,
    '9' : 135.96 ,
    '10' : 121.55
}


def geodesic_radius2side (
    radius : float ,
    div : int
):

    div = int(round(div))

    if div < 0:
        return 0

    if div == 1:
        return radius * 4 / sqrt( 10 + 2 * sqrt(5) )
    elif div <= 10:
        factor = Sides[ str(div) ]
        return radius * factor / 1000

    return 0


def geodesic_side2radius (
    side : float ,
    div : int
):


    div = int(round(div))

    if div < 0:
        return 0

    if div == 1:
        return side / 4 * sqrt( 10 + 2 * sqrt(5) )

    if div <= 10:
        factor = Sides[ str(div) ]
        return side * 1000 / factor

    return 0

