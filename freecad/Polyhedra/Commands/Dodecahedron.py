
import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Dodecahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class DodecahedronCommand:

    def GetResources ( self ):
        return {
            'MenuText' : translated('Dodecahedron','Dodecahedron') ,
            'ToolTip' : translated('Dodecahedron','Generate a Dodecahedron') ,
            'Pixmap' : icon('Shapes/Dodecahedron') ,
            'Accel' : 'Shift+D'
        }


    def Activated ( self ):

        document = FreeCAD.ActiveDocument

        object = document.addObject('Part::FeaturePython','Dodecahedron')

        Dodecahedron(object)
        ViewProviderBox(object.ViewObject,'Dodecahedron')

        document.recompute()

        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

