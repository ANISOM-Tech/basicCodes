# import librarires
import serial
import time

# setup serial communication
arduino = serial.Serial(port='COM5', baudrate=9600)
inp = '0'

while True:
    try:
        # read the serial data from arduino
        data = (arduino.readline()).decode('utf-8')
        data = data.rstrip('\n')
        print(data)
        arduino.flush()
        
        # write the data in arduino
        # inp = ('1' if inp == '0' else '0')
        inp = input('Enter the value: ')
        arduino.write(bytes(inp, 'utf-8'))
        # arduino.flush()
        time.sleep(2)
    except KeyboardInterrupt:
        arduino.close()
        print('serial port is closed')