

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Icosahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class IcosahedronCommand:
    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Icosahedron') ,
            "Accel": "Shift+I",
            "MenuText": translated("Icosahedron", "Icosahedron"),
            "ToolTip": translated("Icosahedron", "Generate a Icosahedron"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Icosahedron")
        Icosahedron(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Icosahedron")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        return


    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

