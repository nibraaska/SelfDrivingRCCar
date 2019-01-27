import car
import camera
from time import sleep
import sys
import tkinter as tk

x = 0
f = open("/home/pi/Documents/decisions.txt", 'w+')
def key_input(event):
	global x
	global f
	print('Key:', event.char)
	key_press = event.char
	sleep_time = 0.030
	if(key_press.lower() =='w'):
		#car.move([1,0,0,0])
		sleep(sleep_time)
		camera.pic(x)
		f.write("1000\n")
		command.bind('<KeyRelease-w>', car.allStop())
	elif(key_press.lower() == 'a'):
		#car.move([1,0,1,0])
		sleep(sleep_time)
		camera.pic(x)
		f.write("1010\n")
		command.bind('<KeyRelease-a>', car.allStop())
	elif(key_press.lower() == 'd'):
		#car.move([1,0,0,1])
		sleep(sleep_time)
		camera.pic(x)
		f.write("1001\n")
		command.bind('<KeyRelease-d>', car.allStop())
	x += 1

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
f.close()
