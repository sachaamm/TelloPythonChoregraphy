# Choregraphie Tello TDP / CGD 2019 / Alex
import EDU_Tello
import pyglet

import socket

import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

time.sleep(1.5)
#

drones = []
    
drones.append(EDU_Tello.TelloController('wlx503eaaaa884f'))
drones.append(EDU_Tello.TelloController('wlx78d2946e0a54'))
drones.append(EDU_Tello.TelloController('wlx8c3badea7325'))
drones.append(EDU_Tello.TelloController('wlx8c3badea7433'))

drones[0].animate(3,4,'a',40,100,150)
# drones[1].animate(3,4,'b',40,100,150)
# drones[2].animate(3,4,'c',40,100,150)
# drones[3].animate(3,4,'d',40,100,150)


   

