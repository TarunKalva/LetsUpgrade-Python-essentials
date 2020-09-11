#!/usr/bin/env python
# coding: utf-8

# # Rock Paper and Scissor game

# In[17]:


def take_player_input():
    player='something'
    while player!='r' and player!='p' and player!='s':
        player=input('Enter the input as R or P or S:')
    return player.lower()    


# In[18]:


import random
def bot_input():
    lst=['r','p','s']
    bot_choice=random.choice(lst)
    return bot_choice


# In[19]:


def check_winner(player,bot):
    if player=='r' and bot=='r':
        return 'draw'
    elif player=='r' and bot=='p':
        return 'bot'
    elif player=='r' and bot=='s':
        return 'player'
    elif player=='p' and bot=='r':
        return 'player'
    elif player=='p' and bot=='p':
        return 'draw'
    elif player=='p' and bot=='s':
        return 'bot'
    elif player=='s' and bot=='r':
        return 'bot' 
    elif player=='s' and bot=='p':
        return 'player'
    elif player=='s' and bot=='s':
        return 'draw' 


# In[35]:


endgame='n'
player_score=0
bot_score=0
name=input('Enter the name:')
while endgame!='y':
    palyer=take_player_input()
    bot=bot_input()
    print('The bot input is:',bot)
    winner=check_winner(player,bot)
    if winner=='player':
        pwin=name
    else:
        pwin='bot'
    print('The winner of this round is:',pwin)
    if winner=='player':
        player_score+=2
    elif winner=='bot':
        bot_score+=2
    else:
        player_score+=1
        bot_score+=1
    print('---Score Board---')
    print(name,':',player_score)
    print('bot:',bot_score)
    endgame=input('do you want to end the game y/n:').lower()
if player_score>bot_score:
    print('The Winner is',name)
elif player_score==bot_score:
    print('match is drawn')
else:
    print('Winner is bot')
    


# In[ ]:




