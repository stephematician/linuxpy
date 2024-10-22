#
# This file is part of the linuxpy project
#
# Copyright (c) 2024 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

import pathlib

from linuxpy.codegen.base import CEnum, run

HEADERS = [
    "/usr/include/linux/gpio.h",
]


TEMPLATE = """\
#
# This file is part of the linuxpy project
#
# Copyright (c) 2024 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

# This file has been generated by {name}
# Date: {date}
# System: {system}
# Release: {release}
# Version: {version}

import enum

from linuxpy.ioctl import IOR as _IOR, IOW as _IOW, IOWR as _IOWR
from linuxpy.ctypes import u8, u16, u32, cuint, cint, cchar, culonglong
from linuxpy.ctypes import Struct, Union, POINTER, cvoidp


MAX_LINES = 64
MAX_ATTRS = 10


{enums_body}


{structs_body}


{iocs_body}"""


class IOC(CEnum):
    def __init__(self):
        def filter(name, value):
            return name.endswith("_IOCTL")

        super().__init__("IOC", ["GPIO_GET_", "GPIO_V2_"], filter=filter)

    def add_item(self, name, value):
        name = name.removesuffix("_IOCTL")
        return super().add_item(name, value)


# macros from #define statements
MACRO_ENUMS = [
    IOC(),
]


this_dir = pathlib.Path(__file__).parent


def decode_name(name: str) -> str:
    return name.removeprefix("gpio_v2_").removeprefix("gpio_")


def main(output=this_dir.parent / "gpio" / "raw.py"):
    run(__name__, HEADERS, TEMPLATE, MACRO_ENUMS, output=output, decode_enum_name=decode_name)


if __name__ == "__main__":
    main()