

from .Utils.Resources import icon
from .Commands import registerCommands

from FreeCAD import Gui , Qt


translatable = Qt.QT_TRANSLATE_NOOP
translate = Qt.translate


class PolyhedraWorkbench ( Gui.Workbench ):

    MenuText = translate('Workbench','Pyramids-and-Polyhedrons')
    ToolTip = translate('Workbench','A workbench for generating pyramids, polyhedrons and geodesic spheres')

    def __init__ ( self ):
        self.__class__.Icon = icon('Workbench')


    def Initialize(self):

        registerCommands()

        # Commands

        self.list = [
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

        title = translatable('Workbench','Pyramids-and-Polyhedrons')

        self.appendToolbar(title,self.list)
        self.appendMenu(title,self.list)


    def ContextMenu ( self , recipient ):

        title = translatable('Workbench','Pyramids-and-Polyhedrons')

        self.appendContextMenu(title,self.list)


    def GetClassName ( self ):
        return 'Gui::PythonWorkbench'

    def Deactivated ( self ):
        pass

    def Activated ( self ):
        pass