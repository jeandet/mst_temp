from meson_cross_gen.targets import Target
from meson_cross_gen.compilers import Compiler

HOST_MACHINE_TEMPLATE = """
system = {system}
cpu_family = {cpu_family}
cpu = {cpu}
endian = {endian}
"""

PROPERTIES_TEMPLATE = """
c_args  = {c_args}
cpp_args = {cpp_args}

c_link_args = {c_link_args}
cpp_link_args = {cpp_link_args}

{extra_properties}
"""

BINARIES_TEMPLATE = """
c = {c}
cpp = {cpp}
{others}
"""

CROSS_TEMPLATE = """
[project options]
{options}

[constants]
{constants}

[properties]
{properties}

[host_machine]
{host_machine}

[binaries]
{binaries}
"""


def _dict_to_ini(d: dict):
    return "\n".join(
        [f"{key} = '{value}'" for key, value in d.items()]
    )


def _generate_constants(target: Target):
    return _dict_to_ini( target.constants)


def _generate_options(target: Target):
    return _dict_to_ini( target.options)


def _generate_properties(target: Target):
    return PROPERTIES_TEMPLATE.format(
        c_args=target.c_args,
        cpp_args=target.cpp_args,

        c_link_args=target.c_link_args,
        cpp_link_args=target.cpp_link_args,

        extra_properties=_dict_to_ini(target.properties)
    )


def _generate_host_machine(target: Target):
    return HOST_MACHINE_TEMPLATE.format(
        system=f"'{target.system}'",
        cpu_family=f"'{target.cpu_family}'",
        cpu=f"'{target.cpu}'",
        endian=f"'{target.endian}'"
    )


def _generate_binaries(compiler: Compiler):
    return BINARIES_TEMPLATE.format(
        c=f"'{compiler.c_compiler}'",
        cpp=f"'{compiler.cxx_compiler}'",
        others="\n".join([f"{name} = '{exe}'" for name, exe in compiler.others.items()])
    )


def generate_cross_file(target: Target, compiler: Compiler):
    return CROSS_TEMPLATE.format(
        options=_generate_options(target),
        constants=_generate_constants(target),
        properties=_generate_properties(target),
        host_machine=_generate_host_machine(target),
        binaries=_generate_binaries(compiler)
    )
