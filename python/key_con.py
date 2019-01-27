import car
from time import sleep
import sys
import tkinter as tk

def key_input(event):
	print('Key:', event.char)
	key_press = event.char
	sleep_time = 0.030
	if(key_press.lower() =='w'):
		car.move([1,0,0,0])
		sleep(0.03)
		command.bind('<KeyRelease-w>', car.allStop())
	elif(key_press.lower() == 'a'):
		car.move([1,0,1,0])
		sleep(1)
		command.bind('<KeyRelease-a>', car.allStop())
	elif(key_press.lower() == 'd'):
		car.move([1,0,0,1])
		sleep(1)
		command.bind('<KeyRelease-d>', car.allStop())

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
