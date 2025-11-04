# SPDX-License-Identifier: GPL-3.0-or-later

from os.path import join
from FreeCAD import Gui

import freecad.Polyhedra.Migration


from .Utils.Files import getWorkbenchFolder

translations = join(getWorkbenchFolder(),'Resources','Translations')

Gui.addLanguagePath(translations)

Gui.updateLocale()


import freecad.Polyhedra.Toolbar
