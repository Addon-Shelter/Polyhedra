
from FreeCAD import Gui


Commands = [
    'Pyramid' ,
    'Tetrahedron' ,
    'Hexahedron' ,
    'Octahedron' ,
    'Dodecahedron' ,
    'Icosahedron' ,
    'Icosahedron-Truncated' ,
    'Geodesic-Sphere' ,
    'Regular-Solid'
]

def toAppend ( command : str ):
    return {
        'toolBar' : 'Solids' ,
        'append' : command
    }

Changes = list(map(toAppend,Commands))


class Manipulator:

    def modifyToolBars ( self ):
        return Changes


def extendToolbar ():
    Gui.addWorkbenchManipulator(Manipulator())

