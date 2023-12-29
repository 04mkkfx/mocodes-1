import random #creating a rock/paper/scissor game.

while True:
    options = ['rock','paper','scissors']
    computer = random.choice(options)
    player = ''

    while player not in options:
        player=input('rock,paper or scissors: ')
        print('AI:', computer)
        print('PLAYER:', player)

    if player == computer:
        print('TIE!')

    elif player =='scissors':
        computer == 'rock'.lower()
        print('YOU LOSE!')

    elif player =='rock'.lower():
        computer == 'paper'.lower()
        print('WINNER')

    elif player == 'paper':
        computer =='rock'
        print('WINNER!')

    elif player =='scissors':
        computer =='paper'
        print('WINNER!')

    again = input('play again? (yes/no): ').lower()
    if again !='yes':
       break

print("Bye!")


