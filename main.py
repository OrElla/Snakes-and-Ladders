import turtle
import random
import time


N = 7
SIZE = 80
font_size = 15

is_over = False



def box():
    for i in range(4):
        Board.table_board.backward(SIZE)
        Board.table_board.right(90)


class Board:

    table_board = turtle.Turtle()
    gameMatrix = []
    Placing_Board = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.table_board.hideturtle()
        self.table_board.speed(0)

        Board.create_board(self)

    def define_Cube(self):
        Board.table_board.hideturtle()
        Board.table_board.penup()
        Board.table_board.goto(-300, - 2 * SIZE)
        Board.table_board.pendown()
        for i in range(4):
            Board.table_board.backward(SIZE / 2)
            Board.table_board.right(90)
        Board.table_board.hideturtle()


    def define_BoardGame(self):
        self.gameMatrix[2] = 9
        self.gameMatrix[5] = 2
        self.gameMatrix[9] = -5
        self.gameMatrix[12] = -12
        self.gameMatrix[13] = 14
        self.gameMatrix[17] = 15
        self.gameMatrix[25] = -15
        self.gameMatrix[26] = 4
        self.gameMatrix[33] = -10
        self.gameMatrix[34] = 12
        self.gameMatrix[37] = -7
        self.gameMatrix[38] = 6
        self.gameMatrix[43] = -2


    def create_board(self):

        self.table_board.hideturtle()
        Board.define_Cube(self)
        #x, y = 270, 200
        start_x = self.x
        # start_y = y
        count = 0
        num = 50
        First_row, Second_row = True, False

        while (count < N * N):
            self.table_board.hideturtle()

            self.gameMatrix.append(0)
            self.Placing_Board.append([])
            self.table_board.penup()
            self.table_board.goto(self.x, self.y)
            self.table_board.pendown()
            self.x -= SIZE

            if First_row == True:
                num -= 1
            if Second_row == True:
                num += 1
            self.table_board.write(num, align='right', font=("Times", int((font_size * 5 + 4) / 4), "bold"))
            self.Placing_Board[count].append(num)
            self.Placing_Board[count].append(self.x)
            self.Placing_Board[count].append(self.y)

            count += 1
            box()

            if self.x <= -(SIZE * N - start_x):
                self.x = start_x
                self.y -= SIZE
                self.table_board.penup()
                if First_row:
                    First_row = False
                    Second_row = True
                    num = num - (N + 1)

                else:
                    First_row = True
                    Second_row = False
                    num = num - (N - 1)

                if self.y <= -(SIZE * N - 50):
                    break
        Board.define_BoardGame(self)




class Player():

    players = []
    Player_Color=[]
    Player_Location = []

    def __init__(self, start_x, start_y,NUM_OF_PLAYERS):
        self.start_x = start_x
        self.start_y = start_y
        self.NUM_OF_PLAYERS = NUM_OF_PLAYERS




    def def_player(self, player, color):

        player.pendown()
        player.shape('circle')
        player.begin_fill()
        player.fillcolor(color)
        player.circle(SIZE / N)
        player.end_fill()
        player.penup()

    def create_player(self):

            for i in range(self.NUM_OF_PLAYERS):

                self.Player_Location.append(0)
                self.players.append(turtle.Turtle())
                self.players[i].penup()
                self.Player_Color.append(0)

                self.start_y -= 10

                if i == 0:
                    self.players[i].goto(self.start_x, self.start_y)
                    Player.def_player(self,self.players[i], "red")
                    self.Player_Color[i] = "red"

                elif i == 1:
                    self.players[i].goto(self.start_x, self.start_y)
                    Player.def_player(self,self.players[i], "green")
                    self.Player_Color[i] = "green"

                elif i == 2:
                    self. players[i].goto(self.start_x, self.start_y)
                    Player.def_player(self, self.players[i], "blue")
                    self.Player_Color[i] = "blue"

                else:
                    self.players[i].goto(self.start_x, self.start_y)
                    Player.def_player(self,self.players[i], "black")
                    self.Player_Color[i] = "black"



class ControllerGame():

    def __init__(self):
        print

    def setPlayerPostion(self, player, i):

        j = 1
        for j in range(N * N):
            if Player.Player_Location[i] == Board.Placing_Board[j][0]:
                player.setx(Board.Placing_Board[j][1] + (SIZE / 2))
                player.sety(Board.Placing_Board[j][2] + (SIZE / 2))

                ControllerGame.check_positions(self, i)
                break

    def Play_Cube(self, num, i):

        Board.table_board.pencolor(Player.Player_Color[i])
        Board.table_board.penup()
        Board.table_board.goto(-4*SIZE+5, - 2 * SIZE + 10)
        Board.table_board.write(num, align='right', font=("Times", int((font_size * 5 + 7) / 4), "bold"))
        Board.table_board.undo()
        time.sleep(3)
        Board.table_board.undo()

    def check_positions(self, i):


        if len(Player.players) <=1:
            return

        if i == 0 and i < len(Player.players) - 1:
            if Player.players[i].pos() == Player.players[i + 1].pos():
                Player.players[i].sety(Player.players[i].ycor() + 20)


            elif i + 1 < len(Player.players) - 1:
                j = i + 2
                for j in range(len(Player.players) - 1):
                    if Player.players[i].pos() == Player.players[j].pos():
                        Player.players[i].sety(Player.players[i].ycor() + 20)

        else:
            if len(Player.players) > 2:
                if i + 1 <= len(Player.players) - 1 and Player.players[i].pos() == Player.players[i + 1].pos():
                    Player.players[i].sety(Player.players[i + 1].ycor() - 20)

                if i + 2 <= len(Player.players) - 1 and Player.players[i].pos() == Player.players[i + 2].pos():
                    Player.players[i].sety(Player.players[i + 2].ycor() - 20)

                if i - 1 != 0 and Player.players[i].pos() == Player.players[i - 1].pos():
                    Player.players[i].sety(Player.players[i].ycor() - 20)

    def winner_Flow(self, i):

        print ("WINNER IS = ", i)
        print (Player.Player_Color[i])
        Board.table_board.setheading(0)
        Board.table_board.goto(270, 200)
        Board.table_board.begin_fill()
        Board.table_board.pendown()
        box()
        Board.table_board.fillcolor(Player.Player_Color[i])
        Board.table_board.goto(270, 240)
        Board.table_board.pencolor("white")

        winner_str = " winner is " + str(i)

        Board.table_board.write(winner_str, align='right', font=("Times", int((font_size * 4 + 7) / 4), "bold"))
        Board.table_board.penup()
        Board.table_board.end_fill()

    def move_player(self):

        for i in range(len(Player.players)):
            global is_over

            num = random.randint(1, 6)
            Player.Player_Location[i] += num

            ControllerGame.Play_Cube(self, num, i)

            if Player.Player_Location[i] > N * N:
                dis = Player.Player_Location[i] - N * N
                Player.Player_Location[i] = N * N - dis

            ControllerGame.setPlayerPostion(self,Player.players[i], i)

            if Board.gameMatrix[Player.Player_Location[i] - 1] != 0:
                time.sleep(2)
                Player.Player_Location[i] += Board.gameMatrix[Player.Player_Location[i] - 1]
                ControllerGame.setPlayerPostion(self,Player.players[i], i)

            if Player.Player_Location[i] == N * N:
                ControllerGame.winner_Flow(self,i)
                is_over = True
                return



if __name__=="__main__":
#def main():

    START_X = -4*SIZE
    START_Y = -3*SIZE +10

    gameBoard = Board(3*SIZE +30, 2*SIZE + SIZE/2)
    #gameBoard.create_board()
    from create_extra_items import create_Ladders
    create_Ladders(gameBoard.table_board, gameBoard.Placing_Board)

    # print ("Enter Num Of Players (between 1-4)")
    # NUM_OF_PLAYERS = input()

    # while(NUM_OF_PLAYERS > 4 or NUM_OF_PLAYERS <1):
    #  print("Wrong Number, try again (between 1-4)")
    # print ("Enter Number Of Players (between 1-4)")
    # NUM_OF_PLAYERS = input()


    NUM_OF_PLAYERS  = 4

    Player(START_X, START_Y, NUM_OF_PLAYERS).create_player()

    StartGame = ControllerGame()

    while not is_over:
        StartGame.move_player()

    print("End")

    gameBoard.table_board.hideturtle()

#main()
turtle.done()


