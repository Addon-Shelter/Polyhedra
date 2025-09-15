
import os


def getWorkbenchFolder():
    return os.path.dirname(os.path.abspath(__file__))


icons_dir = os.path.join(getWorkbenchFolder(), '..',"Resources", "Icons")
