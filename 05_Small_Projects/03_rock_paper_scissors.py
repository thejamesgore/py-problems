# Make a game of rock paper scissors

import random

def shoot():
    print('Lets play Rock, Paper, Sciossors!')
    user = input("Input 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

# r > s, s > p, p > r
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(shoot())