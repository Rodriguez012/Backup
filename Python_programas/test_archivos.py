import time

#def test():
while True:
      file=open("prueba","a")
      file.write(time.strftime('%X %x'))
      file.write("\n")
      time.sleep(1)
      file.close()
