import socket
import time 

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.setsockopt(socket.SOL_SOCKET, 25, 'wlx8c3badea7433'.encode())

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock1.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(3)

sock1.sendto('land'.encode(), 0, ('192.168.10.1', 8889))



