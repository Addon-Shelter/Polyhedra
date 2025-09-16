

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import RegularSolid

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class RegularSolidCommand:
    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Regular-Solid') ,
            "Accel": "Shift+R",
            "MenuText": translated("RegularSolid", "Regular Solid"),
            "ToolTip": translated("RegularSolid", "Generate a Regular Solid"),
        }

    def Activated(self):
        obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "RegularSolid")
        RegularSolid(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Regular-Solid")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")

    def IsActive(self):
        return FreeCAD.ActiveDocument!=None

