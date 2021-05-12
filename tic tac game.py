#display the game with 9 positions for x and o
#first player to start and the board need to be empty
#numbered cell for each player turn
#error msg placing a number in filled place
#players scores a line of three symbol you won


the_board={'1': ' ','2': ' ', '3': ' ',
           '4': ' ','5': ' ','6': ' ',
           '7': ' ','8': ' ','9': ' '}

boardkeys=[]

for key in the_board:
    boardkeys.append(key)

def printboard(board):
    print(board['1']+'/'+board['2']+'/'+board['3'])
    print('-+-+-')
    print(board['4'] + '/' + board['5'] + '/' + board['6'])
    print('-+-+-')
    print(board['7'] + '/' + board['8'] + '/' + board['9'])
    print('-+-+-')

#printboard(the_board)

def game():
    turn = 'X'
    count=0 #0 because count starts from 0

    for i in range(10): #i is for the items or some items you entered
        printboard(the_board)
        print('it is your turn ' + turn + ' '+ 'specify the place you want to go')
        move = input() #user input and move stands for turn
        if the_board[move]==' ':
           the_board[move]= turn
           count+=1 #increase the count
        else:
            print('sorry this location is filled choose the another one ')
            continue
        if count >=5:
            if the_board['1']==the_board['2']==the_board['3'] !=' ':
                printboard(the_board)
                print('\ngame over\n')
                print('player' + turn + 'won the game')
                break
            if the_board['4']==the_board['5']==the_board['6'] !=' ':
                printboard(the_board)
                print('\ngame over\n')
                print('player' +turn + 'won the game')
                break
            if the_board['7']==the_board['8']==the_board['9'] !=' ':
                printboard(the_board)
                print('\ngame over\n')
                print('player' + turn + 'won the game')
                break
            if the_board['7']==the_board['4']==the_board['1'] !=' ':
                printboard(the_board)
                print('\ngame over\n')
                print('player' + turn + 'won the game')
                break
            if the_board['8']==the_board['5']==the_board['2'] !=' ':
                printboard(the_board)
                print('\ngame over\n')
                print('player' + turn + 'won the game')
                break
            if the_board['9']==the_board['6']==the_board['3'] !=' ':
                printboard(the_board)
                print('\ngame over\n')
                print('player' + turn + 'won the game')
                break
            if the_board['9']==the_board['5']==the_board['1'] !=' ':
                printboard(the_board)
                print('\ngame over\n')
                print('player' + turn + 'won the game')
                break
            if the_board['7']==the_board['5']==the_board['3'] !=' ':
                printboard(the_board)
                print('\ngame over\n')
                print('player' + turn + 'won the game')
                break

        if count==9:
            print('\n game over\n')
            print('this game is a tie!')
        if turn=='X':
            turn='0'
        else:
            turn='X'
    restart=input('do you want to start the game ? (y/n)')
    if restart=='y'or restart=='n':
        for key in boardkeys:
                the_board[key]=' '
        game()#recurssive function

if __name__=='__main__':
    game()