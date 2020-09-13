#!/usr/bin/env python3

__author__ = "Alexis Jeandet"
__copyright__ = "Copyright 2020, Laboratory of Plasma Physics"
__credits__ = []
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Alexis Jeandet"
__email__ = "alexis.jeandet@member.fsf.org"
__status__ = "Development"


import argparse
from meson_cross_gen.targets import target_loader, available_targets
from meson_cross_gen.compilers import available_compilers
from meson_cross_gen.cross_file import generate_cross_file


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list-targets", help="List supported targets", action="store_true")
parser.add_argument("-t", "--target", help="Set target", default='stm32f4')
parser.add_argument("-c", "--compiler", help="Set compiler", default='gcc')
args = parser.parse_args()

target_loader.scan_for_targets()

if __name__ == '__main__':
    if args.list_targets:
        print(available_targets)
    else:
        if args.target not in available_targets:
            raise ValueError(f"Unknown target, available targets are:\n{list(available_targets.keys())}")

        if args.compiler not in available_compilers:
            raise ValueError(f"Unknown compiler, available compilers are:\n{list(available_compilers.keys())}")

        target = available_targets[args.target]()
        compiler = available_compilers[args.compiler](target.compiler_prefix)
        print(generate_cross_file(target, compiler))
