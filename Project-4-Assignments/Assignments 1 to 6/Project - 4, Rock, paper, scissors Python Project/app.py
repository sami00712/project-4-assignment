import random

def play():
    user = input(" Choose your Choice, 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p','s'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You Won!'
    
    return 'you lost!!'

def is_win(player, opponent):
    # give us true if player wins
    # rock >  scissors,  scissors > paper, paper > rock

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print (play())

