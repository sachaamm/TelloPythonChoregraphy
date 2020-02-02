import socket

import time


# wlx503eaaaa884f 
# wlx78d2946e0a54
# wlx8c3badea7325
# wlx8c3badea7433
# wlx503eaaac4bd6

wifiA = 'wlx503eaaaa884f' # TELLO-D1E7F9 
wifiB = 'wlx78d2946e0a54' # TELLO-D1F086
wifiC = 'wlx503eaaac4bd6' # TELLO-D1EDA1
wifiD = 'wlx8c3badea7325' # TELLO-D1EE19



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

_delay = 3
_delayB = 4
_shortDistance = 18
_middleDistance = 30
_longDistance = 120
shortDelay = 0.02


_leftShortMove = 'left ' + str(_shortDistance)
_rightShortMove = 'right ' + str(_shortDistance)
_forwardShortMove = 'forward ' + str(_shortDistance)
_backwardShortMove = 'back ' + str(_shortDistance)
_upShortMove = 'up ' + str(_shortDistance)
_downShortMove = 'down ' + str(_shortDistance)

_leftMiddleMove = 'left ' + str(_middleDistance)
_rightMiddleMove = 'right ' + str(_middleDistance)
_forwardMiddleMove = 'forward ' + str(_middleDistance)
_backwardMiddleMove = 'back ' + str(_middleDistance)
_upMiddleMove = 'up ' + str(_middleDistance)
_downMiddleMove = 'down ' + str(_middleDistance)

_leftLongMove = 'left ' + str(_longDistance)
_rightLongMove = 'right ' + str(_longDistance)
_forwardLongMove = 'forward ' + str(_longDistance)
_backwardLongMove = 'back ' + str(_longDistance)
_upLongMove = 'up ' + str(_longDistance)
_downLongMove = 'down ' + str(_longDistance)


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

def turnSwarm(sockA,sockB,sockC,sockD,shortDelay):
    sendCommand(sockA,_leftLongMove) 
    time.sleep(shortDelay)
    sendCommand(sockB,_forwardLongMove) 
    time.sleep(shortDelay)
    sendCommand(sockC,_rightLongMove) #sock3 -> drone #2 () # sock1 -> drone3
    time.sleep(shortDelay)
    sendCommand(sockD,_backwardLongMove) # sock4 -> drone #3 ()  # sock2 -> drone 4
    time.sleep(shortDelay)

def upAndDown(sockA,sockB,sockC,sockD,shortDelay):
    sendCommand(sockA,_upMiddleMove)
    time.sleep(shortDelay)
    sendCommand(sockB,_downMiddleMove)
    time.sleep(shortDelay)
    sendCommand(sockC,_upMiddleMove)
    time.sleep(shortDelay)
    sendCommand(sockD,_downMiddleMove)
    time.sleep(shortDelay)



print("takeoff")
sendSwarmCommand("command")
sendSwarmCommand("takeoff")
##########


time.sleep(5)
#sendCommand("")

#time.sleep(_delay)
#sendSwarmCommand(_upMiddleMove)
#time.sleep(_delay)

print("a")
turnSwarm(sock1,sock2,sock3,sock4,shortDelay)
time.sleep(3)
print("b")
turnSwarm(sock4,sock1,sock2,sock3,shortDelay)
time.sleep(3)
print("c")
turnSwarm(sock3,sock4,sock1,sock2,shortDelay)
time.sleep(3)
print("d")
turnSwarm(sock2,sock3,sock4,sock1,shortDelay)
time.sleep(3)



sendSwarmCommand('land')




