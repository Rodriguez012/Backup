import serial
import time
import numpy


def main():
	ser=serial.Serial('/dev/ttyACM1', 9600, timeout=1)

	while True:
		data=ser.read(32).strip()
		#print hola        
		if data:
			print(data)
		time.sleep(1)
