import socket
import pyglet

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

playing = False

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data

    # if music != None:
    #    music.stop()

    music = pyglet.resource.media('music/odesza-a-moment-apart.wav')
    music.play()

    pyglet.app.run()

    #   playing = True


