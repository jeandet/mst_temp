_cpu_srcs = files([
    'f4/specific_interrupt_vector_table.c',
    '../CortexM/startup.c',
    '../CortexM/interrupt_handlers.c',
    '../CortexM/interrupt_vector_table.c',
    '../cross/syscalls.c'
])

mst_cpu_dep = declare_dependency(sources:_cpu_srcs)
