
from .Resources import icon

from FreeCAD import DocumentObject , Gui

View = Gui.ViewProviderDocumentObject



class ViewProvider:

    view : View

    def __init__( self , view : View ):
        view.Proxy = self

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
