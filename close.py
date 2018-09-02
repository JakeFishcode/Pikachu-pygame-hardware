import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(12, GPIO.OUT)  

GPIO.output(12,GPIO.HIGH)
time.sleep(1)  
print("output LOW now")
GPIO.output(12, GPIO.LOW)  

time.sleep(1)
print("output HIGH now")
GPIO.output(12,GPIO.HIGH)

time.sleep(1)
print("output LOW now")
GPIO.output(12,GPIO.LOW)
time.sleep(1)
print("now it's clean")

GPIO.cleanup()
