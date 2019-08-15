#This program plays a game of pokemon

import random #imports the module random

def make_move_list():
    """
    makes the move list
    @returns the move list
    """
    move1 = [1, 'Tackle', 0.9, 0.05]
    move2 = [2, 'High Jump Kick', 0.75, 0.05]
    move3 = [3, 'Desperate Blow', 0.1, 0.05]
    move4 = [4, 'Slack Off', 0.95, 0.05]
    move_list = [move1,move2,move3,move4]
    return move_list

def display_movelist(move_list):
    """
    Just displays the move list
    @move_list is the move list
    """
    print('%d. %s' % (move_list[0][0],move_list[0][1]))
    print('%d. %s' % (move_list[1][0],move_list[1][1]))
    print('%d. %s' % (move_list[2][0],move_list[2][1]))
    print('%d. %s' % (move_list[3][0],move_list[3][1]))
    
    
def display_monster1(monster1,monster1_hp):
    """
    Displays monster 1 and its remaining hit points
    @monster1 is the 1st monster
    @monster1_hp is its hp
    """
    print('%s has %d hit points remaining.' % (monster1,monster1_hp))
    

def display_monster2(monster2,monster2_hp):
    """
    Displays monster 2 and its remaining hit points
    @monster2 is the 2nd monster
    @monster2_hp is its hp
    """    
    print('%s has %d hit points remaining.' % (monster2,monster2_hp))

def whos_move(turn,players):
    """
    Displays whos move it is and to choose a move
    @turn is whos turn it is
    @players is the current player
    """
    print('Choose a move for %s.' % (players[turn]))
    
def get_move(player,move_list):
    """
    Gets the move from player
    Checks valid input for the entered move
    @player is the player
    @move_list is the move list
    @returns the move
    """
    while True:
        move = input('Enter your move: ')
        if move.isdigit() and int(move) <= 4:#if is a digit and is one of the options
            return move
        if len(move) == 0:#if no input is given it continues
            return move
        else:#When invalid loops back and gets move
            print('Choose a move for %s.' % (player))
            display_movelist(move_list)
            move = get_move(player,move_list)
            return move
        
def make_move(player_turn,player_not_turn,hp1,hp2,move,move_list):
    """
    Makes the current move based on which move is chosen
    @player_turn is the player making the move
    @player_not_turn is the other player
    @hp1 is player making the moves hp
    @hp2 is the other players hp
    @move is the chosen move
    @move_list is the move_list
    @returns either player 2s hp if move = 1, 2, or 3
    else returns player 1s hp
    """
    if len(move) == 0:#if given no input returns nothing
        return
    
    elif move == '1':#when move 1
        hit_chance = random.random()
        if move_list[0][2] > hit_chance:
            strength = random.randint(10,20)
            crit = random.random()
            if 0.05 > crit:#when crits
                strength *= 2#multiply strenght by 2
                hp2 -= strength#subtracts from the hp
                if hp2 < 0:#if hp falls below zero
                    strength += hp2#the given strength is added to equal 0
                    print('%s hit %s with a Tackle dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    print('Critical Hit!')
                    hp2 = 0
                    return hp2
                else:#else displays strength normally
                    print('%s hit %s with a Tackle dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    print('Critical Hit!')
                    return hp2
                
            else:#no crit
                hp2 -= strength#same as above
                if hp2 < 0:
                    strength += hp2
                    print('%s hit %s with a Tackle dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    hp2 = 0
                    return hp2
                else:
                    print('%s hit %s with a Tackle dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    return hp2          
        else:#when misses
            print('%s dodged the attack.' % (player_not_turn))
            return hp2

    elif move == '2':#when move 2
        hit_chance = random.random()
        if move_list[1][2] > hit_chance:
            strength = random.randint(25,30)
            crit = random.random()
            if 0.05 > crit:#if crits
                strength *= 2#multiply strength by 2
                hp2 -= strength#subtracts hp2 by strength
                if hp2 < 0:#when hp falls below 0
                    strength += hp2#strength added to hp to equal 0
                    print('%s hit %s with a High Jump Kick dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    print('Critical Hit!')
                    hp2 = 0
                    return hp2
                
                else:#else displays normally
                    print('%s hit %s with a High Jump Kick dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    print('Critical Hit!')
                    return hp2
            else:#when no crit
                hp2 -= strength#same as above
                if hp2 < 0:
                    strength += hp2
                    print('%s hit %s with a High Jump Kick dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    hp2 = 0
                    return hp2
                else:
                    print('%s hit %s with a High Jump Kick dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    return hp2
        else:#when move misses
            print('%s dodged the attack.' % (player_not_turn))
            return hp2

    elif move == '3': #when move 3
        hit_chance = random.random()
        if move_list[2][2] > hit_chance:
            strength = random.randint(50,60)
            crit = random.random()
            if 0.05 > crit:#if crits
                strength *= 2#strength doubles
                hp2 -= strength#subtracts from hp2
                if hp2 < 0:#if hp falls below 0
                    strength += hp2#strength added to hp to equal 0
                    print('%s hit %s with a Desperate Blow dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    print('Critical Hit!')
                    hp2 = 0
                    return hp2
                else:#else displays normally
                    print('%s hit %s with a Desperate Blow dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    print('Critical Hit!')
                    return hp2
            else:#when no crit
                hp2 -= strength#same as above
                if hp2 <= 0:
                    strength += hp2
                    print('%s hit %s with a Desperate Blow dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    hp2 = 0
                    return hp2
                else:
                    print('%s hit %s with a Desperate Blow dealing %d points'
                          ' of damage.' % (player_turn,player_not_turn,strength))
                    return hp2
                
        else:#when move misses
            print('%s dodged the attack.' % (player_not_turn))
            return hp2

    elif move == '4':#when move 4
        hit_chance = random.random()
        if move_list[3][2] > hit_chance:
            strength = random.randint(15,20)
            crit = random.random()
            if 0.05 > crit:#when crits
                strength *= 2#strength doubles
                if hp1 == 100:#if hp is already 100
                    print('%s failed to heal itself.'
                          % (player_turn))
                    return hp1
                else:
                    hp1 += strength#else hp is added by strength
                    if hp1 > 100:#if hp becomes greater than 100
                        strength = strength - (hp1 - 100) #strenght is subracted
                        print('%s Slacked Off, healing %d points of damage.'
                              % (player_turn, strength))
                        hp1 = 100#hp becomes 100
                        return hp1
                    else:#else displays normally
                        print('%s Slacked Off, healing %d points of damage.'
                              % (player_turn, strength))
                        return hp1
            else:#when no crit
                if hp1 == 100:#same as above
                    print('%s failed to heal itself.'
                          % (player_turn))
                    return hp1
                else:
                    hp1 += strength
                    if hp1 > 100:
                        strength = strength - (hp1 - 100)
                        print('%s Slacked Off, healing %d points of damage.'
                              % (player_turn, strength))
                        hp1 = 100
                        return hp1
                    else:
                        print('%s Slacked Off, healing %d points of damage.'
                              % (player_turn, strength))
                        return hp1
        else:#when heal fails
            print('%s failed to heal itself.' % (player_turn))
            return hp1




def game_over(monster1_hp,monster2_hp):
    """
    Checks if the game is over
    @monster1_hp is monster 1s hp
    @monster2_hp is monster 2s hp
    @returns True if either monster has 0 hp
    else returns False and the game continues
    """
    if monster1_hp == 0 or monster2_hp == 0:
        return True
    else:
        return False

def pokemon():
    """
    Plays a game of Pokemon
    """

#Gets names for monsters
    monster1 = input('Enter the name for your monster: ')
    monster2 = input('Enter the name for your monster: ')

#Checks for a valid seed #
    while True:
        seed = input('Enter a seed value: ')
        if seed.isalpha() == True:
            False
        elif seed.isdigit() == True or seed[0] == '-':
            break

#Inputs seed 
    random.seed(int(seed))

#All things to keep track of    
    move_list = make_move_list()
    turn = random.randint(0,1)
    players = [monster1,monster2]
    monsters_hp = [100,100]

#When the game is still playing    
    while not game_over(monsters_hp[0],monsters_hp[1]):
        display_monster1(monster1,monsters_hp[0])
        display_monster2(monster2,monsters_hp[1])
        whos_move(turn,players)
        display_movelist(move_list)
        move = get_move(players[turn],move_list)
        total_hp = make_move(players[turn],players[(turn + 1)% 2],
                  monsters_hp[turn],monsters_hp[(turn+1)%2],
                  move,move_list)
        if players[turn] == players[0]:
            if move == '1' or move == '2' or move == '3':
                monsters_hp[1] = total_hp
            else:
                monsters_hp[0] = total_hp
                
        elif players[turn] == players[1]:
            if move == '1' or move == '2' or move == '3':
                monsters_hp[0] = total_hp
            else:
                monsters_hp[1] = total_hp
                
        turn = (turn + 1) % 2

#When game is over
    if turn == 0:
        print('%s won the fight.' % (monster2))
    else:
        print('%s won the fight.' % (monster1))
pokemon()
