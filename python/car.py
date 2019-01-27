from gpiozero import PWMOutputDevice
from time import sleep
 
#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 13	# IN1 - Left Drive
PWM_REVERSE_RIGHT_PIN = 6	# IN2 - Right Drive
 
# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)
 
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)
 

def move(one_hot):
#	if(one_hot[0]==1):
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	if(one_hot[2]==1):
		forwardRight.value = 1
	if(one_hot[3]==1):
		reverseRight.value = 1

 
def allStop():
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0
 
def forwardDrive():
	forwardLeft.value = 1
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0
 
def forwardTurnLeft():
	forwardLeft.value = 0.2
	reverseLeft.value = 0
	forwardRight.value = 1.0
	reverseRight.value = 0
 
def forwardTurnRight():
	forwardLeft.value = 0.2
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 1.0

def reverse():
        forwardLeft.value=0
        reverseLeft.value=0.2
        forwardRight.value = 0
        reverseRight.value = 0
        
def main():
	allStop()
	forwardDrive()
	sleep(5)
	forwardTurnLeft()
	sleep(5)
	forwardTurnRight()
	sleep(5)
	allStop()
 
 
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
