import drawShipsandStuff
global scoresPlayer1, scoresPlayer2, inputFile1, inputFile2;

scoresPlayer1 = [ [0]*10 for _ in xrange(10) ]
inputFile1 = open("scoresp1.txt");
for i in xrange(10):
    for j in xrange(10):
        xx = inputFile1.readline();
        xx = xx[:-1]
        scoresPlayer1[i][j] = int(xx)

scoresPlayer2 = [ [0]*10 for _ in xrange(10) ]
inputFile2 = open("scoresp2.txt");
for i in xrange(10):
    for j in xrange(10):
        yy = inputFile2.readline();
        yy = yy[:-1]
        scoresPlayer2[i][j] = int(yy)

inputFile1.close();
inputFile2.close();

def checkAction(ownship, ship, x, y):
    check = True
    # x = (mx-360)/30
    # y = (my)/30
    
    if ship.delFromObject(y,x) == 'deleted':
        print 'We got a hit Admiral!'
        print x,y
        scoresPlayer1[x][y]=scoresPlayer1[x][y]+1;
        check = False
       # draw.drawEnemyShip(draw.DISPLAYSURF, ship, x, y)
    else:
        print 'Nah! you suck :('
        print x, y
        scoresPlayer1[x][y]=scoresPlayer1[x][y]-1;
        check = True
    drawShipsandStuff.reDrawAll(ownship, ship, drawShipsandStuff.OWNSHIPCOLOR, 'own', drawShipsandStuff.DISPLAYSURF, x,y)
    # zxc = input("asdfsdfdsaf")
    return check

def checkAction1(ownship, ship, x, y):
    check = True
    # x = (mx)/30
    # y = my/30

    # print mx, my
    if ship.delFromObject(y,x) == 'deleted':
        print 'We got a hit Admiral!'
        print x,y
        scoresPlayer2[x][y] = scoresPlayer2[x][y]+1;
        
        check = False
       # draw.drawEnemyShip(draw.DISPLAYSURF, ship, x, y)
    else:
        print 'Nah! you suck :('
        print x,y
        scoresPlayer2[x][y]=scoresPlayer2[x][y]-1;
        check = True
    drawShipsandStuff.reDrawAll(ownship, ship, drawShipsandStuff.ENEMYSHIPCOLOR, 'enemy', drawShipsandStuff.DISPLAYSURF, x,y, 0)
    # zxc = input("asdfsdfdsaf")
    return check