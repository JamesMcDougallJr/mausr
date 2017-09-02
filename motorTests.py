

import time
import RPi.GPIO as GPIO
from motor import setupMotor,runall,stop,left,right


setupMotor()
stop()
runall()
time.sleep(5)
stop()
