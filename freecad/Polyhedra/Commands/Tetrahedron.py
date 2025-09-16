

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Tetrahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class TetrahedronCommand:

    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Tetrahedron') ,
            "Accel": "Shift+T",
            "MenuText": translated("Tetrahedron", "Tetrahedron"),
            "ToolTip": translated("Tetrahedron", "Generate a Tetrahedron"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Tetrahedron")
        Tetrahedron(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Tetrahedron")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        return

    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True


