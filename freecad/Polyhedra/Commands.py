# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from PySide6.QtWidgets import QToolBar
from .Command import Command
from .Shapes import Icosahedron_Truncated , Geodesic_Sphere , Dodecahedron , Octahedron , Icosahedron , Hexahedron , Tetrahedron , Pyramid , Regular_Solid

def registerCommands (
    toolbar : QToolBar
):

    Command(
        shortcut = 'Shift+D' ,
        toolbar = toolbar ,
        shape = Dodecahedron ,
        key = 'Dodecahedron'
    )

    Command(
        shortcut = 'Shift+O' ,
        toolbar = toolbar ,
        shape = Octahedron ,
        key = 'Octahedron'
    )

    Command(
        shortcut = 'Shift+I' ,
        toolbar = toolbar ,
        shape = Icosahedron ,
        key = 'Icosahedron'
    )

    Command(
        shortcut = 'Shift+H' ,
        toolbar = toolbar ,
        shape = Hexahedron ,
        key = 'Hexahedron'
    )

    Command(
        shortcut = 'Shift+T' ,
        toolbar = toolbar ,
        shape = Tetrahedron ,
        key = 'Tetrahedron'
    )

    Command(
        shortcut = 'Shift+P' ,
        toolbar = toolbar ,
        shape = Pyramid ,
        key = 'Pyramid'
    )

    Command(
        shortcut = 'Shift+P' ,
        shape = Regular_Solid ,
        toolbar = toolbar ,
        key = 'Regular-Solid'
    )

    Command(
        shortcut = 'Shift+P' ,
        shape = Geodesic_Sphere ,
        toolbar = toolbar ,
        key = 'Geodesic-Sphere'
    )

    Command(
        shortcut = 'Shift+P' ,
        shape = Icosahedron_Truncated ,
        toolbar = toolbar ,
        key = 'Icosahedron-Truncated'
    )
