
from ..Utils.ViewProvider import ViewProvider

from FreeCAD import GuiUp

import freecad.Polyhedra.Shapes as Shapes


class MigrationView : ...


def MigrationPart ( type : str ):

    class Migration:

        def onDocumentRestored ( self , object ):

            print('Migrating pre-PMS part.')

            Proxy = getattr(Shapes,type)

            proxy = Proxy.__new__(Proxy)

            object.Proxy = proxy

            object.addProperty(
                read_only = True ,
                hidden = True ,
                type = 'App::PropertyString',
                name = 'Type'
            )

            object.Type = type

            if GuiUp:

                view = object.ViewObject

                ViewProvider(view)

    return Migration



ViewProviderBox = MigrationView

Icosahedron_truncated = MigrationPart('Icosahedron_Truncated')
Geodesic_sphere = MigrationPart('Geodesic_Sphere')
RegularSolid = MigrationPart('Regular_Solid')
Dodecahedron = MigrationPart('Dodecahedron')
Icosahedron = MigrationPart('Icosahedron')
Tetrahedron = MigrationPart('Tetrahedron')
Hexahedron = MigrationPart('Hexahedron')
Octahedron = MigrationPart('Octahedron')
Pyramid = MigrationPart('Pyramid')
