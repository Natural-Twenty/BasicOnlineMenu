#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:55:27 2019

@author: z5075710
"""


class Ingredient():

    def __init__(self, name, quantity,unit, unitPrice):
        self._name = name
        self._quantity = quantity
        self._unit = unit
        self._unitPrice = unitPrice

    @property
    def name(self):
        return self._name
    
    @property
    def quantity(self):
        return self._quantity
    
    @property
    def unit(self):
        return self._unit
    

    @property
    def unitPrice(self):
        return self._unitPrice
    

# class Ingredient:
#     def __init__(self, name = None, 
#                price = 0.5):
#         if name is None:
#             name = ['Tomato', 'Lettuce', 'Tomato sauce', 'cheddar cheese', 'swiss cheese']
#             self._name = name
#         self._price = price
        
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def price(self):
#         return self._price