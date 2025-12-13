# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

import FreeCAD

from .Utils.ViewProvider import ViewProvider
from .Utils.Resources import icon
from .Utils.Version import Version
from .Locale import Shapes

from .PySide.QtWidgets import QToolBar
from .PySide.QtCore import SIGNAL
from .PySide.QtGui import QAction , QIcon

from FreeCAD import DocumentObject , Gui , Qt
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
        shape : object ,
        shortcut : str ,
        toolbar : QToolBar ,
        key : str
    ):

        self.shortcut = shortcut
        self.shape = shape
        self.icon = key

        self.name = Shapes[ key ]

        Gui.addCommand(key,self)

        action = self.action()
        action.setParent(toolbar)
        toolbar.addAction(action)


    def GetResources ( self ):

        tooltip = Tooltip.replace(r'{{ Name }}',self.name)

        return {
            'MenuText' : self.name ,
            'ToolTip' : tooltip ,
            'Pixmap' : self.iconPath() ,
            'Accel' : self.shortcut
        }


    def Activated ( self ):

        shape = self.shape
        name = self.name

        document = FreeCAD.ActiveDocument

        if not document:
            return

        object : DocumentObject = document \
            .addObject('Part::FeaturePython',name)

        object.addProperty(
            read_only = True ,
            hidden = True ,
            type = 'App::PropertyString',
            name = 'Version'
        )

        object.addProperty(
            read_only = True ,
            hidden = True ,
            type = 'App::PropertyString',
            name = 'Type'
        )

        setattr(object,'Version',Version)
        setattr(object,'Type',self.icon)

        view = object.ViewObject

        if view:
            ViewProvider(view)

        shape(object)

        document.recompute()

        Gui.SendMsgToActiveView('ViewFit')


    def IsActive ( self ):
        return FreeCAD.ActiveDocument != None

    def iconPath ( self ):
        return icon(f'Shapes/{ self.icon }')

    def action ( self ):

        icon = QIcon( self.iconPath() )

        action = QAction(
            toolTip = self.name ,
            icon = icon
        )

        action.connect(SIGNAL('triggered()'),self.Activated)

        return action
