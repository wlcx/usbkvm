import sys
import time
import itertools

sys.path.append("../app/build")
import usbkvm_py as usbkvm

d=usbkvm.Device("USBKVM")

seq = [usbkvm.Led.NONE, usbkvm.Led.USB, usbkvm.Led.HID, usbkvm.Led.HDMI]

for led in itertools.cycle(seq) :
	d.set_led(usbkvm.Led.ALL, led)
	time.sleep(.5)