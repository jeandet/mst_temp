project('mst', ['c', 'cpp'],default_options : ['cpp_std=c++2a'], license: 'GPL3', version: '0.0.1', meson_version: '>=0.55.99')

CPU_DIR = get_option('cpu_dir')

message('Using CPU dir: ' + CPU_DIR)
subdir('cpu/'+CPU_DIR)

executable('get_flags', 'examples/main.cpp', dependencies: mst_cpu_dep)

