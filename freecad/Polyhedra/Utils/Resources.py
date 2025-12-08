# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

import freecad.Polyhedra as module
from importlib import resources


icons = resources.files(module) / 'Resources/Icons'


def icon ( name : str ):

    file = name + '.svg'

    icon = icons / file

    with resources.as_file(icon) as path:
        return str( path )