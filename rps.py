import random

def play():
    my_move = input('rock, paper or scissor? \n')
    npc_move= random.choice(['r','p','s'])

    if my_move == npc_move:
        return 'its a draw you chose {} while the opponent chose {}'.format(my_move,npc_move)

    if youWin(my_move, npc_move):                                                           # if true you win
        return 'You Win you chose {} while the opponent chose {}'.format(my_move,npc_move)

    return 'You Lost you chose {} while the opponent chose {}'.format(my_move,npc_move)     # else false means you lost


def youWin(player, opponent):
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True

print(play())

    




