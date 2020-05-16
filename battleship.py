import random
import copy
class ship:
    def __init__(self):
        self.size = 0
        self.type = ""
        self.direction = ""
        self.startcoord = (0,0)
        self.coords = {}
    def make_ship(self, type, start, direction):
        self.size = 0
        self.type = type
        if type == "Carrier": self.size = 5
        elif type == "Battleship": self.size = 4
        elif type == "Cruiser": self.size = 3
        elif type == "Destroyer": self.size = 2
        else: print("error, bad input type for ship")
        if len(start) != 2: print("error")
        self.direction = direction
        self.startcoord = start
        self.coords = {}
        for x in range(self.size):
            if direction == "up":
                if self.startcoord[1] - x < 0:
                    return "error, ship out of bounds"
                self.coords[(self.startcoord[0], self.startcoord[1] - x)] = "safe"
            elif direction =="down":
                if self.startcoord[1] + x > 9:
                    return "error, ship out of bounds"
                self.coords[(self.startcoord[0], self.startcoord[1] + x)] = "safe"
            elif direction == "right":
                if self.startcoord[0] + x > 9:
                    return "error, ship out of bounds"
                self.coords[(self.startcoord[0] + x, self.startcoord[1])] = "safe"
            elif direction == "left":
                if self.startcoord[0] - x < 0:
                    return "error, ship out of bounds"
                self.coords[(self.startcoord[0] - x, self.startcoord[1])] = "safe"
            else:
                return "error, wrong direction input"
    def get_type(self):
        return self.type
    def get_start(self):
        return self.startcoord
    def get_direction(self):
        return self.direction
    def get_coords(self):
        return self.coords
    def try_hit(self, coord):
        hit = False
        sunk = True
        for val in self.coords:
            if coord == val:
                if self.coords[val] != "hit": hit = True
                self.coords[val] = "hit"
        for val in self.coords:
            if self.coords[val] == "safe": sunk = False
        if sunk and hit: return "sunk"
        if hit: return "hit"
        return "miss"
class Board:
    def __init__(self):
        self.sunken = 0
        self.Carrier = None
        self.Battleship = None
        self.Cruiser2 = None
        self.Cruiser1 = None
        self.Destroyer = None
        self.shiplist = []
        self.board = {}

    def make_board(self, Carrier, Battleship, Cruiser1, Cruiser2, Destroyer):
        self.sunken = 0
        self.Carrier = Carrier
        self.Battleship = Battleship
        self.Cruiser1 = Cruiser1
        self.Cruiser2 = Cruiser2
        self.Destroyer = Destroyer
        self.shiplist = [Carrier,Battleship,Cruiser1,Cruiser2,Destroyer]
        self.board = {}
        for x in range(10):
            for y in range(10):
                self.board[(x,y)] = "water"
        for ship in self.shiplist:
            for coord in ship.get_coords():
                if self.board[coord] == "water":
                    self.board[coord] = ship.get_type()
                else:
                    return "error, ships overlap"
    def get_board(self):
        return self.board
    def try_hit(self, tuple):
        if self.board[tuple] == "hit" or self.board[tuple] == "hit water":
            return "already attempted"
        for x in self.shiplist:
            test = x.try_hit(tuple)
            if test == "hit":
                self.board[tuple] = "hit"
                return "hit"
            if test == "sunk":
                self.board[tuple] = "hit"
                self.sunken +=1
                if self.sunken != 5:return "sunk the " + x.get_type()
                else: return "sunk the " + x.get_type() + ", all ships sunk"
        self.board[tuple] = "hit water"
        return "miss"
    def print_board(self):
        for x in range(10):
            for y in range(10):
                add = 11 - len(self.board[(y,x)])
                print(self.board[(y,x)], end="")
                for z in range(add):
                    print(" ", end="")
            print("")
            print("")
class Player:
    def __init__(self, board1, board2):
        self.board = board1
        self.board2 = board2
        self.won = None
    def get_board(self):
        return self.board
    def print_board(self):
        self.board.print_board()
    def make_move(self,move):
        s  = self.board2.try_hit(move)
        if (len(s) < 16) or (s[len(s)-16:len(s)] != ", all ships sunk"):
            return s
        else:
            return s[0:len(s)-16] + ", you Win!"
    def move_made(self,move):
        s = self.board.try_hit(move)
        if (len(s) < 16) or (s[len(s)-16:len(s)] != ", all ships sunk"):
            return s
        else:
            return s[0:len(s)-16] + ", you Lose!"
def make_random_Board():
    ship1 = ship()
    ship2 = ship()
    ship3 = ship()
    ship4 = ship()
    ship5 = ship()
    directions = ["left", "right", "up", "down"]
    ships = ["Carrier", "Battleship", "Cruiser", "Cruiser", "Destroyer"]
    b1 = ""
    board1 = Board()
    while b1 != None:
        n1 = ""
        while n1 != None:
            x1 = random.randint(0,9)
            y1 = random.randint(0,9)
            d = directions[random.randint(0,3)]
            n1 = ship1.make_ship("Carrier", (x1,y1), d)
        n2 = ""
        while n2 != None:
            x1 = random.randint(0,9)
            y1 = random.randint(0,9)
            d = directions[random.randint(0,3)]
            n2 = ship2.make_ship("Battleship", (x1,y1), d)
        n3 = ""
        while n3 != None:
            x1 = random.randint(0,9)
            y1 = random.randint(0,9)
            d = directions[random.randint(0,3)]
            n3 = ship3.make_ship("Cruiser", (x1,y1), d)
        n4 = ""
        while n4 != None:
            x1 = random.randint(0,9)
            y1 = random.randint(0,9)
            d = directions[random.randint(0,3)]
            n4 = ship4.make_ship("Cruiser", (x1,y1), d)
        n5 = ""
        while n5 != None:
            x1 = random.randint(0,9)
            y1 = random.randint(0,9)
            d = directions[random.randint(0,3)]
            n5 = ship5.make_ship("Destroyer", (x1,y1), d)
        b1 = board1.make_board(ship1, ship2, ship3, ship4, ship5)
    # board1.print_board()
    return board1
def play_random_Game():
    board1 = make_random_Board()
    board2 = make_random_Board()
    player1 = Player(board1, board2)
    player2 = Player(copy.deepcopy(board2), copy.deepcopy(board1))
    list1 = [(x, y) for x in range(10) for y in range(10)]
    list2 = [(x,y) for x in range(10) for y in range(10)]
    string1 = ""
    string2 = ""
    while((len(string1) < 10 or string1[len(string1)-10:len(string1)] !=", you Win!") and (len(string2) < 10 or string2[len(string2)-10:len(string2)] != ", you Win!")):
        x = random.randint(0,len(list1)-1)
        tup1 = list1[x]
        list1 = list1[0:x] + list1[x+1:]
        y = random.randint(0,len(list2)-1)
        tup2 = list2[y]
        list2 = list2[0:y] + list2[y+1:]
        string1 = player1.make_move(tup1)
        player1.move_made(tup2)
        string2 = player2.make_move(tup2)
        player2.move_made(tup1)
        print("player 1: " + str(tup1) + " " + string1)
        print("player 2: " + str(tup2) + " " + string2)
        print("")
    player1.print_board()
    print("")
    player2.print_board()
play_random_Game()
