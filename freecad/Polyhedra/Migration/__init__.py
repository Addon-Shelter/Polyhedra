
from types import ModuleType
from sys import modules

import freecad.Polyhedra.Utils.ViewProvider as ViewProviders
import freecad.Polyhedra.Migration.Object as Module
import freecad.Polyhedra.Shapes as Shapes


modules[ 'polyhedrons' ] = Module


modules[ 'Virtual' ] = ModuleType('Virtual')
modules[ 'Virtual.Polyhedra' ] = ModuleType('Polyhedra')



providers = ModuleType('ViewProviders')
setattr(providers,'ViewProvider',ViewProviders.ViewProvider)
modules[ 'Virtual.Polyhedra.ViewProviders' ] = providers


parts = ModuleType('Parts')
setattr(parts,'Icosahedron_Truncated',Shapes.Icosahedron_Truncated)
setattr(parts,'Geodesic_Sphere',Shapes.Geodesic_Sphere)
setattr(parts,'Regular_Solid',Shapes.Regular_Solid)
setattr(parts,'Dodecahedron',Shapes.Dodecahedron)
setattr(parts,'Icosahedron',Shapes.Icosahedron)
setattr(parts,'Tetrahedron',Shapes.Tetrahedron)
setattr(parts,'Hexahedron',Shapes.Hexahedron)
setattr(parts,'Octahedron',Shapes.Octahedron)
setattr(parts,'Pyramid',Shapes.Pyramid)
modules[ 'Virtual.Polyhedra.Parts' ] = parts

