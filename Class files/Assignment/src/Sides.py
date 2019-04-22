#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:29:33 2019

@author: z5075710
"""

class Sides:
    
    def __init__(self, sides = ['3 pack nuggets', '6 pack nuggets', 'small fries', 'medium fries', 'large fries', 
                                'small sundae-chocolate', 'medium sundae-chocolate', 'large sundae-chocolate',
                                'small sundae-strawberry', 'medium sundae-strawberry', 'large sundae-strawberry'],
                 drinks = ['375mL of coke', '600mL bottle of coke', '600mL bottle of water', 'small orange-juice',
                           'medium orange-juice', 'large orange-juice'],
                 sidePrice = [3, 5, 2, 3, 4, 3, 4, 5, 3, 4, 5],
                 drinkPrice = [2, 4, 3, 1, 2, 3]):
        self._sides = sides
        self._drinks = drinks
        self._sidePrice = sidePrice
        self._drinkPrice = drinkPrice
    
    @property
    def sides(self):
        return self._sides
    
    @property
    def drinks(self):
        return self._drinks
    
    @property
    def sidePrice(self):
        return self._sidePrice
    
    @property
    def drinkPrice(self):
        return self._drinkPrice
    
        
     
        
    