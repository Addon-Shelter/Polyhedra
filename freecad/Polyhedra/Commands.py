
from .Command import Command
from .Shapes import Icosahedron_Truncated , Geodesic_Sphere , Dodecahedron , Octahedron , Icosahedron , Hexahedron , Tetrahedron , Pyramid , Regular_Solid

from FreeCAD import Gui


def registerCommands ():

    command = Command(
        shortcut = 'Shift+D' ,
        shape = Dodecahedron ,
        name = 'Dodecahedron' ,
        icon = 'Dodecahedron' ,
        key = 'Dodecahedron'
    )

    Gui.addCommand('Dodecahedron',command)


    command = Command(
        shortcut = 'Shift+O' ,
        shape = Octahedron ,
        name = 'Octahedron' ,
        icon = 'Octahedron' ,
        key = 'Octahedron'
    )

    Gui.addCommand('Octahedron',command)


    command = Command(
        shortcut = 'Shift+I' ,
        shape = Icosahedron ,
        name = 'Icosahedron' ,
        icon = 'Icosahedron' ,
        key = 'Icosahedron'
    )

    Gui.addCommand('Icosahedron',command)


    command = Command(
        shortcut = 'Shift+H' ,
        shape = Hexahedron ,
        name = 'Hexahedron' ,
        icon = 'Hexahedron' ,
        key = 'Hexahedron'
    )

    Gui.addCommand('Hexahedron',command)


    command = Command(
        shortcut = 'Shift+T' ,
        shape = Tetrahedron ,
        name = 'Tetrahedron' ,
        icon = 'Tetrahedron' ,
        key = 'Tetrahedron'
    )

    Gui.addCommand('Tetrahedron',command)


    command = Command(
        shortcut = 'Shift+P' ,
        shape = Pyramid ,
        name = 'Pyramid' ,
        icon = 'Pyramid' ,
        key = 'Pyramid'
    )

    Gui.addCommand('Pyramid',command)


    command = Command(
        shortcut = 'Shift+P' ,
        shape = Regular_Solid ,
        name = 'Regular Solid' ,
        icon = 'Regular-Solid' ,
        key = 'Regular-Solid'
    )

    Gui.addCommand('Regular-Solid',command)


    command = Command(
        shortcut = 'Shift+P' ,
        shape = Geodesic_Sphere ,
        name = 'Geodesic Sphere' ,
        icon = 'Geodesic-Sphere' ,
        key = 'Geodesic-Sphere'
    )

    Gui.addCommand('Geodesic-Sphere',command)


    command = Command(
        shortcut = 'Shift+P' ,
        shape = Icosahedron_Truncated ,
        name = 'Icosahedron Truncated' ,
        icon = 'Icosahedron-Truncated' ,
        key = 'Icosahedron-Truncated'
    )

    Gui.addCommand('Icosahedron-Truncated',command)
