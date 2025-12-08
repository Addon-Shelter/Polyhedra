# SPDX-License-Identifier: GPL-3.0-or-later

from .Dodecahedron import plato as Dodecahedron
from .Icosahedron import plato as Icosahedron
from .Tetrahedron import plato as Tetrahedron
from .Hexahedron import plato as Hexahedron
from .Octahedron import plato as Octahedron

from FreeCAD import Vector
from typing import Literal


PlatoType = Literal[ '4' , '6' , '8' , '12' , '20' ]


Plato = {
    '20' : Icosahedron ,
    '12' : Dodecahedron ,
     '8' : Octahedron ,
     '6' : Hexahedron ,
     '4' : Tetrahedron
}


def plato ( type : PlatoType ):

    vertices , faces = Plato[ type ]

    vectors = [ Vector(vertex) for vertex in vertices ]

    return vectors , faces