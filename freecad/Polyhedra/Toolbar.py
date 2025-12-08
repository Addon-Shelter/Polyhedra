# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from .PySide.QtWidgets import QMainWindow , QToolBar
from .PySide.QtCore import QTimer

from .Utils.Document import DocumentSwitch
from .Commands import registerCommands

from FreeCAD import Gui , Qt , addDocumentObserver


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP

title = QT_TRANSLATE_NOOP('Toolbar','Polyhedra')


toolbar = None


timer = QTimer()
timer.setSingleShot(True)

def insertToolbar ():

    visible = isPartActive()

    global toolbar

    window : QMainWindow = Gui.getMainWindow()

    if not window:
        return

    if not toolbar:

        toolbar = QToolBar(title)
        toolbar.setToolTip('Tooltip')
        toolbar.setObjectName('Solids-Polyhedra')

        registerCommands(toolbar)

        toolbar.setEnabled(False)
        window.addToolBar(toolbar)

    toolbar.setVisible(visible)


def isPartActive ():

    global timer

    workbench = Gui.activeWorkbench()

    if not workbench:
        return False

    if not hasattr(workbench,'__Workbench__'):
        timer.start(100)
        return False

    name = workbench.name()

    return name == 'PartWorkbench'


timer.timeout.connect(insertToolbar)



window = Gui.getMainWindow()
window.workbenchActivated.connect(insertToolbar)


from FreeCAD import activeDocument


def update ():

    global toolbar

    if not toolbar:
        return

    enabled = not not activeDocument()

    toolbar.setEnabled(enabled)


observer = DocumentSwitch(update)

addDocumentObserver(observer)