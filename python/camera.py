import picamera
#import carcopy
import numpy as np
from time import sleep

def pic():
	with picamera.PiCamera() as camera:
		camera.resolution = (64, 64)
		camera.framerate = 24
		output = np.empty((64,64,3), dtype=np.uint8)
		camera.capture(output, 'rgb')
		arr = np.dot(output[...,:3], [0.299, 0.587, 0.114])
		arr = (arr / 255.0) + 0.01
		np.savetxt('test.txt', arr.reshape(1, 4096), delimiter=',', fmt='%1g')
f = open('test.txt', 'w')
pic()

