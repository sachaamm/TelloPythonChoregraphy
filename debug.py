import socket

import time

from wifi import Cell, Scheme



# wlx503eaaaa884f 
# wlx78d2946e0a54
# wlx8c3badea7325
# wlx8c3badea7433

wifiA = 'wlx503eaaaa884f' # TELLO-D1E7F9 
wifiB = 'wlx78d2946e0a54' # TELLO-D1F086
wifiC = 'wlx8c3badea7325' # TELLO-D1EDA1
wifiD = 'wlx503eaaac4bd6' # TELLO-D1EE19



#cellA = Cell.all(wifiA)
#cellB = Cell.all(wifiB)
#cellC = Cell.all(wifiC)
#cellD = Cell.all(wifiD)

#schemeA = Scheme.for_cell('wlsp', 'TELLO-D1E7F9', cellA, 'aa')
#schemeA.save()
#schemeA.activate()



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
_longDistance = 140

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
    sendCommand(sock1,command)
    time.sleep(0.02)
    sendCommand(sock2,command)
    time.sleep(0.02)
    sendCommand(sock3,command)
    time.sleep(0.02)
    sendCommand(sock4,command)
    time.sleep(0.02)


def sendCommand(telloSock,command):
    telloSock.sendto(command.encode(),0, ('192.168.10.1', 8889)) 



print("takeoff")
#sendSwarmCommand("command")
#sendSwarmCommand("takeoff")


sockTest = sock1

sendCommand(sockTest,"command")
sendCommand(sockTest,"takeoff")


time.sleep(_delay)
sendCommand(sock1,_backwardLongMove) 
time.sleep(_delay)
sendCommand(sock1,_rightLongMove) 
time.sleep(_delay)
sendCommand(sock1,_forwardLongMove)
time.sleep(_delay) 
sendCommand(sock1,_leftLongMove) 
time.sleep(_delay)
sendCommand(sockTest,"land")






time.sleep(_delay)
sendSwarmCommand(_upMiddleMove)
time.sleep(_delay)

shortDelay = 0.02

sendSwarmCommand("flip b")

print("first part...")
print("a")
# sendSwarmCommand(_leftShortMove)
# time.sleep(_delay)
print("b")
# sendSwarmCommand(_upShortMove)
# time.sleep(_delay)
print("c")
# sendSwarmCommand(_rightShortMove)
# time.sleep(_delay)
print("d")
#sendSwarmCommand(_downShortMove)
# time.sleep(_delay)
print("e")
# sendSwarmCommand('cw 90')
# time.sleep(_delayB)
print("f")
# sendSwarmCommand('ccw 90')
# time.sleep(_delayB)
print("g")
# sendSwarmCommand(_upShortMove)
# time.sleep(_delayB)
print("h")
# sendSwarmCommand('cw 30')
# time.sleep(_delayB)
print("i")
# sendSwarmCommand('ccw 30')
# time.sleep(_delayB)
print("j")

time.sleep(_delayB)
sendSwarmCommand('cw 180')

print("up and down...")
sendSwarmCommand(_upMiddleMove)
time.sleep(_delay)
sendSwarmCommand(_downMiddleMove)
time.sleep(_delay)
sendSwarmCommand(_upMiddleMove)
#time.sleep(_delay)
#sendSwarmCommand(_downMiddleMove)
#time.sleep(_delay)
#sendSwarmCommand(_upMiddleMove)
#time.sleep(_delay)

print("differing part...")
print("a")
sendCommand(sock1,_backwardLongMove) 
time.sleep(shortDelay)
sendCommand(sock2,_leftLongMove) 
time.sleep(shortDelay)
sendCommand(sock3,_forwardLongMove) #sock3 -> drone #2 () # sock1 -> drone3
time.sleep(shortDelay)
sendCommand(sock4,_rightLongMove) # sock4 -> drone #3 ()  # sock2 -> drone 4

time.sleep(_delay)
print("b")
sendCommand(sock1,_rightLongMove)
time.sleep(shortDelay)
sendCommand(sock2,_backwardLongMove)
time.sleep(shortDelay)
sendCommand(sock3,_leftLongMove)
time.sleep(shortDelay)
sendCommand(sock4,_forwardLongMove)

time.sleep(_delay)
print("c")
sendCommand(sock1,_forwardLongMove)
time.sleep(shortDelay)
sendCommand(sock2,_rightLongMove)
time.sleep(shortDelay)
sendCommand(sock3,_backwardLongMove)
time.sleep(shortDelay)
sendCommand(sock4,_leftLongMove)

time.sleep(_delay)
print("d")
sendCommand(sock1,_leftLongMove)
time.sleep(shortDelay)
sendCommand(sock2,_forwardLongMove)
time.sleep(shortDelay)
sendCommand(sock3,_rightLongMove)
time.sleep(shortDelay)
sendCommand(sock4,_backwardLongMove)
time.sleep(shortDelay)

time.sleep(_delay)

print("ending part...")
sendSwarmCommand('ccw 180')
time.sleep(_delay)

sendSwarmCommand('cw 360')
time.sleep(_delay)


sendCommand(sock1,_upMiddleMove)
time.sleep(0.01)
sendCommand(sock2,_downMiddleMove)
time.sleep(0.01)
sendCommand(sock3,_upMiddleMove)
time.sleep(0.01)
sendCommand(sock4,_downMiddleMove)
time.sleep(0.01)

sendCommand(sock1,_downMiddleMove)
time.sleep(0.01)
sendCommand(sock2,_upMiddleMove)
time.sleep(0.01)
sendCommand(sock3,_downMiddleMove)
time.sleep(0.01)
sendCommand(sock4,_upMiddleMove)
time.sleep(0.01)




sendSwarmCommand('land')




