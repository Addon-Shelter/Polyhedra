# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from .Utils.Resources import paths
from FreeCAD import Gui

import freecad.Polyhedra.Migration


Gui.addLanguagePath(paths[ 'translations' ])

Gui.updateLocale()


import freecad.Polyhedra.Toolbar
