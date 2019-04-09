#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:10:23 2019

@author: z5075710
"""

class Main:
    def __init__(self, name = ['burger', 'wrap'],
                 bun_type = ['muffin', 'sesame'],
                 patty_type = ['chicken', 'vegetarian', 'beef'],
                 price = [2, 4, 0.5, 1]):
        self._name = name
        self._bun_type = bun_type
        self._patty_type = patty_type
        self._price = price
        
    @property
    def name(self):
        return self._name
    
    @property
    def bun_type(self):
        return self._bun_type
    
    @property
    def patty_type(self):
        return self._patty_type
    
    @property
    def price(self):
        return self._price
        

        
        #Implemented for customer orders userstory. Does not include inventory implementation
    