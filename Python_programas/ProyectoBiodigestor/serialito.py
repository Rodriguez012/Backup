import serial 
import time
import numpy

dataTemp=[]
dataTiempo=[]
#comentar puerto a conveniencia
#puerto='/dev/ttyACM0'
#puerto='/dev/ttyUSB0'

def run():
	ser=serial.Serial('/dev/ttyUSB0', 9600, timeout=0) #timeout=0 (arduino controla el loop)
	t0=time.clock() #cambiar esta funci[on porque lee el tiempo que toma el loop
	while True:
		data=ser.read(24).strip()
        #al usar sys.getsizeof(28.75) [un float] da 24
		#data=ser.readline().decode('ascii')      
		if data:
			
			print(data)
			
			dataTemp.append(data)
			
			
		#time.sleep(3) #time.sleep(t) con t en segundos
