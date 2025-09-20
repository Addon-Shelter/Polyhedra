
from .PySide.QtWidgets import QToolBar
from .Command import Command
from .Shapes import Icosahedron_Truncated , Geodesic_Sphere , Dodecahedron , Octahedron , Icosahedron , Hexahedron , Tetrahedron , Pyramid , Regular_Solid

from FreeCAD import Gui


def registerCommands ( toolbar : QToolBar ):

    command = Command(
        shortcut = 'Shift+D' ,
        shape = Dodecahedron ,
        key = 'Dodecahedron'
    )

    Gui.addCommand('Dodecahedron',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)


    command = Command(
        shortcut = 'Shift+O' ,
        shape = Octahedron ,
        key = 'Octahedron'
    )

    Gui.addCommand('Octahedron',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)


    command = Command(
        shortcut = 'Shift+I' ,
        shape = Icosahedron ,
        key = 'Icosahedron'
    )

    Gui.addCommand('Icosahedron',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)


    command = Command(
        shortcut = 'Shift+H' ,
        shape = Hexahedron ,
        key = 'Hexahedron'
    )

    Gui.addCommand('Hexahedron',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)


    command = Command(
        shortcut = 'Shift+T' ,
        shape = Tetrahedron ,
        key = 'Tetrahedron'
    )

    Gui.addCommand('Tetrahedron',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)


    command = Command(
        shortcut = 'Shift+P' ,
        shape = Pyramid ,
        key = 'Pyramid'
    )

    Gui.addCommand('Pyramid',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)


    command = Command(
        shortcut = 'Shift+P' ,
        shape = Regular_Solid ,
        key = 'Regular-Solid'
    )

    Gui.addCommand('Regular-Solid',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)


    command = Command(
        shortcut = 'Shift+P' ,
        shape = Geodesic_Sphere ,
        key = 'Geodesic-Sphere'
    )

    Gui.addCommand('Geodesic-Sphere',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)


    command = Command(
        shortcut = 'Shift+P' ,
        shape = Icosahedron_Truncated ,
        key = 'Icosahedron-Truncated'
    )

    Gui.addCommand('Icosahedron-Truncated',command)

    action = command.action()
    action.setParent(toolbar)
    toolbar.addAction(action)
