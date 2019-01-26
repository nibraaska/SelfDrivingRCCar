import socket
import time
import urllib.request
import os.path
import sys
from car import forwardDrive,forwardTurnLeft, forwardTurnRight, reverse, allStop

DOCUMENT_ROOT = ''

#print(str(socket.gethostbyname("www.google.com")))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',81))
s.listen(10)
#t = (urllib.request.urlopen("http://tbau.000webhostapp.com/Photoshop Website/images/earth2.jpg").read())


try:
    c, addr = s.accept()
    print("Got connection from"+str(addr))
    
    while True:
        request = c.recv(4096)
        if(request != None):
            #print ("Message: "+request.decode('utf-8'))
            str=request.decode('utf-8')
            if(str != ""):
                print(str)
            if(str == "1000"):
                forwardDrive()
            elif(str == "1001"):
                forwardTurnRight()
            elif(str == "1010"):
                forwardTurnLeft()
            #if(str == "0100"):
            #    reverse()
            else:
                allStop()
        #request.decode is how we grab
        
    c.close()
       # print("Connection done")
except BaseException as error:
    #c.close()
    print(error)

s.close()
