from .. import register_target
from ..cortex_m import CortexM4
from ...common import MST_SRC_ROOT


@register_target("stm32f4")
class Stm32f4(CortexM4):
    def __init__(self):
        super().__init__()
        self.family = "STM32"
        self.sub_family = "STM32F4"
        self.name = "stm32f4"
        common_args = ["-DSTM32", "-DSTM32F4"]
        self.c_args += common_args
        self.cpp_args += common_args
        common_link_args = ['-L'+MST_SRC_ROOT + 'cpu/stm32/f4', '-Tstm32f429.ld']
        self.c_link_args += common_link_args
        self.cpp_link_args += common_link_args
        self.options["cpu_dir"] = "stm32"
