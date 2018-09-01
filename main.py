import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

ledStatus = 1
GPIO.output(22,GPIO.HIGH)#key output high
GPIO.output(23,GPIO.HIGH)

while True:
	if(GPIO.input(21) == GPIO.HIGH):
		print("button pressd!")
		ledStatus = not ledStatus
		if ledStatus:
			GPIO.output(23,GPIO.HIGH)
			GPIO.cleanup()
			eixt()
			pass
		else:
			GPIO.ouput(23,GPIO.LOW)
			pass
		time.sleep(0.03)
		pass
	time.sleep(0.01)
	pass
