
import FreeCAD

from .Utils.Resources import icon
from .Shapes import registerCommands


QT_TRANSLATE_NOOP = FreeCAD.Qt.QT_TRANSLATE_NOOP


class PolyhedraWorkbench(FreeCAD.Gui.Workbench):
    translate = FreeCAD.Qt.translate

    MenuText = translate("Workbench", "Pyramids-and-Polyhedrons")
    ToolTip = translate(
        "Workbench", "A workbench for generating pyramids, polyhedrons and geodesic spheres"
    )

    def __init__(self):

        self.__class__.Icon = icon('Workbench')

    def Initialize(self):
        """This function is executed when FreeCAD starts"""

        registerCommands()

        self.list = ["Pyramid","Tetrahedron","Hexahedron","Octahedron","Dodecahedron","Icosahedron","Icosahedron_truncated",
                     "Geodesic_sphere","RegularSolid"] # A list of command names created in the line above
        #self.appendMenu(["An existing Menu","My submenu"],self.list) # appends a submenu to an existing menu
        QT_TRANSLATE_NOOP = FreeCAD.Qt.QT_TRANSLATE_NOOP
        self.appendToolbar(
            QT_TRANSLATE_NOOP("Workbench", "Pyramids-and-Polyhedrons"), self.list
        )  # creates a new toolbar with your commands
        self.appendMenu(
            QT_TRANSLATE_NOOP("Workbench", "Pyramids-and-Polyhedrons"), self.list
        )  # creates a new menu

    def GetClassName ( self ):
        return 'Gui::PythonWorkbench'

    def Deactivated ( self ):
        pass

    def Activated ( self ):
        pass

    def ContextMenu ( self , recipient ):

        # "recipient" will be either "view" or "tree"
        self.appendContextMenu(
            QT_TRANSLATE_NOOP("Workbench", "Pyramids-and-Polyhedrons"), self.list
        )  # add commands to the context menu

