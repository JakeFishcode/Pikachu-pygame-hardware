import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(12, GPIO.OUT)  
GPIO.output(12,GPIO.HIGH)
time.sleep(1)
GPIO.output(12,GPIO.LOW)
print("now it's LOW")
time.sleep(5)
print("now sleep over")
GPIO.output(12,GPIO.HIGH)
time.sleep(1)
GPIO.output(12,GPIO.LOW)
print("wait for it's change")
time.sleep(3)
print("It changes")
time.sleep(1)
GPIO.cleanup()


