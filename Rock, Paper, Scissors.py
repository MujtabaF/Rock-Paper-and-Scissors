from random import randint
lives = 10
print("Welcome to rock paper scissors " )
for chance in range(lives):

    player = input('rock (r), paper (p) or scisors(s)?')
    chosen = randint(1,3)
    

    if chosen == 1:
        computer = 'r'

    elif chosen == 2:
        computer = 's'

    else: 
        computer = 'p'
    print("The battle is between ", player, 'vs', computer)
    if player == computer:
        print('DRAW')
    elif player == 'r' and computer == 's':
        print('PLAYER WINS')
    elif player == 'r' and computer == 'p':
        print('COMPUTER WINS')
    elif player == 'p' and computer == 'r':
        print('PLAYER WINS')
    elif player == 'p' and computer == 's':
        print('COMPUTER WINS')
    elif player == 's' and computer == 'p':
        print('PLAYER WINS')
    elif player == 's' and computer == 'r':
        print('COMPUTER WINS')


