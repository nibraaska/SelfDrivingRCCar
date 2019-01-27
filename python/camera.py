import picamera
#import carcopy
import numpy as np
from time import sleep

def pic(x):
	with picamera.PiCamera() as camera:
		camera.resolution = (128, 128)
		camera.capture('/home/pi/Pictures/image' + str(x) + '.png')

