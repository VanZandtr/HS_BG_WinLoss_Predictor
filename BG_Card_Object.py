# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:58:40 2020

@author: rvanza632
"""

class Card:      
    def dragon_welp_eff(self):
        num_dragons = 0
        #can be made easier
        for card in self.player_board:
            if card[3] == "Dragon":
                num_dragons += 1
        #deal damage to random enemy minion
        print("Dealt", num_dragons,"to opp")
        
    
        
        
    def __init__(self):
        self.player_board = []
        self.opp_board  = []
        
        #[name, rank, golden?, type, att, def, deathrattle, on_attack, on_turn_start, taunt/divine shield] 0 - 8
        #token
        self.alley_cat_token = ["Tabey Cat", 1, False, "Beast", 1, 1, None, None, None, None]
        
        #rank 1
        self.alley_cat = ["Alley Cat", 1, False, "Beast", 1, 1, None, None, None, None]
        self.deck_swabbie = []
        self.dragonspawn_lieutenant = []
        self.fiendish_servant = []
        self.mecharoo = []
        self.micro_machine = []
        self.murloc_tidecaller = []
        self.murloc_tidehunter = []
        self.dragon_welp = ["Dragon Welp", 1, False, "Dragon", 1, 2, None, None, self.dragon_welp_eff, None]
        self.righteous_protector = []
        self.rockpool_hunter = []
        self.scallywag = []
        self.scavenging_hyena = []
        self.selfless_hero = []
        self.vulgar_homunculus = []
        self.wrath_weaver = []
        
        self.all_cards = [self.alley_cat, self.dragon_welp]