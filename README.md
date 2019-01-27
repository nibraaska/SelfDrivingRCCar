# SelfDrivingRCCar

This repository was created for the 2019 MTSU hackathon. The goal is to create an autonomous RC car using an supervised end to end learning apporach with a convolutional neural network


An [Android application](https://github.com/JZDesign/SelfDrivingRCCar) was created (with the help of our lovey mentor: Jacob Rakidzich) to interface with a raspberry pi, sending data for wheel displacement and throttle
### 
# About the files:
## ml/
This directory includes the code written un Jupyter Noteboook for our CNN and data preprocessing

## python/
This directory includes the scripts running on the raspberry pi used to control the RC car and communication with the Android Application



### Technical Notes:
Machine Learning:
                The convolutional neural network was written in python using Jupyter Labs. We decided on using one layer as similar projects found success with the same. Our camera (attached to the pi) grabs a frame every time a command is sent from the Android application. Our model is meant to accociate frames with decisions (forward,reverse,left,right)
                
Controlling the pi:

                The pi recives input over a soccet set up on the pi that correlated to a command (forward,reverse,left right)
                
# Bumps and Bruises:
## The app:
While we initially intended to conrol the pi using an Android application, we ran into issues with hosting multiple projects in the same GIT repository, because of this we adapted by making directories for each. In that process the Android application files were disorganized. This resulted in multiple building issues for the project, prompting the need for a new repository. In the mean time we adapted by sending commands to the pi through an SSH using W,S,A,D to control forward,reverse,left,right

## The Hardware
### Power
Over the course of the project we ran in to two power supply issues. 1. The battery to power the motors in the rc car was very small (500mah) and died very often. This resulted in us being more diligent with our time in planning the code writing/testing
2. The pi needed a power supply that our power banks couldnt provide. This prompted a midnight trip to walmart to get the power banks needed

### Turning
Near the end of the project, our servo that controlled turns was no longer able to function properly. This meant that we could no longer perform the turns needed to run our course. To adapt we decided to change our course to be a stright track. We adapted our neural network output to be simply recogize a symbol on the track to stop. 


