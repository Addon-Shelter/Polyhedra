# SPDX-FileAttributionText: Based on the Blender Add-Mesh-Extra-Objects addon.
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from math import sqrt as sqrt


s = 1.0 / sqrt( 3.0 )


vertices = [
    ( -s , -s , -s ) ,
    ( +s , -s , -s ) ,
    ( +s , +s , -s ) ,
    ( -s , +s , -s ) ,
    ( -s , -s , +s ) ,
    ( -s , -s , +s ) ,
    ( +s , -s , +s ) ,
    ( -s , +s , +s )
]

faces = [
    [ 0 , 3 , 2 , 1 ] ,
    [ 0 , 1 , 5 , 4 ] ,
    [ 0 , 4 , 7 , 3 ] ,
    [ 6 , 5 , 1 , 2 ] ,
    [ 6 , 2 , 3 , 7 ] ,
    [ 6 , 7 , 4 , 5 ]
]


plato = ( vertices , faces )
