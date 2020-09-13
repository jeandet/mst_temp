__author__ = "Alexis Jeandet"
__copyright__ = "Copyright 2020, Laboratory of Plasma Physics"
__credits__ = []
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Alexis Jeandet"
__email__ = "alexis.jeandet@member.fsf.org"
__status__ = "Development"

import importlib, os


class Compiler:
    name = ""
    c_compiler = ""
    cxx_compiler = ""
    c_linker = ""
    cxx_linker = ""
    others = {}

    def __repr__(self):
        return """
name:           {name}
C compiler:     {c_compiler}
C++ compiler:   {cxx_compiler}
C linker:       {c_linker}
C++ linker:     {cxx_linker}
others:         {others}
""".format(**self.__dict__)


def _make_exe(exe, prefix, path):
    if path != "":
        return f"{path}/{prefix}{exe}"
    return f"{prefix}{exe}"


class Gcc(Compiler):
    def __init__(self, prefix="", path=""):
        self.name = "GCC"
        self.c_compiler = _make_exe("gcc", prefix, path)
        self.cxx_compiler = _make_exe("g++", prefix, path)
        self.c_linker = _make_exe("gcc", prefix, path)
        self.cxx_linker = _make_exe("g++", prefix, path)
        self.others = {key: _make_exe(key, prefix, path) for key in
                       ["ar", "as", "ld", "strip", "objcopy", "objdump", "size", "gcov", "gdb"]}


available_compilers = {"gcc": Gcc}
