

from .Utils.Resources import icon
from .Commands import registerCommands

from FreeCAD import Gui , Qt


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


class PolyhedraWorkbench ( Gui.Workbench ):

    MenuText = QT_TRANSLATE_NOOP('Workbench','Polyhedra')
    ToolTip = QT_TRANSLATE_NOOP('Workbench','A workbench for generating pyramids, polyhedrons and geodesic spheres')

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

        title = QT_TRANSLATE_NOOP('Workbench','Polyhedra')

        self.appendToolbar(title,self.list)
        self.appendMenu(title,self.list)


    def ContextMenu ( self , recipient ):

        title = QT_TRANSLATE_NOOP('Workbench','Polyhedra')

        self.appendContextMenu(title,self.list)


    def GetClassName ( self ):
        return 'Gui::PythonWorkbench'

    def Deactivated ( self ):
        pass

    def Activated ( self ):
        pass