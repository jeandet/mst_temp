from .. import register_target
from ..cortex_m import CortexM4


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
