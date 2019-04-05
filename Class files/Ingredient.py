#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:55:27 2019

@author: z5075710
"""

class Ingredient:
    def __init(self, name = ['Tomato', 'Lettuce', 'Tomato sauce', 'cheddar cheese', 'swiss cheese'], price = 0.5):
        self._name = name
        self._price = price
        
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price