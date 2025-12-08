# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from .Resources import icon

from FreeCAD import DocumentObject , Gui

View = Gui.ViewProviderDocumentObject


class ViewProvider:

    __module__ = 'Virtual.Polyhedra.ViewProviders'
    __name__ = 'ViewProvider'

    view : View

    def __init__( self , view : View ):
        view.Proxy = self
        self.view = view

    def attach ( self , view : View ):
        self.view = view

    def updateData ( self , fp , prop ):
        pass

    def onChanged( self , vobj , prop ):
        pass

    def getIcon ( self ):

        object : DocumentObject = self.view.Object

        type = object.getPropertyByName('Type')

        return icon(f'Shapes/{ type }')

    def loads ( self , state ):
        pass

    def dumps ( self ):
        return None
