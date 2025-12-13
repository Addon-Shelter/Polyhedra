# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from typing import Callable


class DocumentSwitch:

    __callback : Callable

    def __init__ (
        self ,
        callback : Callable
    ):
        self.__callback = callback


    def slotCreatedDocument ( self , *_ ):
        self.__callback()

    def slotDeletedDocument ( self , *_ ):
        self.__callback()

    def slotRelabelDocument ( self , *_ ):
        self.__callback()

    def slotActivateDocument ( self , *_ ):
        self.__callback()