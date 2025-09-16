

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Tetrahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class TetrahedronCommand:

    def GetResources ( self ):
        return {
            'MenuText' : translated('Tetrahedron','Tetrahedron') ,
            'ToolTip' : translated('Tetrahedron','Generate a Tetrahedron') ,
            'Pixmap' : icon('Shapes/Tetrahedron') ,
            'Accel' : 'Shift+T'
        }


    def Activated ( self ):

        document = FreeCAD.ActiveDocument

        object = document.addObject('Part::FeaturePython','Tetrahedron')

        Tetrahedron(object)
        ViewProviderBox(object.ViewObject, 'Tetrahedron')

        document.recompute()
        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None


