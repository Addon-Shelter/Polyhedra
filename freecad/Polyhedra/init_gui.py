
from os.path import join
from FreeCAD import Gui

from .Utils.Files import getWorkbenchFolder


translations = join(getWorkbenchFolder(),'Resources','Translations')

Gui.addLanguagePath(translations)

Gui.updateLocale()


import freecad.Polyhedra.Toolbar
