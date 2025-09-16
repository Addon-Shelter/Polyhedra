
import FreeCAD

from .Utils.ViewProviderBox import ViewProviderBox
from .Utils.Resources import icon
from .Locale import Shapes

from FreeCAD import Gui , Qt
from typing import Any


t = Qt.QT_TRANSLATE_NOOP

Tooltip = t('Command.Tooltip','Generate a {{ Name }}')


class Command:

    shortcut : str
    shape : Any
    icon : str
    name : str

    def __init__ (
        self ,
        icon : str ,
        shape : object ,
        shortcut : str ,
        key : str
    ):

        self.shortcut = shortcut
        self.shape = shape
        self.icon = icon

        self.name = Shapes[ key ]


    def GetResources ( self ):

        tooltip = Tooltip.replace(r'{{ Name }}',self.name)

        return {
            'MenuText' : self.name ,
            'ToolTip' : tooltip ,
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

