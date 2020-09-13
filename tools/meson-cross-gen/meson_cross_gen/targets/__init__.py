__author__ = "Alexis Jeandet"
__copyright__ = "Copyright 2020, Laboratory of Plasma Physics"
__credits__ = []
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Alexis Jeandet"
__email__ = "alexis.jeandet@member.fsf.org"
__status__ = "Development"


class Target:
    name = ""
    family = ""
    sub_family = ""

    system = ''
    cpu_family = ''
    cpu = ''
    endian = ''

    c_args = []
    cpp_args = []
    c_link_args = []
    cpp_link_args = []
    compiler_prefix = ""

    constants = {}
    options = {}
    properties = {}

    def __repr__(self):
        return """
name:           {name}
family:         {family}
sub_family:     {sub_family}
c_args:         {c_args}
cpp_args:       {cpp_args}
c_link_args:    {c_link_args}
cpp_link_args:  {cpp_link_args}
""".format(**self.__dict__)


available_targets = {}


def register_target(name):
    def _reg(cls):
        available_targets[name] = cls
        return cls
    return _reg