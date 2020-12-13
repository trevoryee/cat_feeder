# cat_feeder
A simple cat feeder using a Raspberry Pi Zero and coded in Python.
Requires a HX711 sensor and servo motor.

Servo should be pinned out to:
Black – comes to GND (pin 6) from the Pi
Red – comes to 3V3 (pin 1) from the Pi
Yellow/Orange – to a free GPIO pin (e.g., GPIO17, pin 11)

HX711 should be pinned out to:
VCC to Raspberry Pi Pin 2 (5V)
GND to Raspberry Pi Pin 6 (GND)
DT to Raspberry Pi Pin 29 (GPIO 5)
SCK to Raspberry Pi Pin 31 (GPIO 6)

This code needs to be uploaded into a .py file still. @!/usr/bin/python3

#importing required modules
import RPi.GPIO as GPIO
import time
from hx711 import hx711

#setup GPIO
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(HX711, GPIO.INPUT)
#

# setup HX711 sensor
try:
	hx = HX711 (dout_pin=21, pd_sck_pin=20)
if err:
        raise ValueError('Tare is unsuccessful.')
reading = hx.get_raw_data_mean()
if reading:
	print('Data subtracted by offset, not in units, but is reading as')
else:
	 print('invalid data', reading)
#

# servo angle set function
p = GPIO.PWM(servoPIN, 50)
def SetAngle(angle)
	duty = angle / 18 + 2
	GPIO.output(servoPIN, True)
	p.ChangeDutyCycle(duty)
	sleep(2)
	GPIO.output(servoPIN, False)
	p.ChangeDutyCycle(0)

SetAngle(90)
SetAngle(-90)
pwm.stop()
GPIO.cleanup()
#
