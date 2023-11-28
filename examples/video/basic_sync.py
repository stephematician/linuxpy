#
# This file is part of the linuxpy project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

import logging
import time

from linuxpy.video.device import Device


def main():
    fmt = "%(threadName)-10s %(asctime)-15s %(levelname)-5s %(name)s: %(message)s"
    logging.basicConfig(level="INFO", format=fmt)

    with Device.from_id(0) as stream:
        start = last = time.monotonic()
        last_update = 0
        for frame in stream:
            new = time.monotonic()
            fps, last = 1 / (new - last), new
            if new - last_update > 0.1:
                elapsed = new - start
                print(
                    f"frame {frame.frame_nb:04d} {len(frame)/1000:.1f} Kb at {fps:.1f} fps; {elapsed=:.2f} s;",
                    end="\r",
                )
                last_update = new


try:
    main()
except KeyboardInterrupt:
    logging.info("Ctrl-C pressed. Bailing out")
