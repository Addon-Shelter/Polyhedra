
from os.path import join
from .Files import getWorkbenchFolder


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
        return join(
            getWorkbenchFolder(), "Resources", "Icons",
            (self.obj_name).lower() + ".svg"
        )

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None
