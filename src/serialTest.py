import serial
import time
# ser = serial.Serial('/dev/tty.usbserial', 9600)
ser = serial.Serial('/dev/ttyACM0', 9600)
while True: # send each second data through Serial
    print "..."
    time.sleep(1)
    ser.write('5')
