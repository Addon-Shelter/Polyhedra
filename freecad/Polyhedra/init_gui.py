# ***************************************************************************
# *   Copyright (c) 2019  Eddy Verlinden , Genk Belgium   (eddyverl)        *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

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
from .Commands import registerCommands
from .Toolbar import extendToolbar


translations = join(getWorkbenchFolder(),'Resources','Translations')

Gui.addLanguagePath(translations)

Gui.updateLocale()

registerCommands()

extendToolbar()
