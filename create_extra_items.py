import turtle

N =7
SIZE = 80
ANGLE = 90

def def_sankes(i, x, y, radius, color,t_board):

    y = y + 20
    x = x +10

    t_board.penup()
    t_board.begin_fill()
    t_board.goto(x, y)
    t_board.fillcolor(color)
    t_board.circle(radius)
    t_board.pendown()
    t_board.end_fill()

def create_snaks(t_board,P_Board):

    for i in range(N-1):

        ### FROM 10 TO 5
        if i==0:
            ###  1  ### -- UP

            a_x = P_Board[N*N-10][1]+2*SIZE
            b_y = P_Board[N*N-10][2]
            def_sankes(i,a_x +20, b_y, 15,"aquamarine",t_board)
            ###  2  ### -- UP
            def_sankes(i, a_x + 23, b_y-10, 10, "black",t_board)
            ###  3  ### -- UP
            def_sankes(i, a_x +20, b_y - 22, 7, "aquamarine",t_board)
            ###  4  ### -- UP
            def_sankes(i, a_x+17, b_y -30, 7, "black",t_board)
            ###  5  ### -- UP
            def_sankes(i, a_x +20 ,b_y - 40, 7, "aquamarine",t_board)
            ###  6  ### -- UP
            def_sankes(i, a_x + 30,  b_y - 35, 7, "black",t_board)
            ### 7  ### -- UP
            def_sankes(i, a_x + 40, b_y - 30, 8, "aquamarine",t_board)
            ###  8  ### -- UP
            def_sankes(i, a_x + 45, b_y - 34, 5, "black",t_board)

        ### FROM 13 TO 1
        elif i==1:

            a_x = P_Board[N*N-10][1]-SIZE
            b_y = P_Board[N*N-13][2]

            ###  1  ### -- UP
            def_sankes(i,a_x+20, b_y,15,"brown",t_board)

            ###  2  ### -- UP
            b_y = P_Board[N * N - 10][2]
            def_sankes(i, a_x+23, b_y-10, 10, "black",t_board)
            ###  3  ### -- UP
            def_sankes(i, a_x+20,b_y - 22, 7, "brown",t_board)
            ###  4  ### -- UP
            def_sankes(i, a_x+23, b_y - 30, 7, "black",t_board)
            ###  5  ### -- UP
            def_sankes(i, a_x+20, b_y - 40, 7, "brown",t_board)
            ###  6  ### -- UP
            def_sankes(i, a_x+8, b_y - 35, 7, "black",t_board)
            ### 7  ### -- UP
            def_sankes(i, a_x-2, b_y -30, 8, "brown",t_board)
            ###  8  ### -- UP
            def_sankes(i, a_x-13, b_y - 34, 6, "black",t_board)

         ### FROM 44 TO 42
        elif i == 2:

            a_x = P_Board[N * N - 10][1] - SIZE
            b_y = P_Board[N * N - 13][2] +5*SIZE
            ###  1  ### -- UP
            def_sankes(i, a_x+20, b_y, 15, "yellow",t_board)
            ###  2  ### -- UP
            def_sankes(i, a_x + 17, b_y - 10, 10, "black",t_board)
            ###  3  ### -- UP
            def_sankes(i, a_x + 20, b_y - 22, 7, "yellow",t_board)
            ###  4  ### -- UP
            def_sankes(i, a_x + 23, b_y - 30, 7, "black",t_board)
            ###  5  ### -- UP
            def_sankes(i, a_x + 20, b_y - 40, 7, "yellow",t_board)
            ###  6  ### -- UP
            def_sankes(i, a_x + 8, b_y-35, 7, "black",t_board)
            ### 7  ### -- UP
            def_sankes(i, a_x - 2, b_y - 30, 8, "yellow",t_board)
            ###  8  ### -- UP
            def_sankes(i, a_x - 13, b_y - 34, 6, "black",t_board)

        ### FROM 34 TO 24
        elif i == 3:

            a_x = P_Board[N * N - 10][1]+ 20 +3*SIZE
            b_y = P_Board[N * N - 13][2] + 3 * SIZE
            ###  1  ### -- UP
            def_sankes(i, a_x+ 20,  b_y, 15, "DeepPink",t_board)
            ###  2  ### -- UP
            def_sankes(i, a_x + 17, b_y - 10, 10, "black",t_board)
            ###  3  ### -- UP
            def_sankes(i, a_x + 20, b_y - 22, 7, "DeepPink",t_board)
            ###  4  ### -- UP
            def_sankes(i, a_x + 17, b_y - 30, 7, "black",t_board)
            ###  5  ### -- UP
            def_sankes(i, a_x + 17, b_y - 39, 8, "DeepPink",t_board)
            ###  6  ### -- UP
            def_sankes(i, a_x + 10, b_y - 47, 7, "black",t_board)
            ### 7  ### -- UP
            def_sankes(i, a_x, b_y - 47, 7, "DeepPink",t_board)
            ###  8  ### -- UP
            def_sankes(i, a_x - 10, b_y - 38, 8, "black",t_board)
            ### 9  ### -- UP
            def_sankes(i, a_x-20, b_y - 29, 7, "DeepPink",t_board)
            ###  10  ### -- UP
            def_sankes(i, a_x - 30, b_y - 20, 7, "black",t_board)
            ### 11  ### -- UP
            def_sankes(i, a_x - 37, b_y - 29, 6, "DeepPink",t_board)
            ###  12  ### -- UP
            def_sankes(i, a_x -43, b_y - 35, 5, "black",t_board)


         ### FROM 38 TO 31
        elif i == 4:
            ###  1  ### -- UP

            a_x = P_Board[N * N - 10][1] + 2 * SIZE
            b_y = P_Board[N * N - 13][2] + 4 * SIZE
            def_sankes(i, a_x+20, b_y, 15, "DarkGray",t_board)
            ###  2  ### -- UP
            def_sankes(i, a_x + 17,b_y - 10, 10, "black",t_board)
            ###  3  ### -- UP
            def_sankes(i, a_x + 20, b_y - 22, 7, "DarkGray",t_board)
            ###  4  ### -- UP
            def_sankes(i, a_x + 17, b_y - 30 , 7, "black",t_board)
            ###  5  ### -- UP
            def_sankes(i, a_x + 15, b_y - 39, 6, "DarkGray",t_board)
            ###  6  ### -- UP
            def_sankes(i, a_x + 10,b_y - 40, 9, "black",t_board)
            ### 7  ### -- UP
            def_sankes(i, a_x, b_y - 47, 8, "DarkGray",t_board)
            ###  8  ### -- UP
            def_sankes(i, a_x - 10, b_y - 38, 7, "black",t_board)
            ### 9  ### -- UP
            def_sankes(i, a_x - 20, b_y - 29 , 8, "DarkGray",t_board)
            ###  10  ### -- UP
            def_sankes(i, a_x - 30, b_y - 30, 7, "black",t_board)
            ### 11  ### -- UP
            def_sankes(i, a_x - 40, b_y - 29, 7, "DarkGray",t_board)
            ###  12  ### -- UP
            def_sankes(i, a_x - 50, b_y - 38, 8, "black",t_board)
            ### 13  ### -- UP
            def_sankes(i, a_x - 60, b_y - 47, 7, "DarkGray",t_board)
            ###  14  ### -- UP
            def_sankes(i, a_x - 70, b_y - 38, 8, "black",t_board)
            ### 15  ### -- UP
            def_sankes(i, a_x - SIZE, b_y - 29, 9, "DarkGray",t_board)
            ###  16  ### -- UP
            def_sankes(i, a_x - SIZE - 10, b_y - 30, 7, "black",t_board)
            ### 17  ### -- UP
            def_sankes(i, a_x - SIZE - 20,b_y - 29, 8, "DarkGray",t_board)
            ###  18  ### -- UP
            def_sankes(i, a_x - SIZE - 28, b_y - 36, 6, "black",t_board)

        ### FROM 26 TO 11
        else:

            a_x = P_Board[N * N - 10][1]
            b_y = P_Board[N * N - 13][2]+ 2*SIZE
            ###  1  ### -- UP
            def_sankes(i, a_x +20, b_y, 15, "DarkOrange",t_board)
            ###  2  ### -- UP
            def_sankes(i, a_x+ 17, b_y - 10, 10, "black",t_board)
            ###  3  ### -- UP
            def_sankes(i, a_x+ 20,b_y - 22, 7, "DarkOrange",t_board)
            ###  4  ### -- UP
            def_sankes(i, a_x+26, b_y - 30, 7, "black",t_board)
            ###  5  ### -- UP
            def_sankes(i, a_x+35, b_y - 25, 7, "DarkOrange",t_board)
            ###  6  ### -- UP
            def_sankes(i, a_x+45, b_y - 30, 7, "black",t_board)
            ### 7  ### -- UP
            def_sankes(i, a_x + 55, b_y - 35, 7, "DarkOrange",t_board)
            ###  8  ### -- UP
            def_sankes(i, a_x + 65, b_y - 30, 7, "black",t_board)
            ### 9  ### -- UP
            def_sankes(i, a_x + 75, b_y - 25, 7, "DarkOrange",t_board)
            ###  10  ### -- UP
            def_sankes(i, a_x + SIZE +5, b_y - 30, 7, "black",t_board)
            ### 11  ### -- UP
            def_sankes(i, a_x + SIZE +5, b_y -35, 7, "DarkOrange",t_board)
            ###  12  ### -- UP
            def_sankes(i, a_x + SIZE + 5, b_y - 45, 7, "black",t_board)
            ### 13  ### -- UP
            def_sankes(i, a_x + SIZE, b_y - 55, 7, "DarkOrange",t_board)
            ###  14  ### -- UP
            def_sankes(i, a_x + SIZE + 5, b_y - 65, 7, "black",t_board)
            ### 15  ### -- UP
            def_sankes(i, a_x + SIZE +10, b_y - 75, 7, "DarkOrange",t_board)
            ###  16  ### -- UP
            def_sankes(i, a_x + SIZE + 5, b_y - SIZE -5, 7, "black",t_board)
            ### 17  ### -- UP
            def_sankes(i, a_x + SIZE, b_y - SIZE -15, 7, "DarkOrange",t_board)
            ###  18  ### -- UP
            def_sankes(i, a_x + SIZE + 5, b_y - SIZE - 25, 7, "black",t_board)
            ### 19  ### -- UP
            def_sankes(i, a_x + SIZE+10, b_y - SIZE - 35, 7, "DarkOrange",t_board)
            ###  20  ### -- UP
            def_sankes(i,  a_x + SIZE + 14,b_y - SIZE - 35, 6, "black",t_board)
        t_board.hideturtle()


def def_lines(i, a_x ,b_y, heading,go_forward, t_board):

    t_board.penup()
    t_board.goto(a_x, b_y)
    t_board.pendown()
    t_board.setheading(heading)
    t_board.forward(go_forward)
    t_board.hideturtle()



def create_Ladders(t_board, P_Board):


    for i in range(N):

        t_board.color("Green")

        # Setting Up width to 2
        t_board.width("4")
        # Setting up speed to 2
        t_board.speed(0)

        #### FROM 3 TO 12
        if i ==0:
            # code for inner lines of the square

            a_x = (P_Board[N * N - 4][1] - (SIZE // 2) - SIZE / 3)
            b_y = (P_Board[N * N - 13 - SIZE // 2][2] + SIZE / 2)

            ### 1 ####  ---- up line
            def_lines(i, a_x, b_y +55 ,0, 36,t_board)
            ### 2 ####  ---- middle line
            def_lines(i, a_x, b_y+ 30, 0, 36,t_board)
            ### 3 ####  ---- down line
            def_lines(i, a_x, b_y+5,0, 36,t_board)
            ### 3 ####  ---- left line
            def_lines(i, a_x, b_y - 20, ANGLE, 100,t_board)
            ### 4 ####  ---- right line
            def_lines(i, a_x +SIZE / 3+ 10,b_y-20, ANGLE, 100,t_board)

        #### FROM 14 TO 28
        if i == 1:
            # code for inner lines of the square

            a_x = (P_Board[N * N - 14][1]) - 6 * SIZE +10
            b_y = (P_Board[N * N - 29 - SIZE // 2][2]) + SIZE / 2 - 20

            ### 1 ####  ---- up line
            def_lines(i, a_x, b_y + SIZE, 0, 44,t_board)
            ### 2 ####  ---- up 2 line
            def_lines(i, a_x, b_y+45 , 0, 44,t_board)
            ### 3 ####  ---- middle line
            def_lines(i, a_x, b_y+10, 0, 44,t_board)
            ### 4 ####  ---- middle down
            def_lines(i, a_x,b_y-20, 0, 44,t_board)
            ### 5 ###  ---- down line
            def_lines(i, a_x, b_y-50, 0, 44,t_board)
            ### 6 ####  ---- left
            def_lines(i, (P_Board[N * N - 14][1] - SIZE / 3) - 5 * SIZE,b_y-SIZE, ANGLE, 180,t_board)
            ### 7 ####  ---- right
            def_lines(i, (P_Board[N * N - 13][1] + 10)-5*SIZE, b_y-SIZE,ANGLE, 180,t_board)

        ### from 6 to 8 ###
        if i ==2:
            # code for inner lines of the square
            a_x = (P_Board[N * N - 6][1])
            b_y =(P_Board[N * N - 6][2])


            ### 1 ####  ---- middle line 1
            def_lines(i,a_x+SIZE,b_y+SIZE,-ANGLE/2, 22,t_board)
            ### 2 ####  ---- middle line 2
            def_lines(i, a_x+SIZE +20 ,b_y + SIZE + 20,-ANGLE/2, 22,t_board)
            ### 3 ####  ---- middle line 3
            def_lines(i, a_x+SIZE -20 ,b_y + SIZE-20,-ANGLE/2, 22,t_board)
            ### 4 ####  ---- right line
            def_lines(i, a_x+SIZE/2,b_y+SIZE/2,ANGLE/2, 100,t_board)
            ### 5 ####  ---- left line
            def_lines(i, a_x + SIZE/2 + 20,b_y + SIZE/3,ANGLE/2, 100,t_board)

        ### from 27 to 31
        if i==3:

            a_x = (P_Board[N * N - 27][1]) -4*SIZE
            b_y = (P_Board[N * N - 27][2])
            # code for inner lines of the square
            ### 1 ####  ---- middle line 1
            def_lines(i, a_x + SIZE, b_y + SIZE, -ANGLE/2,22,t_board)
            ### 2 ####  ---- middle line 2
            def_lines(i, a_x + SIZE + 20, b_y + SIZE + 20, -ANGLE/2, 22,t_board)
            ### 3 ####  ---- middle line 3
            def_lines(i, a_x + SIZE - 20,b_y + SIZE - 20, -ANGLE/2, 22,t_board)
            ### 4 ####  ---- right line
            def_lines(i, a_x + SIZE / 2,b_y + SIZE / 2, ANGLE/2, 100,t_board)
            ### 5 ####  ---- left line
            def_lines(i, a_x + SIZE / 2 + 20, b_y+ SIZE / 3, ANGLE/2, 100,t_board)

        ### from 39 to 45
        if i==4:
            # code for inner lines of the square
            ### 1 ####  ---- dowm line 1

            a_x = (P_Board[N * N - 39][1]) + SIZE/2
            b_y = (P_Board[N * N - 39][2])

            def_lines(i, a_x-30, b_y+ SIZE/2+9, ANGLE/2,  32,t_board)
            ### 2 ####  ---- up line 2
            def_lines(i, a_x-80, b_y+ SIZE + 20, ANGLE/2, 32,t_board)
            ### 3 ####  ---- middle line 3
            def_lines(i, a_x-50,b_y + SIZE-10, ANGLE/2, 32,t_board)
            ### 4 ####  ---- right line
            def_lines(i, a_x-20, b_y + SIZE / 2,ANGLE+ ANGLE/2, 100,t_board)
            ### 5 ####  ---- left line
            def_lines(i, a_x+ 7, b_y + SIZE / 3+33, ANGLE+ANGLE/2, 105,t_board)

        ### from 18 to 33
        if i==5:
            # code for inner lines of the square
            a_x = P_Board[N * N - 18][1]
            b_y = (P_Board[N * N - 18][2])

            ### 1 ####  ---- up line 1
            def_lines(i, a_x + SIZE +10, b_y + SIZE + 100,-ANGLE/2+20, 33,t_board)
            ### 2 ####  ---- middle line 2
            def_lines(i, a_x + SIZE -12,b_y + SIZE + 50, -ANGLE/2+20, 33,t_board)
            ### 3 ####  ---- down line 3
            def_lines(i,a_x + SIZE - 34,b_y + SIZE, -ANGLE/2+20, 33,t_board)
            ### 4 ####  ---- right line
            def_lines(i,a_x + SIZE / 2-10,b_y + SIZE / 2, (ANGLE+ANGLE/2)/2, 200,t_board)
            ### 5 ####  ---- left line
            def_lines(i,a_x + SIZE / 2 + 20,b_y+ SIZE / 3, (ANGLE+ANGLE/2)/2, 200,t_board)


        ### from 35 to 47
        if i==6:
            # code for inner lines of the square
            a_x = P_Board[N * N - 35][1]
            b_y = P_Board[N * N - 35][2]

            ### 1 ####  ---- up line 1
            def_lines(i, a_x - SIZE-35, b_y+ SIZE + 86, ANGLE / 2, 40,t_board)
            ### 1 ####  ---- up line 1
            def_lines(i, a_x - SIZE-15, b_y + SIZE + 65, ANGLE / 2, 40,t_board)
            ### 1 ####  ---- up line 1
            def_lines(i,a_x - SIZE-1, b_y + SIZE + 50, ANGLE / 2, 40,t_board)
            ### 1 ####  ---- up line 1
            def_lines(i, a_x -62, b_y + SIZE + 30, ANGLE/2, 40,t_board)
            ### 2 ####  ---- middle line 2
            def_lines(i,a_x -43,b_y + SIZE+10, ANGLE/2, 40,t_board)
            ### 3 ####  ---- middle down line 3
            def_lines(i, a_x - 12,b_y + SIZE -20, ANGLE/2, 40,t_board)
            ### 4 ####  ---- down line 3
            def_lines(i,a_x + 7, b_y + SIZE - 40, ANGLE / 2, 40,t_board)
            ### 5 ####  ---- left line
            def_lines(i, a_x + SIZE / 2-20, b_y + SIZE / 3, ANGLE+ANGLE/2, 220,t_board)
            ### 6 ####  ---- right line
            def_lines(i, a_x + SIZE / 2 + 17,b_y + SIZE/2+ 8, ANGLE+ANGLE/2, 230,t_board)
    create_snaks(t_board,P_Board)


