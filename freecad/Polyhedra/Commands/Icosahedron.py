

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Icosahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class IcosahedronCommand:

    def GetResources ( self ):
        return {
            'MenuText' : translated('Icosahedron','Icosahedron') ,
            'ToolTip' : translated('Icosahedron','Generate a Icosahedron') ,
            'Pixmap' : icon('Shapes/Icosahedron') ,
            'Accel' : 'Shift+I'
        }


    def Activated ( self ):

        document = FreeCAD.ActiveDocument

        object = document.addObject('Part::FeaturePython','Icosahedron')

        Icosahedron(object)
        ViewProviderBox(object.ViewObject, 'Icosahedron')

        document.recompute()
        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

