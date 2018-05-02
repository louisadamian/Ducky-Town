# Import the device reading library
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from evdev import InputDevice, categorize, ecodes, KeyEvent, list_devices
from picamera import PiCamera
from time import sleep
import driveworking as drive
import atexit
from multiprocessing import Process, Queue
import os

<<<<<<< HEAD:Working/driveRCCameraworking.py
=======
def map(x, in_min, in_max, out_min, out_max):
     return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Get the name of the Logitech Device


>>>>>>> master:driveRCCamera.py
def getInputDeviceByName(name):
  devices = [InputDevice(fn) for fn in list_devices()]
  for device in devices:
    if device.name == name:
      return InputDevice(device.fn)
  return None

# Import our gamepad.
gamepad = getInputDeviceByName('Logitech Gamepad F710')
camera = PiCamera()


<<<<<<< HEAD:Working/driveRCCameraworking.py

mh = Adafruit_MotorHAT(addr=0x60)
lmotor = mh.getMotor(1)
rmotor = mh.getMotor(2)

def scaleMap (value, value_low, value_high, map_low, map_high):
    return (float(value) - value_low) * (map_high - map_low) / (value_high - value_low) + map_low

def motorProcess (q):
  while True:
    msg = None
    while not q.empty():
      msg = q.get()
    if msg == None:
      continue
    elif msg[0] == None and msg [1] == None and msg[2] == None and msg[3] == None:
      return
    else:
      throttle_percent, right_percent, left_percent, direction = msg[0], msg[1], msg[2], msg[3]
      drive.runMotor(lmotor,throttle_percent*left_percent*255, direction)
      drive.runMotor(rmotor,throttle_percent*right_percent*255, direction)


def gamepadProcess():
  current_image_number = 0
  current_video_number = 0
  is_recording = False
  throttle_percent = 0.0
  left_percent = 0.0
  right_percent = 0.0
  direction = True
  for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
      keyevent = categorize(event)
      if keyevent.keystate == KeyEvent.key_down:
        print(keyevent.keycode)
        # example key detection code
        if 'BTN_A' in keyevent.keycode:
          # Do something here when the A button is pressed
          if is_recording == False:
            print("recoring started")
            camera.start_preview()
            camera.start_recording('/home/nuvustudent/Desktop/Videos/video%s.h264' % current_video_number)
            is_recording = True
          else:
            print("recording ending")
            camera.stop_recording()
            camera.stop_preview()
            is_recording = False
            current_video_number += 1
        elif 'BTN_B' in keyevent.keycode:
          # Do something here when the B button is pressed
          camera.capture('/home/nuvustudent/Desktop/Images/image%s.jpg' % current_image_number)
          current_image_number += 1
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
        if event.value > 0:
          direction = False
        else:
          direction = True
        print("REVERSE")
      elif event.code == 3:
        print('JOY_LR '+str(event.value))
        if event.value < 0:
          right_percent = 1.0
          left_percent = scaleMap(event.value,0,-32770,1,0)
        elif event.value > 0:
          left_percent = 1.0
          right_percent = scaleMap(event.value,0,32770,1,0)
      elif event.code == 4:
        print('JOY_UD '+str(event.value))
      elif event.code == 5:
        print('TRIG_R '+str(event.value))
        throttle_percent = scaleMap(event.value,0,255,0,1)
      elif event.code == 16:
        print('HAT_LR '+str(event.value))
      elif event.code == 17:
        print('HAT_UD '+str(event.value))
      else:
        pass
    q.put([throttle_percent,right_percent,left_percent,direction])


# Create a queue for communication between the GamePad and the motorProcess. 
q = Queue()
# Create a Process that runs the motors, give it the queue.
p = Process(target=motorProcess, args=(q,))
# Start the motorPorcess
p.start()

# Ensure the motorProcess joins and the motors turn off.
def exitFunction():
  # Send a sign to the motorProcess to end
  q.put([None,None,None,None])
  # Wait for the motor process to end
  p.join()
  # Kill all the motors
  drive.turnOffMotors()
# Register the exitFunction() to be called when this Python script ends.
atexit.register(exitFunction)

# Call the Gamepad Process function which runs forever (until Ctrl+C is entered)
gamepadProcess()
  
=======
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
        camera.start_recording('/home/nuvustudent/Desktop/Videos/video%s.h264' % current_video_number)
        sleep(10)
        camera.stop_recording()
        camera.stop_preview
        current_video_number += 1
        pass
      elif 'BTN_B' in keyevent.keycode:
        # Do something here when the B button is pressed
        camera.capture('/home/nuvustudent/Desktop/Images/image%s.jpg' % current_image_number)
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
      map(event.value, 0, 255, -100, 100)

    elif event.code == 4:
      print('JOY_UD '+str(event.value))
    elif event.code == 5:
        map(event.value, 0, 255, 0, 32767)
      print('TRIG_R '+str(event.value))
    elif event.code == 16:
      print('HAT_LR '+str(event.value))
    elif event.code == 17:
      print('HAT_UD '+str(event.value))
    else:
      pass
>>>>>>> master:driveRCCamera.py
