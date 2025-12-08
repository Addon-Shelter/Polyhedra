# SPDX-FileAttributionText: Based on the Blender Add-Mesh-Extra-Objects addon.
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.


vertices = [

    ( +1.0 , +0.0 , +0.0 ) ,
    ( -1.0 , +0.0 , +0.0 ) ,

    ( +0.0 , +1.0 , +0.0 ) ,
    ( +0.0 , -1.0 , +0.0 ) ,

    ( +0.0 , +0.0 , +1.0 ) ,
    ( +0.0 , +0.0 , -1.0 )
]

faces = [

    [ 4 , 0 , 2 ] ,
    [ 4 , 2 , 1 ] ,
    [ 4 , 1 , 3 ] ,
    [ 4 , 3 , 0 ] ,

    [ 5 , 2 , 0 ] ,
    [ 5 , 1 , 2 ] ,
    [ 5 , 3 , 1 ] ,
    [ 5 , 0 , 3 ]
]


plato = ( vertices , faces )

