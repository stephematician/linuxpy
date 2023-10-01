#
# This file is part of the python-linux project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

from .base import CEnum, run


HEADERS = [
    "/usr/include/linux/magic.h",
]


TEMPLATE = """\
#
# This file is part of the python-linux project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

# This file has been generated by {name}
# Date: {date}
# System: {system}
# Release: {release}
# Version: {version}

import enum


{enums_body}"""


class MagicEnum(CEnum):
    def __init__(self):
        super().__init__("Magic", "", filter=lambda name, _: "MAGIC_STRING" not in name)

    def add_item(self, name, value):
        name = name.replace("_MAGIC", "")
        return super().add_item(name, value)


# macros from #define statements
MACRO_ENUMS = [MagicEnum()]


def main():
    run(__package__, HEADERS, TEMPLATE, MACRO_ENUMS)


if __name__ == "__main__":
    main()