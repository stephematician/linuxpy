#
# This file is part of the python-linux project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

from linux.codegen import CEnum, run


HEADERS = [
    "/usr/include/linux/v4l2-common.h",
    "/usr/include/linux/v4l2-controls.h",
    "/usr/include/linux/videodev2.h",
    "/usr/include/linux/v4l2-mediabus.h",
    "/usr/include/linux/v4l2-dv-timings.h",
    "/usr/include/linux/v4l2-subdev.h",
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

from linux.ioctl import IO as _IO, IOR as _IOR, IOW as _IOW, IOWR as _IOWR 
from linux.ctypes import u8, i8, u16, i16, u32, i32, u64, i64, cuint, cint, cchar
from linux.ctypes import Struct, Union, POINTER, timeval, timespec
from linux.video.util import v4l2_fourcc, v4l2_fourcc_be

v4l2_std_id = u64

{enums_body}


{structs_body}


{iocs_body}"""


# macros from #define statements
MACRO_ENUMS = [
    CEnum("SelectionFlag", "V4L2_SEL_FLAG_", "IntFlag"),
    CEnum("SelectionTarget", "V4L2_SEL_TGT_"),
    CEnum("Capability", "V4L2_CAP_", "IntFlag"),
    CEnum("PixelFormat", "V4L2_PIX_FMT_"),
    CEnum("BufferFlag", "V4L2_BUF_FLAG_", "IntFlag"),
    CEnum("ImageFormatFlag", "V4L2_FMT_FLAG_", "IntFlag"),
    CEnum("InputStatus", "V4L2_IN_ST_", "IntFlag"),
    CEnum("InputType", "V4L2_INPUT_TYPE_"),
    CEnum("InputCapabilities", "V4L2_IN_CAP_", "IntFlag"),
    CEnum("ControlClass", "V4L2_CTRL_CLASS_"),
    CEnum("ControlID", "V4L2_CID_"),
    CEnum("ControlFlag", "V4L2_CTRL_FLAG_", "IntFlag"),
    CEnum("TimeCodeType", "V4L2_TC_TYPE_"),
    CEnum("TimeCodeFlag", "V4L2_TC_FLAG_", "IntFlag"),
    CEnum("EventType", "V4L2_EVENT_"),
    CEnum("EventSubscriptionFlag", "V4L2_EVENT_SUB_FL_", "IntFlag"),
    CEnum("IOC", "VIDIOC_"),
]


def main():
    run(__package__, HEADERS, TEMPLATE, MACRO_ENUMS)


if __name__ == "__main__":
    main()