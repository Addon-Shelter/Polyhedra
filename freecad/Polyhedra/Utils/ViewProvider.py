
from .Resources import icon


class ViewProvider:

    icon : str

    def __init__(
        self ,
        obj ,
        icon : str
    ):
        self.icon = icon
        obj.Proxy = self

    def attach ( self , object ):
        return

    def updateData ( self , fp , prop ):
        return

    def onChanged( self , vobj , prop ):
        pass

    def getIcon ( self ):
        return icon(f'Shapes/{ self.icon }')

    def __setstate__ ( self , state ):
        return None

    def __getstate__ ( self ):
        return None
