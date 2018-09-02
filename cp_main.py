import time


class Pikachu:
	def htford(self,time):
		self.time = time
		print("One hundred thousand Ford Start!!!")
		time.sleep(time)
		print("The enemy must be died!!!")


try:
	time.sleep(0.1)
	print("I use the class")
	Pikachu.htford(time=2)
except BaseException:
	print("Something got wrong")
else:
	print("Write it well")


