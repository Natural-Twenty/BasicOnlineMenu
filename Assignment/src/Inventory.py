#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:21:47 2019

@author: z5075710
"""

class Inventory:
    def __init__(self, main = ['burger-muffin', 'burger-sesame', 'wrap-sesame', 'wrap-sesame', 'chicken', 'vegetarian', 'beef'],
                 mainQuant = [10, 5, 6, 8, 10, 7, 2],
                 side = ['nuggets', 'fries', 'coke', 'water'],
                 sideQuant = [10, 25, 40, 19],
                 ingredient = ['Tomato', 'Lettuce', 'Tomato sauce', 'cheddar cheese', 'swiss cheese'],
                 ingredientQuant = [5, 7, 9, 14, 12]):
        self._main = main
        self._mainQuant = mainQuant
        self._side = side
        self._sideQuant = sideQuant
        self._ingredient = ingredient
        self._ingredientQuant = ingredientQuant
    
    @property
    def main(self):
        return self._main
    
    @property
    def mainQuant(self):
        return self._mainQuant
    
    @property
    def side(self):
        return self._side
    
    @property
    def sideQuant(self):
        return self._sideQuant
    
    @property
    def ingredient(self):
        return self._ingredient
    
    @property
    def ingredientQuant(self):
        return self._ingredientQuant
    
    