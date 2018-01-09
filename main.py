from pygame.locals import *
from time import sleep
import drawShipsandStuff
import makeShips
import Controller
import pygame
import sys
from random import randint

count = 1
num_hits = 0
num_misses = 0
score = 0
visitedPlayer1 = [ [0]*10 for _ in xrange(10) ]
visitedPlayer2 = [ [0]*10 for _ in xrange(10) ]

owncolor = drawShipsandStuff.OWNSHIPCOLOR
enemycolor = drawShipsandStuff.ENEMYSHIPCOLOR

drawShipsandStuff.drawBoard()
drawShipsandStuff.drawBoard(360)
# draw.drawBoard()

ownship = makeShips.workShip()
enemyship = makeShips.workShip()

# for i in range(100):
# 	for j in ownship.object:
# 		for x,y in j.cells:




OwnListShip = ownship.createListShips()
EnemyListShip = enemyship.createListShips()

# drawShipsandStuff.drawAllShip(ownship.object, owncolor, 'own')
# drawShipsandStuff.drawAllShip(enemyship.object, enemycolor, 'enemy')

# for i in enemyship.object:
#     print i.cells

def ifAllDead(workship):
	cnt = True
	for i in workship.object:
		if (not i.isDead()):
			cnt = False

	return cnt

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		# if event.type == MOUSEBUTTONUP:

	# mousex = randint(30,690)
	# mousey = randint(30,330)
	x = -1
	y = -1
	
	if (count % 2):	
		# o = max([max(Controller.scoresPlayer1[i]) for i in xrange(10)])
		m = Controller.scoresPlayer1[0][0]

		for a in xrange(10):
			for b in xrange(10):
				if (Controller.scoresPlayer1[a][b]>m and visitedPlayer1[a][b] is 0):
					m = Controller.scoresPlayer1[a][b]

		# print Controller.scoresPlayer1
		# print o
		for i in xrange(10):
			for j in xrange(10):
				print ("MYYYYYY::::maxValue: ", m, " currentvalue: ", Controller.scoresPlayer1[i][j])
				if (Controller.scoresPlayer1[i][j] ==m):
					# Controller.scoresPlayer1[i][j] = -999999
					visitedPlayer1[i][j] = 1;
					x = i+1;
					y = j+1;
					break;
			if x > -1:
				break;

		# mousex = (x * 30) + 390
		# mousey = (y * 30) + 30

		print ("x: ", x, " y: ", y)

		# check = (mousex >= 390 and mousex < 690 and mousey >= 30 and mousey < 330)
		# if (check):
		if Controller.checkAction(ownship.object, enemyship, x-1, y-1):
			count = count + 1
				# print(count)
		# else:
		# 	print ("Not your house, mate!")
				
	else:
		# o = max([max(Controller.scoresPlayer2[i]) for i in xrange(10)])
		m = Controller.scoresPlayer2[0][0]

		for a in xrange(10):
			for b in xrange(10):
				if (Controller.scoresPlayer2[a][b]>m and visitedPlayer2[a][b] is 0):
					m = Controller.scoresPlayer2[a][b]
		# print Controller.scoresPlayer2
		# print o
		for i in xrange(10):
			for j in xrange(10):
				print ("ENEMYYYYY::::maxValue: ", m, " currentvalue: ", Controller.scoresPlayer2[i][j])
				if (Controller.scoresPlayer2[i][j]==m):
					# Controller.scoresPlayer2[i][j] = -999999
					visitedPlayer2[i][j]= 1;
					x = i+1;
					y = j+1;
					break;
			if x > -1:
				break;

		# mousex = (x * 30) + 30
		# mousey = (y * 30) + 30

		print ("x: ", x, " y: ", y)
		
		# check = mousex >= 30 and mousex < 330 and mousey >= 30 and mousey < 330
		# if (check):
		if Controller.checkAction1(enemyship.object, ownship, x-1, y-1):
			count = count + 1
		# else:
		# 	print ("Not your home, mate!")

	if (ifAllDead(ownship)):
		print("The enemy wins! You surely suck at this game! BlarglarghGlargh!!")
		inputFile1 = open("scoresp1.txt", "w")
		inputFile2 = open("scoresp2.txt", "w")
		for i in xrange(10):
			for j in xrange(10):
				inputFile1.write(str(Controller.scoresPlayer1[i][j])+"\n")
				inputFile2.write(str(Controller.scoresPlayer2[i][j])+"\n")
		break

	elif (ifAllDead(enemyship)):
		print(" I won!!")
		inputFile1 = open("scoresp1.txt", "w")
		inputFile2 = open("scoresp2.txt", "w")
		for i in xrange(10):
			for j in xrange(10):
				inputFile1.write(str(Controller.scoresPlayer1[i][j])+"\n")
				inputFile2.write(str(Controller.scoresPlayer2[i][j])+"\n")
		break
			
	pygame.display.update()
	# sleep(0.2)
sleep(0.05)
