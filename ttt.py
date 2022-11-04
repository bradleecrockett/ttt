#import the pygame and sys modules
import pygame
import sys

# import the builtin local variables from pygame
from pygame.locals import *


# helper functions
'''
@param a list of 9 elements representing a tictactoe board 
        filled with "X", "O" or " " characters
@return a string either 'X', 'O' if there is a 3 in a row
        or a space character ' ' when no winner exists
'''
def check_winner(ttt_board):
    for quadr in (0,3,6):
        if ttt_board[quadr]==ttt_board[quadr+1] and ttt_board[quadr+1] == ttt_board[quadr+2]:
            return ttt_board[quadr]
    for quadr in range(3):
        if ttt_board[quadr]==ttt_board[quadr+3] and ttt_board[quadr+3] == ttt_board[quadr+6]:
            return ttt_board[quadr]
    if (ttt_board[0]==ttt_board[4] and ttt_board[4] == ttt_board[8]) or (ttt_board[2]==ttt_board[4] and ttt_board[4] == ttt_board[6]):
        return ttt_board[4]
    return ' '



def get_cell_from_xy(x,y):
    if y<150:
        if x <150:
            return 0
        elif x <250:
            return 1
        else:
            return 2
    elif y<250:
        if x <150:
            return 3
        elif x <250:
            return 4
        else:
            return 5
    else:
        if x <150:
            return 6
        elif x <250:
            return 7
        else:
            return 8







def main():
    # initialize pygame
    pygame.init()
    # Create the window 400px,400px     w,  h
    screen = pygame.display.set_mode((400, 400))
    FRAMERATE = 30 # fps
    clock = pygame.time.Clock()
    pygame.display.set_caption('Tic Tac Toe')

    # define some colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)

    # load some images for later display
    o_img = pygame.image.load("o.png")
    x_img = pygame.image.load("x.png")


    # draw the tictac toe lines
    #      draw.line( where, color,  start_pt,  end_pt, thickness)
    pygame.draw.line(screen, WHITE, [150, 50], [150, 350], 5)
    pygame.draw.line(screen, WHITE, [250, 50], [250, 350], 5)
    pygame.draw.line(screen, WHITE, [50, 150], [350, 150], 5)
    pygame.draw.line(screen, WHITE, [50, 250], [350, 250], 5)

    

    #Set up font for displaying whos turn it is / winner messages
    pygame.font.init()
    font = pygame.font.SysFont("comicsansms", 25)


    # Set up the tictac to board and the player list
    # and turn number
    board = []
    for i in range(9):
        board.append(" ")
    players = ["X","O"]
    turn = 0
    game_on = True
    

    # main pygame loop
    # check for user input (events)
    # update game state based on events
    # redraw the screen
    while True:
        # look for user input events
        for event in pygame.event.get():
            if event.type == QUIT:#click the x in the rt corner of the window
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP: #key pressed
                # print(event.key)
                if(event.key == K_r):
                    main()
                else:
                    print("Invalid Key. Press 'r' to restart the game")
            elif event.type == MOUSEBUTTONUP and game_on: #release the mouse button
                mousex, mousey = event.pos
                cell = get_cell_from_xy(mousex,mousey) # see above
                # print(mousex, mousey, cell, turn)
                # print(board)
                if board[cell]==" ":
                    board[cell] = players[turn%2]
                    # print(board)
                    # print(turn, mousex, mousey, cell)
                    if(turn%2 == 0):
                        screen.blit(x_img, ((cell%3+1)*100-32, (cell//3+1)*100-32))
                    else:
                        screen.blit(o_img, ((cell%3+1)*100-32, (cell//3+1)*100-32))
                    turn += 1
                    winner = check_winner(board)
                    if winner == "X":
                        print("X Wins!!")
                    elif winner == "O":
                        print("O Wins")
                    elif turn >8:
                        print("Cats game")
        winner = check_winner(board)
        
        game_on = turn < 9 and check_winner(board) == " "
        if turn > 8:
            msg = "Cats Game. Press 'r' to play again"
        elif winner=="X":
            msg = "X Wins! Press 'r' to play again"
        elif winner == "O":
            msg = "O Wins! Press 'r' to play again"
        else:
            msg = players[turn%2] + "'s run, click on a cell."

        
        # render the msg into text to be displayed
        text = font.render(msg, True, RED)
        # draw a rectangle over the old text
        pygame.draw.rect(screen, BLACK, (100,20,300,40))
        # stamp the text on the screen
        screen.blit(text, (100, 20))

        # redraw the screen
        pygame.display.update()
        clock.tick(FRAMERATE)
    

if __name__=="__main__":
    main()
    



    

if __name__ == "__main__":
    main()