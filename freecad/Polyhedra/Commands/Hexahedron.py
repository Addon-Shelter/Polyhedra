

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Hexahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class HexahedronCommand:

    def GetResources ( self ):
        return {
            'MenuText' : translated('Hexahedron','Hexahedron') ,
            'ToolTip' : translated('Hexahedron','Generate a Hexahedron') ,
            'Pixmap' : icon('Shapes/Hexahedron') ,
            'Accel' : 'Shift+H'
        }


    def Activated ( self ):

        document = FreeCAD.ActiveDocument

        object = document.addObject('Part::FeaturePython','Hexahedron')

        Hexahedron(object)
        ViewProviderBox(object.ViewObject,'Hexahedron')

        document.recompute()
        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

