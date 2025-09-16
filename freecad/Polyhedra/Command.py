
import FreeCAD

from .Utils.ViewProviderBox import ViewProviderBox
from .Utils.Resources import icon

from FreeCAD import Gui , Qt
from typing import Any


translate = Qt.translate


class Command:

    shortcut : str
    shape : Any
    name : str
    icon : str
    key : str

    def __init__ (
        self ,
        name : str ,
        icon : str ,
        shape : object ,
        shortcut : str ,
        key : str
    ):
        self.shortcut = shortcut
        self.shape = shape
        self.name = name
        self.icon = icon
        self.key = key


    def GetResources ( self ):

        key = self.key

        return {
            'MenuText' : translate(key,key) ,
            'ToolTip' : translate(key,f'Generate a { self.name }') ,
            'Pixmap' : icon(f'Shapes/{ self.icon }') ,
            'Accel' : self.shortcut
        }


    def Activated ( self ):

        shape = self.shape
        name = self.name

        document = FreeCAD.ActiveDocument

        if not document:
            return

        object = document.addObject('Part::FeaturePython',name)

        shape(object)
        ViewProviderBox(object.ViewObject,name)

        document.recompute()

        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

