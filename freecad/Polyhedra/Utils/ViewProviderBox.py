
from .Resources import icon


class ViewProviderBox:

    obj_name = "Dodecahedron"

    def __init__(self, obj, obj_name):
        self.obj_name = obj_name
        obj.Proxy = self

    def attach(self, obj):
        return

    def updateData(self, fp, prop):
        return

    def onChanged(self, vobj, prop):
        pass

    def getIcon(self):
        return icon(f'Shapes/{ self.obj_name }')

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None
