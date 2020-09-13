from . import Target
from ..common import MST_SRC_ROOT

class CortexM4(Target):
    def __init__(self):
        common_args = ["-mcpu=cortex-m4", "-mfloat-abi=hard", "-mfpu=fpv4-sp-d16", "-ffunction-sections", "-fdata-sections", "-nostartfiles", "--specs=nano.specs"]
        link_args = ["-Wl,--gc-sections", "-Wl,-Map,output.map"]
        self.c_args += common_args
        self.cpp_args += common_args + ["-fno-use-cxa-atexit", "-fno-exceptions"]
        self.c_link_args += common_args + link_args
        self.cpp_link_args += common_args + link_args + ["-fno-use-cxa-atexit", "-fno-exceptions"]
        self.compiler_prefix = "arm-none-eabi-"
        common_link_args = ['-L' + MST_SRC_ROOT + 'cpu/CortexM']
        self.c_link_args += common_link_args
        self.cpp_link_args += common_link_args

        self.system = 'bare-metal'
        self.cpu_family = 'arm'
        self.cpu = 'cortex-m4'
        self.endian = 'little'

