# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:58:24 2020

@author: rvanza632
"""

from BG_Card_Object import Card
import random

cards = Card()
total_runs = 10

def add_cards_to_player_board():
    while True:
        card_to_add = input("Add card to your board (first to last) or Done: ")
        if card_to_add == "Done":
            return
        for card in cards.all_cards:
            if card_to_add == card[0]:
                add_att = input ("Attack?")
                add_def = input ("Defense?")
                #add_death/eff
                new_card = card.copy()
                new_card[4] = add_att
                new_card[5] = add_def
                cards.player_board.append(new_card)
                print("Card Added")

def add_cards_to_opp_board():
    while True:
        card_to_add = input("Add card to opp's board (first to last) or Done: ")
        if card_to_add == "Done":
            return
        for card in cards.all_cards:
            if card_to_add == card[0]:
                add_att = input ("Attack?")
                add_def = input ("Defense?")
                #add_death,eff
                new_card = card.copy()
                new_card[4] = add_att
                new_card[5] = add_def
                cards.opp_board.append(new_card)
                print("Card Added")
                
            
    
def run_on_start(pb, ob, flip_res):
    switch_flag = flip_res
    opp_index = 0
    player_index = 0
    
    while True:
        if player_index > 8  and opp_index > 8:
            return
        
        #opp_turn
        elif switch_flag == 0:
            for card in ob:
                if card[8] is not None:
                    print("Opp ON Start Action")
                    card[8]()
            opp_index += 1
            switch_flag = 1
    
        #player_turn
        else: #if switch_flag == 1:
            for card in pb:
                if card[8] is not None:
                    print("Player On Start Action")
                    card[8]()
            player_index += 1
            switch_flag = 0
                
            
def battle(pb, ob, flip_res):
    print("Running Simulation X1000")
    switch_flag = flip_res
    opp_index = 0
    player_index = 0
    
    while True:
        #tie
        if len(cards.player_board) == 0 and len(cards.opp_board) == 0:
            return 0
        
        #loss
        elif len(cards.player_board) == 0 and len(cards.opp_board) != 0:
            print("LOSS")
            return -1
        
        #win
        elif len(cards.player_board) == 0 and len(cards.opp_board) != 0:
            return 1
        
        #opp_turn
        elif switch_flag == 0:
            print("OPP TURN")
            #card at index fights random card or taunt
            
            #check for taunt
            player_cards_to_pick_from = []
            has_taunt = False
            for card in pb:
                if card[9] == "Taunt":
                    player_cards_to_pick_from = [card]
                    has_taunt = True
                    
            #pick random non-taunt o/w
            random_card = []
            if has_taunt == False:
                random_card = random.choice(pb)
            else:
                random_card = random.choice(player_cards_to_pick_from)
            
            #fight
            #player card health - opp attack
            random_card[5] = random_card[5] - ob[opp_index][4]
            
            #opp card health - player attack
            ob[opp_index][5] = ob[opp_index][5] - random_card[4]
            
            print(pb)
            print(ob)
            #check if dead
            if random_card[5] <= 0:
                pb.remove(random_card)
                if player_index > 0:
                    player_index = player_index - 1
            
            if ob[opp_index][5] <= 0:
                ob.remove(ob[opp_index])
                opp_index = opp_index - 1
                
            opp_index += 1
            switch_flag = 1
            print()
        
        #player_turn
        else:
            print("Player TURN")
            #card at index fights random card or taunt
            
            #check for taunt
            player_cards_to_pick_from = []
            has_taunt = False
            for card in ob:
                if card[9] == "Taunt":
                    player_cards_to_pick_from = [card]
                    has_taunt = True
                    
            #pick random non-taunt o/w
            random_card = []
            if has_taunt == False:
                random_card = random.choice(ob)
            else:
                random_card = random.choice(player_cards_to_pick_from)
            
            #fight
            #player card health - opp attack
            random_card[5] = random_card[5] - pb[player_index][4]
            
            #opp card health - player attack
            pb[player_index][5] = pb[player_index][5] - random_card[4]
            
            print(pb)
            print(ob)
            
            #check if dead
            if random_card[5] <= 0:
                ob.remove(random_card)
                if opp_index > 0:
                    opp_index = opp_index - 1
            
            if pb[player_index][5] <= 0:
                pb.remove(pb[player_index])
                player_index = player_index - 1
            
            
            player_index += 1
            switch_flag = 0
            print()
    
    #on attacks
    #deathrattles
    
    print("Your board:", cards.player_board)
    print("Opp board:", cards.opp_board)
    
def coin_flip():
    flip = random.randint(0, 1)
    print(flip)
    return flip

def main():

    #add_cards_to_player_board()
    #add_cards_to_opp_board()
    
    wins = 0
    losses = 0
    ties = 0
    
    for i in range(total_runs):
        #test
        new_card_1 = ["Alley Cat", 1, False, "Beast", 1, 1, None, None, None, None]
        new_card_2 = ["Alley Cat", 1, False, "Beast", 2, 2, None, None, None, None]
        cards.player_board.append(new_card_1)
        cards.opp_board.append(new_card_2)
    
        ret = coin_flip()
        run_on_start(cards.player_board, cards.opp_board, ret)
        result = battle(cards.player_board, cards.opp_board, ret)
        
        if result == 1:
            wins = wins + 1
        elif result == -1:
            losses = losses + 1
        else:
            ties = ties + 1
        
        
    
    print("Total Runs:", total_runs)
    print("Wins:", wins)
    print("Ties:", ties)
    print("Losses:", losses)
    


main()
