import socket
import time
import urllib.request
import os.path
import sys
from car import move, allStop, forwardDrive
from camera import pic

DOCUMENT_ROOT = ''

#print(str(socket.gethostbyname("www.google.com")))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',80))
s.listen(10)
#t = (urllib.request.urlopen("http://tbau.000webhostapp.com/Photoshop Website/images/earth2.jpg").read())


try:
    c, addr = s.accept()
    print("Got connection from"+str(addr))
    f = open ('train.txt' , 'w')
    while True:
        request = c.recv(4096)
        if(request != None):
           # print ("Message: "+request.decode('utf-8'))
            str=request.decode('utf-8')
        if(str != ""):
            print(str)
        if(str == "1000"):
            forwardDrive()
            print("After")
        elif(str == "1010"):
            move([1,0,1,0])
        elif(str == "1001"):
            move([1,0,0,1])
        else:
            allStop()
        #request.decode is how we grab

    c.close()
       # print("Connection done")
except BaseException as error:
    #c.close()
    print(error)
finally:
	s.close()
