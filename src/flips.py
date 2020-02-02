import socket

import time


# wlx503eaaaa884f 
# wlx78d2946e0a54
# wlx8c3badea7325
# wlx8c3badea7433
# wlx503eaaac4bd6

wifiA = 'wlx503eaaac4bd6' # TELLO-D1E7F9 
wifiB = 'wlx78d2946e0a54' # TELLO-D1F086
wifiC = 'wlx8c3badea7325' # TELLO-D1EDA1
wifiD = 'wlp3s0' # TELLO-D1EE19


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

#print "UDP target IP:", UDP_IP
#print "UDP target port:", UDP_PORT
#print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

time.sleep(1.5)

_delay = 1
_delayB = 5



sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.setsockopt(socket.SOL_SOCKET, 25, wifiA.encode())

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.setsockopt(socket.SOL_SOCKET, 25, wifiB.encode())

sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3.setsockopt(socket.SOL_SOCKET, 25, wifiC.encode())

sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock4.setsockopt(socket.SOL_SOCKET, 25, wifiD.encode())

def sendSwarmCommand(command):
    sendCommand(sock1,command.encode())
    time.sleep(0.02)
    sendCommand(sock2,command.encode())
    time.sleep(0.02)
    sendCommand(sock3,command.encode())
    time.sleep(0.02)
    sendCommand(sock4,command.encode())
    time.sleep(0.02)


def sendCommand(telloSock,command):
    telloSock.sendto(command.encode(),0, ('192.168.10.1', 8889)) 




print("takeoff")
sendSwarmCommand("command")
sendSwarmCommand("takeoff")
##########


time.sleep(_delayB)

sendSwarmCommand("flip b")
time.sleep(_delay)
sendSwarmCommand("flip f")
time.sleep(_delay)
# sendSwarmCommand("flip b")
# time.sleep(_delay)
# sendSwarmCommand("flip f")
# time.sleep(_delay)



sendSwarmCommand('land')




