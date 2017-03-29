def __init__(self):
	    self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	
	    try:
		    self.ser.open()
	    except Exception as e:
                print("Error: {}".format(e))
	
	    return self.ser.isOpen()


	#Attempt to read from the GPS module
            def gpsRead(self):
                return self.ser.readline()
            
