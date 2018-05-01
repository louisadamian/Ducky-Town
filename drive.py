#!/usr/bin/python
# Import Adafruit Motor HAT Library
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
# Import additional libraries that support MotorHAT
import time
import atexit

# create a default MotorHAT object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
lmotor = mh.getMotor(1)
rmotor = mh.getMotor(2)

def turnOffMotors():
  mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def scaleMap (value, value_low, value_high, map_low, map_high):
    return (float(value) - value_low) * (map_high - map_low) / (value_high - value_low) + map_low

def drive(speed):
    runMotor(lmotor,speed)
    runMotor(rmotor,speed)

def drive(speed, turn):
    tVal = turn/2
    runMotor(lmotor, speed* tVal)
    runMotor(rmotor, speed*(-tVal))

# Complete this function so:
# 1. values in the range 1 to 32768 make the motor spin forward faster and faster.
# 2. values in the range -1 to -32768 make the motor spin backward faster and faster.
# 3. any value equal to 0 makes the motor BRAKE.
# 4. any values less than -32768 and greater than 32768 are rejected.
def runMotor(motor, speed):
	motor.setSpeed(speed)
	motor.run(Adafruit_MotorHAT.BACKWARD)
while(True):
	runMotor(lmotor,32767)
	runMotor(rmotor,32767)
