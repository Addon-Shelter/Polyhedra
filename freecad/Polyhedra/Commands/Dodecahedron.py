
import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Dodecahedron

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class DodecahedronCommand:
    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Dodecahedron') ,
            "Accel": "Shift+D",
            "MenuText": translated("Dodecahedron", "Dodecahedron"),
            "ToolTip": translated("Dodecahedron", "Generate a Dodecahedron"),
        }

    def Activated(self):
        obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Dodecahedron")
        Dodecahedron(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Dodecahedron")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        return


    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

