
# Based on examples at : https://www.freecadweb.org/wiki/Workbench_creation

# Version 01.08

# Version 01.02  (2020-01-15)
# added geodesic sphere

# version 01.03   (2020-01-23)
# added hexahedron  (cube)

# version 01.04  (2020-01-30)
# renamed Mod to Pyramids-and-Polyhedrons

# version 01.05  (2020-12-26)
# additional namechanges, no functional changes

# version 01.07a  (2020-12-30)
# flexibility for installation folder

# version 01.08   (2023-08-21)
# no printing of the workbenchfolders  (issue bij Alex Neufeld)


from os.path import join
from FreeCAD import Gui

from .Utils.Files import getWorkbenchFolder


translations = join(getWorkbenchFolder(),'Resources','Translations')

Gui.addLanguagePath(translations)

Gui.updateLocale()


import freecad.Polyhedra.Toolbar
