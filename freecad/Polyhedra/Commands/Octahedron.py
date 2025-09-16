

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Octahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class OctahedronCommand:

    def GetResources ( self ):
        return {
            'MenuText' : translated('Octahedron','Octahedron') ,
            'ToolTip' : translated('Octahedron','Generate a Octahedron') ,
            'Pixmap' : icon('Shapes/Octahedron') ,
            'Accel' : 'Shift+O'
        }


    def Activated(self):

        document = FreeCAD.ActiveDocument

        object = document.addObject('Part::FeaturePython','Octahedron')

        Octahedron(object)
        ViewProviderBox(object.ViewObject,'Octahedron')

        document.recompute()
        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

