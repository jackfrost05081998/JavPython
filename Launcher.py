import os

print("WELCOME TO OUR PYTHON SNAKE GAME")

while True:
	yorn = input("PRESS ENTER TO START THE GAME! ")
	if yorn == "":
		os.system("python /home/groot/Game.py")
		break
	if yorn != "":
		print("PRESS ENTER AGAIN ")
