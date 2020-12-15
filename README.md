# cat_feeder
A simple cat feeder using a Raspberry Pi Zero and coded in Python.
Requires a HX711 sensor and servo motor.

Servo should be pinned out to:

Black – comes to GND (pin 6) from the Pi
Red – comes to 3V3 (pin 1) from the Pi
Yellow/Orange – to a free GPIO pin (e.g., GPIO17, pin 11)

Load cell to HX711:

RED: E+
BLACK:E-
WHITE : A+
GREEN: A-

HX711 to PI:

GND : PIN 25 (GROUND)
DT : PIN 21 (BCM GPIO9)
SCK : PIN 23 (BCM GPIO11)
VCC: PIN 1 (3.3V)

https://www.raspberrypi.org/documentation/usage/gpio/
http://wiki.hivetool.org/Interface_the_HX711_to_Pi
https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/
