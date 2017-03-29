def gpsRead(self):
		while True:
			self.ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
			if self.ser.isOpen():
				print 'Open: '
			data = self.ser.readline()
			print data
		return data
