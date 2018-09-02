import time
import pygame,sys
import RPi.GPIO as GPIO

class Pikachu_music:
	pygame.init()
	pygame.mixer.init()
	def play_music(self,road):
		pygame.mixer.music.load(road)
		pygame.mixer.music.play()
	def stop_music(self):
		pygame.mixer.music.stop()

class Raspberrypi():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(12,GPIO.OUT)#Relay out
	GPIO.output(12,GPIO.HIGH)
	GPIO.setup(8,GPIO.OUT)#led out
	GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)#key input
	def led_shine_1(self):
		GPIO.output(8,GPIO.HIGH)
	def led_shine_0(self):
		GPIO.output(8,GPIO.LOW)
	
	def relay_ht_1(self):
		GPIO.output(12,GPIO.LOW)
	def relay_ht_0(self):
		GPIO.output(12,GPIO.HIGH)
	
	


class Pikachu:

	def htford(self,ht_time=0.5):
		self.ht_time = ht_time
		print("One hundred thousand Ford Start!!!")
		time.sleep(ht_time)
		print("The enemy must be died!!!")

	def shine(self,sh_time=0.5):
		self.sh_time = sh_time
		print("Shinning")
		time.sleep(sh_time)
		print("The emnemy must be blind")
	
	def scream(self,sc_time=0.5):
		self.sc_time = sc_time
		print("Shutting!!!")
		time.sleep(sc_time)
		print("The emnemy must be deaf")
		

if __name__  == '__main__':
	print("Test")
	R = Raspberrypi()
	P = Pikachu_music()
	m = 'try.mp3'
	try:
		while True:
			if GPIO.input(6) == GPIO.HIGH:
				print("key down")
				P.play_music(m)
				time.sleep(2)
				R.relay_ht_1()
				time.sleep(1)
				R.relay_ht_0()
	except BaseException:
		GPIO.cleanup()

