import time
import pygame,sys
class Pikachu_music:
	pygame.init()
	pygame.mixer.init()
	def play_music(self,road):
		pygame.mixer.music.load(road)
		pygame.mixer.music.play()
	def stop_music(self):
		pygame.mixer.music.stop()



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
		
a = Pikachu_music()
music_file = 'try.mp3'
a.play_music(music_file)
time.sleep(20)
a.stop_music()

p = Pikachu()
time.sleep(0.1)
print("I use the class")
p.htford()
p.shine()
p.scream()


if __init__ =='__main__':
	main()
