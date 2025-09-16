

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Geodesic_Sphere

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class GeodesicSphereCommand:
    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Geodesic-Sphere') ,
            "Accel": "Shift+G",
            "MenuText": translated("Geodesic_sphere", "Geodesic sphere"),
            "ToolTip": translated("Geodesic_sphere", "Generate Geodesic Spheres"),
        }

    def Activated(self):
        obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "GeodesicSphere")
        Geodesic_Sphere(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Geodesic-sphere")
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        return


    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

