import serial 
import time
import numpy
import sys

dataTemp=[]
dataTiempo=[]
#comentar puerto a conveniencia
#puerto='/dev/ttyACM0'
puerto='/dev/ttyUSB0'


def writer(data): #performs operations to record time and temps in a file
	filo=open("Temperatura", "a")
	file=open("Tiempo", "a")

	filo.write(data)
	filo.write("\n")

	#guarda tiempo de cada lectura en archivo separado
	file.write(time.strftime('%X %x'))
	file.write("\n")
	
	file.close()
	filo.close()


def reader(): #reads the serial port and catchs temps
	ser=serial.Serial(puerto, 9600, timeout=0) #timeout=0 (arduino controla el loop)
	t0=time.clock() #cambiar esta funci[on porque lee el tiempo que toma el loop
	while True:
		data=ser.read(24).strip()
        #al usar sys.getsizeof(28.75) [un float] da 24
		#data=ser.readline().decode('ascii')      
		if data:
			
			print(data)
			writer(data)
			dataTemp.append(data)
			
			
		



