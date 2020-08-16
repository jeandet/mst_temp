from . import Target


class CortexM4(Target):
    def __init__(self):
        common_args = ["-mcpu=cortex-m4", "-mfloat-abi=hard", "-mfpu=fpv4-sp-d16", "-flto", "-ffunction-sections", "-fdata-sections"]
        link_args = ["-Wl,--gc-sections", "-Wl,-Map,output.map"]
        self.c_args += common_args
        self.cpp_args += common_args + ["-fno-use-cxa-atexit"]
        self.c_link_args += common_args + link_args
        self.cpp_link_args += common_args + link_args
        self.compiler_prefix = "arm-none-eabi-"

        self.system = 'bare-metal'
        self.cpu_family = 'arm'
        self.cpu = 'cortex-m4'
        self.endian = 'little'

