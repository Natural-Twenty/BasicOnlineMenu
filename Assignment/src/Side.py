#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:29:33 2019

@author: z5075710
"""


class Side():
    def __init__(self, name, unit, quantity, unitPrice):
        self._name = name
        self._unit = unit
        self._quantity = quantity
        self._unitPrice = unitPrice
        self._ingredients = []

    @property
    def name(self):
        return self._name
        
    @property
    def unit(self):
        return self._unit

    @property
    def quantity(self):
        return self._quantity
    
    @property
    def unitPrice(self):
        return self._unitPrice
    
    @property
    def ingredients(self):
        return self._ingredients
    
    def add_ingre(self,ingre):
        self._ingredients.append(ingre)

# class Sides:
    
#     def __init__(self, sides = ['3 pack nuggets', '6 pack nuggets', '0.2 kg small fries', '0.4 kg medium fries', '0.6 kg large fries'],
#                  drinks = ['375mL can of coke', '600mL bottle of water'],
#                  sidePrice = [3, 5, 2, 3, 4],
#                  drinkPrice = [2, 3]):
#         self._sides = sides
#         self._drinks = drinks
#         self._sidePrice = sidePrice
#         self._drinkPrice = drinkPrice
    
#     @property
#     def sides(self):
#         return self._sides
    
#     @property
#     def drinks(self):
#         return self._drinks
    
#     @property
#     def sidePrice(self):
#         return self._sidePrice
    
#     @property
#     def drinkPrice(self):
#         return self._drinkPrice
    
        
     
        
    