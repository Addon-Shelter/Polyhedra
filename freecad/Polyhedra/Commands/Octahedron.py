

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Octahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class OctahedronCommand:

    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Octahedron') ,
            "Accel": "Shift+O",
            "MenuText": translated("Octahedron", "Octahedron"),
            "ToolTip": translated("Octahedron", "Generate a Octahedron"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Octahedron")
        Octahedron(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Octahedron")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        return


    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

