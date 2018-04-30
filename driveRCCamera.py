
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import the device reading library
from evdev import InputDevice, categorize, ecodes, KeyEvent, list_devices
from picamera import PiCamera
from time import sleep


# Get the name of the Logitech Device
def getInputDeviceByName(name):
  devices = [InputDevice(fn) for fn in list_devices()]
  for device in devices:
    if device.name == name:
      return InputDevice(device.fn)
  return None

# Import our gamepad.
gamepad = getInputDeviceByName('Logitech Gamepad F710')
camera = PiCamera()

current_image_number = 0
current_video_number = 0

# Loop over the gamepad's inputs, reading it.
for event in gamepad.read_loop():
  if event.type == ecodes.EV_KEY:
    keyevent = categorize(event)
    if keyevent.keystate == KeyEvent.key_down:
      print(keyevent.keycode)
      # example key detection code
      if 'BTN_A' in keyevent.keycode:
        # Do something here when the A button is pressed
        camera.start_preview()
        camera.start_recording('/home/pi/Desktop/videos/video%s.h264' % current_video_number)
        sleep(10)
        camera.stop_recording()
        camera.stop_preview
        current_video_number += 1
        pass
      elif 'BTN_B' in keyevent.keycode:
        # Do something here when the B button is pressed
        camera.capture('/home/pi/Desktop/images/image%s.jpg' % current_image_number)
        current_image_number += 1
        pass
      elif 'BTN_START' in keyevent.keycode:
        # Do something here when the START button is pressed
        pass
  elif event.type == ecodes.EV_ABS:
    if event.code == 0:
      print('PAD_LR '+str(event.value))
    elif event.code == 1:
      print('PAD_UD '+str(event.value))
    elif event.code == 2:
      print('TRIG_L '+str(event.value))
    elif event.code == 3:
      print('JOY_LR '+str(event.value))
    elif event.code == 4:
      print('JOY_UD '+str(event.value))
    elif event.code == 5:
      print('TRIG_R '+str(event.value))
    elif event.code == 16:
      print('HAT_LR '+str(event.value))
    elif event.code == 17:
      print('HAT_UD '+str(event.value))
    else:
      pass

