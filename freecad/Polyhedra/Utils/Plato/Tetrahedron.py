# SPDX-FileAttributionText: Based on the Blender Add-Mesh-Extra-Objects addon.
# SPDX-License-Identifier: GPL-3.0-or-later

from math import sqrt as sqrt


s = sqrt( 2.0 ) / 3.0
t = -1.0 / 3.0
u = sqrt( 6.0 ) / 3.0


vertices = [
    ( 0.0 , 0.0 , 1.0 ) ,
    ( 2.0 * s , 0.0 , +t ) ,
    ( -s , +u , +t ) ,
    ( -s , -u , +t )
]

faces = [
    [ 0 , 1 , 2 ] ,
    [ 0 , 2 , 3 ] ,
    [ 0 , 3 , 1 ] ,
    [ 1 , 3 , 2 ]
]


plato = ( vertices , faces )
