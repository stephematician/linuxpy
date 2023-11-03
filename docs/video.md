# Video

Video for Linux 2 (V4L2).

Without further ado:

```python
>>> from linuxpy.video.device import Device
>>> with Device.from_id(0) as cam:
>>>     for i, frame in enumerate(cam):
...         print(f"frame #{i}: {len(frame)} bytes")
...         if i > 9:
...             break
...
frame #0: 54630 bytes
frame #1: 50184 bytes
frame #2: 44054 bytes
frame #3: 42822 bytes
frame #4: 42116 bytes
frame #5: 41868 bytes
frame #6: 41322 bytes
frame #7: 40896 bytes
frame #8: 40844 bytes
frame #9: 40714 bytes
frame #10: 40662 bytes
```

Getting information about the device:

```python
>>> from linuxpy.video.device import Device, BufferType

>>> cam = Device.from_id(0)
>>> cam.open()
>>> cam.info.card
'Integrated_Webcam_HD: Integrate'

>>> cam.info.capabilities
<Capability.STREAMING|EXT_PIX_FORMAT|VIDEO_CAPTURE: 69206017>

>>> cam.info.formats
[ImageFormat(type=<BufferType.VIDEO_CAPTURE: 1>, description=b'Motion-JPEG',
             flags=<ImageFormatFlag.COMPRESSED: 1>, pixelformat=<PixelFormat.MJPEG: 1196444237>),
 ImageFormat(type=<BufferType.VIDEO_CAPTURE: 1>, description=b'YUYV 4:2:2',
             flags=<ImageFormatFlag.0: 0>, pixelformat=<PixelFormat.YUYV: 1448695129>)]

>>> cam.get_format(BufferType.VIDEO_CAPTURE)
Format(width=640, height=480, pixelformat=<PixelFormat.MJPEG: 1196444237>}

>>> for ctrl in cam.controls.values(): print(ctrl)
<IntegerControl brightness min=0 max=255 step=1 default=128 value=128>
<IntegerControl contrast min=0 max=255 step=1 default=32 value=32>
<IntegerControl saturation min=0 max=100 step=1 default=64 value=64>
<IntegerControl hue min=-180 max=180 step=1 default=0 value=0>
<BooleanControl white_balance_automatic default=True value=True>
<IntegerControl gamma min=90 max=150 step=1 default=120 value=120>
<MenuControl power_line_frequency default=1 value=1>
<IntegerControl white_balance_temperature min=2800 max=6500 step=1 default=4000 value=4000 flags=inactive>
<IntegerControl sharpness min=0 max=7 step=1 default=2 value=2>
<IntegerControl backlight_compensation min=0 max=2 step=1 default=1 value=1>
<MenuControl auto_exposure default=3 value=3>
<IntegerControl exposure_time_absolute min=4 max=1250 step=1 default=156 value=156 flags=inactive>
<BooleanControl exposure_dynamic_framerate default=False value=False>

>>> cam.controls["saturation"]
<IntegerControl saturation min=0 max=100 step=1 default=64 value=64>

>>> cam.controls["saturation"].id
9963778
>>> cam.controls[9963778]
<IntegerControl saturation min=0 max=100 step=1 default=64 value=64>

>>> cam.controls.brightness
<IntegerControl brightness min=0 max=255 step=1 default=128 value=128>
>>> cam.controls.brightness.value = 64
>>> cam.controls.brightness
<IntegerControl brightness min=0 max=255 step=1 default=128 value=64>
```

(see also [v4l2py-ctl](examples/video/v4l2py-ctl.py) example)

## asyncio

linuxpy.video is asyncio friendly:

```bash
$ python -m asyncio

>>> from linuxpy.video.device import Device
>>> with Device.from_id(0) as camera:
...     async for frame in camera:
...         print(f"frame {len(frame)}")
frame 10224
frame 10304
frame 10224
frame 10136
...
```

(check [basic async](examples/video/basic_async.py) and [web async](examples/video/web/async.py) examples)

## gevent

linuxpy.video is also gevent friendly:

```
$ python

>>> from linuxpy.io import GeventIO
>>> from linuxpy.video.device import Device
>>> with Device.from_id(0, io=GeventIO) as camera:
...     for frame in camera:
...         print(f"frame {len(frame)}")
frame 10224
frame 10304
frame 10224
frame 10136
...
```

(check [basic gevent](examples/basic_gevent.py) and [web gevent](examples/web/sync.py) examples)

## Video output

It is possible to write to a video output capable device (ex: v4l2loopback).
The following example shows how to grab frames from device 0 and write them
to device 10

```bash
>>> from linuxpy.video.device import Device, VideoOutput, BufferType
>>> dev_source = Device.from_id(0)
>>> dev_sink = Device.from_id(10)
>>> with dev_source, dev_target:
>>>     source = VideoCapture(dev_source)
>>>     sink = VideoOutput(dev_sink)
>>>     source.set_format(640, 480, "MJPG")
>>>     sink.set_format(640, 480, "MJPG")
>>>     with source, sink:
>>>         for frame in source:
>>>             sink.write(frame.data)
```

## v4l2loopback

Start from scratch:
```bash
# Remove kernel module and all devices (no client can be connected at this point)
sudo modprobe -r v4l2loopback

# Install some devices
sudo modprobe v4l2loopback video_nr=20,21 card_label="Loopback 0","Loopback 1"
```

## References

See the ``linux/videodev2.h`` header file for details.


* [V4L2 (Latest)](https://www.kernel.org/doc/html/latest/userspace-api/media/v4l/v4l2.html) ([videodev.h](https://www.kernel.org/doc/html/latest/userspace-api/media/v4l/videodev.html))
* [V4L2 6.2](https://www.kernel.org/doc/html/v6.2/userspace-api/media/v4l/v4l2.html) ([videodev.h](https://www.kernel.org/doc/html/v6.2/userspace-api/media/v4l/videodev.html))