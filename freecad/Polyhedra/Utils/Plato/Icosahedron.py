# SPDX-FileAttributionText: Based on the Blender Add-Mesh-Extra-Objects addon.
# SPDX-License-Identifier: GPL-3.0-or-later

from math import sqrt as sqrt


s = ( 1.0 + sqrt( 5.0 ) ) / 2.0
t = sqrt( 1.0 + s * s )

s = s / t
t = 1 / t


vertices = [
    ( +s , +t , .0 ) ,
    ( -s , +t , .0 ) ,
    ( +s , -t , .0 ) ,
    ( -s , -t , .0 ) ,
    ( +t , .0 , +s ) ,
    ( +t , .0 , -s ) ,
    ( -t , .0 , +s ) ,
    ( -t , .0 , -s ) ,
    ( .0 , +s , +t ) ,
    ( .0 , -s , +t ) ,
    ( .0 , +s , -t ) ,
    ( .0 , -s , -t )
]

faces = [
    [  0 ,  8 ,  4 ] ,
    [  0 ,  5 , 10 ] ,
    [  2 ,  4 ,  9 ] ,
    [  2 , 11 ,  5 ] ,
    [  1 ,  6 ,  8 ] ,
    [  1 , 10 ,  7 ] ,
    [  3 ,  9 ,  6 ] ,
    [  3 ,  7 , 11 ] ,
    [  0 , 10 ,  8 ] ,
    [  1 ,  8 , 10 ] ,
    [  2 ,  9 , 11 ] ,
    [  3 , 11 ,  9 ] ,
    [  4 ,  2 ,  0 ] ,
    [  5 ,  0 ,  2 ] ,
    [  6 ,  1 ,  3 ] ,
    [  7 ,  3 ,  1 ] ,
    [  8 ,  6 ,  4 ] ,
    [  9 ,  4 ,  6 ] ,
    [ 10 ,  5 ,  7 ] ,
    [ 11 ,  7 ,  5 ]
]


plato = ( vertices , faces )
