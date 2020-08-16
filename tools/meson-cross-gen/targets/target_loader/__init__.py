__author__ = "Alexis Jeandet"
__copyright__ = "Copyright 2020, Laboratory of Plasma Physics"
__credits__ = []
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Alexis Jeandet"
__email__ = "alexis.jeandet@member.fsf.org"
__status__ = "Development"

import importlib, os
from ..targets.stm32 import *


def _scan_for_targets():
    target_dir = os.path.dirname(os.path.realpath(__file__)) + "/../targets"
    modules_files = [f for f in os.listdir(target_dir) if f[-3:] == '.py' and f != '__init__.py']
    for m_file in modules_files:
        mod = importlib.import_module( "targets.targets." + m_file[:-3], "")


_scan_for_targets()
