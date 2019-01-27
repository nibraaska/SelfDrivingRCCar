# SelfDrivingRCCar

This repository was created for the 2019 MTSU hackathon. The goal is to create an autonomous RC car using a supervised end to end learning approach with a convolutional neural network.


An [Android application](https://github.com/JZDesign/SelfDrivingRCCar) was created (with the help of our lovey mentor: Jacob Rakidzich) to interface with a raspberry pi, sending data for wheel displacement and throttle.
### 
# About the files:
## ml/
This directory includes the code written in Jupyter Notebook for our CNN model and its data preprocessing

## python/
This directory includes the scripts running on the raspberry pi used to control the RC car and communication with the Android Application.



### Technical Notes:
Machine Learning:
                The convolutional neural network was written in python using Jupyter Notebook. We decided on our CNN layers to be: 1 Conv2d, 1 max pooling, and 1 dense layer. Our camera (attached to the pi) grabs a frame every time a command is sent from the Android application. Our model is meant to associate the pixel array with decisions (forward,reverse,left,right).
                
Controlling the pi:

The pi receives input over a socket set up on the pi that correlated to a command (forward,reverse,left right).
                
# Bumps and Bruises:
## The app:
While we initially intended to control the pi using an Android application, we ran into issues with hosting multiple projects in the same GIT repository, because of this we adapted by making directories for each. In that process the Android application files were disorganized. This resulted in multiple building issues for the project, prompting the need of a new repository for the Android application. In the meantime, we adapted by sending commands to the pi through a SSH connection using W,S,A,D to control forward,reverse,left,right.

## The Hardware
### Power
Over the course of the project, we ran into two power supply issues. 1. The battery to power the motors in the rc car was very small (500mah) and died very often. This resulted in us being more diligent with our time in planning the code writing/testing
2. The pi needed a power supply that our power banks couldn't provide. This prompted a midnight trip to walmart to get the power banks needed.

### Turning
Near the end of the project, our servo that controlled the turns was no longer able to function properly. This meant that we could no longer perform the turns needed to run our course. To adapt we decided to change our course to be a straight track. Instead of our CNN outputting wheel displacement,, we had it output the command to stop if a specific node is detected on its path. Without the RC car having brakes, we had to improvise by using the reverse command for a small amount of time in order to stop. 


# THE TEAM
Josiah Rininger 
Nibraas Khan
Michael McComas
Arif Bashar
Elijah Dangerfield
George Boktor
Dylan Spies
