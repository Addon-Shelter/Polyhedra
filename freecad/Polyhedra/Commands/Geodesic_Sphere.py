

import FreeCAD

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Shapes import Geodesic_Sphere

from FreeCAD import Gui , Qt


translated = Qt.QT_TRANSLATE_NOOP


class GeodesicSphereCommand:

    def GetResources ( self ):
        return {
            'MenuText' : translated('Geodesic_sphere','Geodesic sphere') ,
            'ToolTip' : translated('Geodesic_sphere','Generate Geodesic Spheres') ,
            'Pixmap' : icon('Shapes/Geodesic-Sphere') ,
            'Accel' : 'Shift+G'
        }


    def Activated ( self ):

        document = FreeCAD.ActiveDocument

        object = document.addObject('Part::FeaturePython','GeodesicSphere')

        Geodesic_Sphere(object)
        ViewProviderBox(object.ViewObject,'Geodesic-sphere')

        document.recompute()
        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

