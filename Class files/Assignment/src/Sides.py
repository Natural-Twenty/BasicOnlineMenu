#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:29:33 2019

@author: z5075710
"""

class Sides:
    
    def __init__(self, sides = ['3 pack nuggets', '6 pack nuggets', '0.2 kg small fries', '0.4 kg medium  fries', '0.6 kg large fries', 'Small chocolate sundae', 'Medium chocolate sundae', 'Large chocolate sundae', 'Small strawberry sundae', 'Medium strawberry sundae', 'Large strawberry sundae'],
                 drinks = ['Can of coke', 'Bottle of coke' 'Bottle of water', 'Small orange juice', 'Medium orange juice', 'Large orange juice'],
                 sidePrice = [3, 5, 2, 3, 4, 4, 5, 6, 4, 5, 6],
                 drinkPrice = [2, 4, 3, 4, 5, 6]):
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
    
        
     
        
    