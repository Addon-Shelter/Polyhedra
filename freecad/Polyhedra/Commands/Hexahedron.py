

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Hexahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class HexahedronCommand:

    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Hexahedron') ,
            "Accel": "Shift+H",
            "MenuText": translated("Hexahedron", "Hexahedron"),
            "ToolTip": translated("Hexahedron", "Generate a Hexahedron"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Hexahedron")
        Hexahedron(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Hexahedron")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        return

    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

