
from .Icosahedron_Truncated import IcosahedronTrCommand
from .Geodesic_Sphere import GeodesicSphereCommand
from .Dodecahedron import DodecahedronCommand
from .RegularSolid import RegularSolidCommand
from .Icosahedron import IcosahedronCommand
from .Tetrahedron import TetrahedronCommand
from .Hexahedron import HexahedronCommand
from .Octahedron import OctahedronCommand
from .Pyramid import PyramidCommand

from FreeCAD import Gui


def registerCommands ():
    
    Gui.addCommand('Icosahedron_truncated',IcosahedronTrCommand())
    Gui.addCommand('Geodesic_sphere',GeodesicSphereCommand())
    Gui.addCommand('RegularSolid',RegularSolidCommand())
    Gui.addCommand('Dodecahedron',DodecahedronCommand())
    Gui.addCommand('Icosahedron',IcosahedronCommand())
    Gui.addCommand('Tetrahedron',TetrahedronCommand())
    Gui.addCommand('Hexahedron',HexahedronCommand())
    Gui.addCommand('Octahedron',OctahedronCommand())
    Gui.addCommand('Pyramid',PyramidCommand())
