import socket
import time

# EDU Tello Controller Class
class TelloController:

    def __init__(self,network_interface):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, 25, network_interface.encode())
        self.networkInterface = network_interface
        print("Instantiate a drone under network interface : " + network_interface)

    


    def animate(self,_delay,_delayB,_argument,_shortDistance,_middleDistance,_longDistance):

        # https://jaxenter.com/implement-switch-case-statement-python-138315.html
        switcher = {
            'a': self.animationA(_delay,_delayB,_shortDistance,_middleDistance,_longDistance),
            'b': self.animationB(_delay,_delayB,_shortDistance,_middleDistance,_longDistance),
            'c': self.animationC(_delay,_delayB,_shortDistance,_middleDistance,_longDistance),
            'd': self.animationD(_delay,_delayB,_shortDistance,_middleDistance,_longDistance)
        }

        print (" Animate drone with animation " + _argument)

        # Get the function from switcher dictionary
        animation = switcher.get(_argument, lambda: "Invalid argument")
        # animation()
        # Execute the function
        

    def initiateAnimation(self): # Initiate command sending
        print("Initiate command sending on " + self.networkInterface)
        self.sock.sendto('command'.encode(), 0, ('192.168.10.1', 8889))   
        self.sock.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))

    def animationDelay(self,_delay):
        print("Animation delay " + str(_delay))

        time.sleep(_delay)

    def animationA(self,_delay,_delayB,_shortDistance,_middleDistance,_longDistance):

        self.animationFirstPart(_delay,_delayB,_shortDistance,_middleDistance)

        self.sock.sendto('left ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #16
        self.animationDelay(_delay)
        self.sock.sendto('backward ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #17
        self.animationDelay(_delay)
        self.sock.sendto('right ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) # 18 
        self.animationDelay(_delay)
        self.sock.sendto('forward ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #19
        self.animationDelay(_delay)

        self.animationLastPart(_delay,_delayB)
    

    def animationB(self,_delay,_delayB,_shortDistance,_middleDistance,_longDistance):
        
        self.animationFirstPart(_delay,_delayB,_shortDistance,_middleDistance)

        self.sock.sendto('left ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #16
        self.animationDelay(_delay)
        self.sock.sendto('backward ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #17
        self.animationDelay(_delay)
        self.sock.sendto('right ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) # 18 
        self.animationDelay(_delay)
        self.sock.sendto('forward ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #19
        self.animationDelay(_delay)

        self.animationLastPart(_delay,_delayB)

    def animationC(self,_delay,_delayB,_shortDistance,_middleDistance,_longDistance):

        self.animationFirstPart(_delay,_delayB,_shortDistance,_middleDistance)

        self.sock.sendto('left ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #16
        self.animationDelay(_delay)
        self.sock.sendto('backward ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #17
        self.animationDelay(_delay)
        self.sock.sendto('right ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) # 18 
        self.animationDelay(_delay)
        self.sock.sendto('forward ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #19
        self.animationDelay(_delay)

        self.animationLastPart(_delay,_delayB)

    def animationD(self,_delay,_delayB,_shortDistance,_middleDistance,_longDistance):

        self.animationFirstPart(_delay,_delayB,_shortDistance,_middleDistance)

        self.sock.sendto('left ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #16
        self.animationDelay(_delay)
        self.sock.sendto('backward ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #17
        self.animationDelay(_delay)
        self.sock.sendto('right ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) # 18 
        self.animationDelay(_delay)
        self.sock.sendto('forward ' + str(_longDistance).encode(), 0, ('192.168.10.1', 8889)) #19
        self.animationDelay(_delay)

        self.animationLastPart(_delay,_delayB)

    # short Distance 40 middle 100 long 150
    def animationFirstPart(self,_delay,_delayB,_shortDistance,_middleDistance):

        self.initiateAnimation()
        self.animationDelay(_delay)

        # self.sock.sendto('ccw 30'.encode(), 0, ('192.168.10.1', 8889))
        # self.animationDelay(_delay)

        self.sock.sendto('left ' + str(_shortDistance).encode(), 0, ('192.168.10.1', 8889)) #1
        self.animationDelay(_delay)
        self.sock.sendto('up ' + str(_shortDistance).encode(), 0, ('192.168.10.1', 8889)) #2
        self.animationDelay(_delay)
        self.sock.sendto('right ' + str(_shortDistance).encode(), 0, ('192.168.10.1', 8889)) #3
        self.animationDelay(_delay)
        self.sock.sendto('down ' + str(_shortDistance).encode(), 0, ('192.168.10.1', 8889)) #4
        self.animationDelay(_delay)


        self.sock.sendto('cw 90'.encode(), 0, ('192.168.10.1', 8889)) #5
        self.animationDelay(_delayB)
        self.sock.sendto('ccw 90'.encode(), 0, ('192.168.10.1', 8889)) #6
        self.animationDelay(_delayB)
        self.sock.sendto('up ' + str(_shortDistance).encode(), 0, ('192.168.10.1', 8889)) #7
        self.animationDelay(_delayB)
        self.sock.sendto('cw 30'.encode(), 0, ('192.168.10.1', 8889)) #8
        self.animationDelay(_delayB)
        self.sock.sendto('ccw 30'.encode(), 0, ('192.168.10.1', 8889)) #9
        self.animationDelay(_delayB)
        self.sock.sendto('cw 180'.encode(), 0, ('192.168.10.1', 8889)) #10
        self.animationDelay(_delayB)
        self.sock.sendto('up ' + str(_middleDistance).encode(), 0, ('192.168.10.1', 8889)) #11
        self.animationDelay(_delayB)
        self.sock.sendto('down ' + str(_middleDistance).encode(), 0, ('192.168.10.1', 8889)) #12 
        self.animationDelay(2)
        self.sock.sendto('up ' + str(_middleDistance).encode(), 0, ('192.168.10.1', 8889)) #13 
        self.animationDelay(2)
        self.sock.sendto('down ' + str(_middleDistance).encode(), 0, ('192.168.10.1', 8889)) #14
        self.animationDelay(2)
        self.sock.sendto('up ' + str(_middleDistance).encode(), 0, ('192.168.10.1', 8889)) #15
        self.animationDelay(2)

    def animationLastPart(self,_delay,_delayB):
        self.sock.sendto('ccw 180'.encode(), 0, ('192.168.10.1', 8889)) #20
        self.animationDelay(_delay) 
        self.sock.sendto('cw 360'.encode(), 0, ('192.168.10.1', 8889)) #21
        self.animationDelay(_delay)

        self.sock.sendto('land'.encode(), 0, ('192.168.10.1', 8889))