import random

class shipSet(object):

    def  __init__(self):
        self.cells = set ([])
        self.hitspace = set([])

    def addCell(self, cell):
        if isinstance(cell, set):
            self.cells = self.cells.union(cell)
        else:
            self.cells.add(cell)

    def ifhit(self, cell):
        self.hitspace.add(cell)
        a = self.hitspace
        self.cells.remove(cell)
        z = self.cells


    def isDead(self):
        if len(self.cells) == 0:
            #print 'Ship length is zero'
            return True


class workShip(object):

    def __init__(self):
        self.object=[]

    def createListShips(self):

        for c in range(1):
            ship = shipSet()
            ship.addCell(self.genDeckShip(4))
            self.object.append(ship)

        for c in range(3):
            ship = shipSet()
            ship.addCell(self.genDeckShip(2))
            self.object.append(ship)

        for c in range(2):
            ship = shipSet()
            ship.addCell(self.genDeckShip(3))
            self.object.append(ship)

        for c in range(4):
            ship = shipSet()
            ship.addCell(self.genShipPlace())
            self.object.append(ship)


    def delFromObject(self, x, y):
        for i in self.object:
            if (x,y) in i.cells:
                i.ifhit((x,y))
                # print 'deleted'
                return 'deleted' 


    def shipCells(self):

        gg = set([])
        for gl in self.object:
            gg = gg.union(gl.cells)
        return gg

    def placeNearShip(self):

        kotl = set([])
        for x,y in self.shipCells():
            for a in range(x-1,x+2):
                for b in range(y-1,y+2):
                    if (a,b) != (x,y):
                        kotl.add((a,b))
        return kotl

    def genShipPlace(self):

        allspace = set([])

        for i in range(0,10):
            for j in range(0,10):
                allspace.add((i,j))

            space = allspace - (self.shipCells().union(self.placeNearShip()))
            ship = random.sample(space, 1)


        return ship[0]

    def genDeckShip(self, deck):

        allspace = set([])
        for i in range(0,10):
            for j in  range(0,10):
                allspace.add((i,j))
                space = allspace - (self.shipCells().union(self.placeNearShip()))

        shiplist = []
        for x, y in space:
            z = self.generateSet(x,y,deck)
            for i in z:
                if i.issubset(space):
                    shiplist.append(i)

        deck2ship = random.sample(shiplist,1)[0]
        return deck2ship

    def generateSet(self, x, y, deck):
        if deck == 2:
            z = set([])
            w = set([])
            for i in range(2):
                z.add((x,y+i))
                w.add((x+i,y))
            return [z,w]

        elif deck == 3:
            z = set([])
            w = set([])
            for i in range(3):
                z.add((x,y+i))
                w.add((x+i,y))
            return [z,w]

        elif deck == 4:
            z = set([])
            w = set([])
            for i in range(4):
                z.add((x,y+i))
                w.add((x+i,y))
            return [z,w]

