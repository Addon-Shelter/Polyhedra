

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Icosahedron_Truncated

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class IcosahedronTrCommand:

    def GetResources ( self ):
        return {
            'MenuText' : translated('Icosahedron_truncated','Icosahedron truncated') ,
            'ToolTip' : translated('Icosahedron_truncated','Generate a Truncated Icosahedron (football)') ,
            'Pixmap' : icon('Shapes/Icosahedron-Truncated') ,
            'Accel' : 'Shift+F'
        }


    def Activated ( self ):

        document = FreeCAD.ActiveDocument

        object = document.addObject('Part::FeaturePython','IcosahedronTruncated')

        Icosahedron_Truncated(object)
        ViewProviderBox(object.ViewObject,'Icosahedron-Truncated')

        document.recompute()
        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

