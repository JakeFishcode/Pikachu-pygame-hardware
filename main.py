import time
import pygame,sys
class Pikachu_music:
	pygame.init()
	pygame.mixer.init()
	ping = pygame.display.set_mode([500,365])
	def play_music(self,road):
		pygame.mixer.music.load(road)
		pygame.mixer.music.play()
	def stop_music(self):
		pygame.mixer.musci.stop()



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
		


p = Pikachu()
time.sleep(0.1)
print("I use the class")
p.htford()
p.shine()
p.scream()
