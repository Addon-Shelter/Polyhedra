

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import RegularSolid

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class RegularSolidCommand:

    def GetResources ( self ):
        return {
            'MenuText' : translated('RegularSolid','Regular Solid') ,
            'ToolTip' : translated('RegularSolid','Generate a Regular Solid') ,
            'Pixmap' : icon('Shapes/Regular-Solid') ,
            'Accel' : 'Shift+R'
        }


    def Activated ( self ):

        document = FreeCAD.ActiveDocument

        object = document.addObject('Part::FeaturePython','RegularSolid')

        RegularSolid(object)
        ViewProviderBox(object.ViewObject,'Regular-Solid')

        document.recompute()
        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

