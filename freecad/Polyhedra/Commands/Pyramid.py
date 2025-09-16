

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Pyramid

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class PyramidCommand ():

    def GetResources ( self ):
        return {
            'MenuText' : translated('Pyramid','Pyramid') ,
            'ToolTip' : translated('Pyramid','Generate a Pyramid with any number of sides') ,
            'Pixmap' : icon('Shapes/Pyramid') ,
            'Accel' : 'Shift+P'
        }

    def Activated ( self ):

        document = FreeCAD.ActiveDocument

        if not document:
            return

        object = document.addObject('Part::FeaturePython','Pyramid')

        Pyramid(object)
        ViewProviderBox(object.ViewObject,'Pyramid')

        document.recompute()

        Gui.SendMsgToActiveView('ViewFit')

        return


    def IsActive(self):
        return not not FreeCAD.ActiveDocument

