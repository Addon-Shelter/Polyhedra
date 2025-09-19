
from PySide.QtCore import QTimer
from FreeCAD import Gui

import PartGui

print(dir(PartGui))


timer = QTimer()
timer.setSingleShot(True)

def extend ():

    global timer

    workbench = Gui.activeWorkbench()

    if not hasattr(workbench,'__Workbench__'):

        print('Not yet loaded')

        timer.start(1000)
        return

    if not hasattr(workbench,'name'):
        return

    name = workbench.name()

    if name != 'PartWorkbench':
        return


    list = [
        'Pyramid' ,
        'Tetrahedron' ,
        'Hexahedron' ,
        'Octahedron' ,
        'Dodecahedron' ,
        'Icosahedron' ,
        'Icosahedron-Truncated' ,
        'Geodesic-Sphere' ,
        'Regular-Solid'
    ]

    workbench.appendToolbar('Solids-Polyhedra',list)


timer.timeout.connect(extend)


window = Gui.getMainWindow()
window.workbenchActivated.connect(extend)
