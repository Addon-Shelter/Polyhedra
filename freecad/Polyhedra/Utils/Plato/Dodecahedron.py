# SPDX-FileAttributionText: Based on the Blender Add-Mesh-Extra-Objects addon.
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from math import sqrt as sqrt


s = 1.0 / sqrt( 3.0 )
t = sqrt( ( 3.0 - sqrt( 5.0 ) ) / 6.0 )
u = sqrt( ( 3.0 + sqrt( 5.0 ) ) / 6.0 )


vertices = [
    ( +s , +s , +s ) ,
    ( +s , +s , -s ) ,
    ( +s , -s , +s ) ,
    ( +s , -s , -s ) ,
    ( -s , +s , +s ) ,
    ( -s , +s , -s ) ,
    ( -s , -s , +s ) ,
    ( -s , -s , -s ) ,

    ( +t , +u , .0 ) ,
    ( -t , +u , .0 ) ,
    ( +t , -u , .0 ) ,
    ( -t , -u , .0 ) ,
    ( +u , .0 , +t ) ,
    ( +u , .0 , -t ) ,
    ( -u , .0 , +t ) ,
    ( -u , .0 , -t ) ,
    ( .0 , +t , +u ) ,

    ( .0 , -t , +u ) ,
    ( .0 , +t , -u ) ,
    ( .0 , -t , -u )
]

faces = [
    [  0 ,  8 ,  9 ,  4 , 16 ] ,
    [  0 , 12 , 13 ,  1 ,  8 ] ,
    [  0 , 16 , 17 ,  2 , 12 ] ,
    [  8 ,  1 , 18 ,  5 ,  9 ] ,
    [ 12 ,  2 , 10 ,  3 , 13 ] ,
    [ 16 ,  4 , 14 ,  6 , 17 ] ,
    [  9 ,  5 , 15 , 14 ,  4 ] ,
    [  6 , 11 , 10 ,  2 , 17 ] ,
    [  3 , 19 , 18 ,  1 , 13 ] ,
    [  7 , 15 ,  5 , 18 , 19 ] ,
    [  7 , 11 ,  6 , 14 , 15 ] ,
    [  7 , 19 ,  3 , 10 , 11 ]
]


plato = ( vertices , faces )
