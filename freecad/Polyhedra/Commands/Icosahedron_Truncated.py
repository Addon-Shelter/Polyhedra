

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Icosahedron_Truncated

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class IcosahedronTrCommand:
    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Icosahedron-Truncated') ,
            "Accel": "Shift+F",
            "MenuText": translated("Icosahedron_truncated", "Icosahedron truncated"),
            "ToolTip": translated(
                "Icosahedron_truncated", "Generate a Truncated Icosahedron (football)"
            ),
        }

    def Activated(self):
        obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "IcosahedronTruncated")
        Icosahedron_Truncated(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Icosahedron-Truncated")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        return


    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

