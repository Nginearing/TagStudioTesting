# I know this isn't at all a "macro wrapper" but idk

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
import logging
import importlib
import os

macros_folder = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'modals', 'macros'))

def LoadMacros(menu_bar, macros_menu):
    "Loads and adds macros to the Macro Menubar"
    for filename in os.listdir(macros_folder):
        if filename.endswith(".py"):
            try:
                module_name = filename[:-3]
                logging.info("[MACROS] Loading macro: " + filename + "...")
                module_path = os.path.join(macros_folder, filename)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module) 
                macro = QAction(module.ActionName, menu_bar)
                macro.triggered.connect(module.MacroAction)
                macros_menu.addAction(macro)
                logging.info("[MACROS] "+ module.ActionName + ": Successfully loaded")
            except:
                logging.error("[MACROS] "+ module.ActionName + ": Failed to load")
                return
    logging.info("[MACROS] All macros have been successfully loaded")
