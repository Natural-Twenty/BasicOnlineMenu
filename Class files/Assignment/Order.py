#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:43:40 2019

@author: z5075710
         z5177881
"""
import random
class Order:
    def __init__(self, main, mainBun, mainBunNo, mainPatty, mainPattyNo, mainPrice, 
                 ingredients = [], ingredientsPrice= 0,
                 sides = [], drinks=[], sidePrice = 0, drinkPrice = 0):
        self._main = main
        self._mainBun = mainBun
        self._mainBunNo = mainBunNo
        self._mainPatty = mainPatty
        self._mainPattyNo = mainPattyNo
        self._mainPrice = mainPrice
        self._ingredients = ingredients
        self._ingredientsPrice = ingredientsPrice
        self._sides = sides
        self._drinks = drinks
        self._sidePrice = sidePrice
        self._drinkPrice = drinkPrice
        self._orderID = random.randint(1,10)
        print(f'Here is your order ID: {self._orderID}')
    
    # Update when the order is ready to pick up
    def preparation_status(self):
        self._is_ready = True
        
    @property
    def is_ready(self):
        return self._is_ready
    
    def main(self):
        return self._main
    
    @main.setter
    def main(self, main):
        print('Setting main')
        self._main = main
        
    @property
    def mainBun(self):
        return self._mainBun
    
    @mainBun.setter
    def mainBun(self, mainBun):
        print('Setting mainBun')
        self._mainBun = mainBun
        
    @property
    def mainBunNo(self):
        return self._mainBunNo
    
    @mainBunNo.setter
    def mainBunNo(self, mainBunNo):
        if isinstance(mainBunNo, int) == False:
            print('Invalid input')
        elif mainBunNo < 2:
            print('Need at least 2 buns')
        elif mainBunNo > 4:
            print('Must be bellow 4 buns')
        else:
            print('setting main Bun number')
            self._mainBunNo = mainBunNo
            
    @property
    def mainPatty(self):
        return self._mainPatty
    
    @mainPatty.setter
    def mainPatty(self, mainPatty):
        print('Setting main patty')
        self._mainPatty = mainPatty
        
    @property
    def mainPattyNo(self):
        return self._mainPattyNo
    
    @mainPattyNo.setter
    def mainPattyNo(self, mainPattyNo):
        if isinstance(mainPattyNo, int) == False:
            print('Invalid input')
        elif mainPattyNo < 1:
            print('Must have at least 1 patty')
        elif mainPattyNo > 4:
            print('Must have at most 4 patties')
        else:
            self._mainPattyNo = mainPattyNo
            
    @property
    def mainPrice(self):
        return self._mainPrice
    
    @mainPrice.setter
    def mainPrice(self, mainPrice):
        print('Setting main price')
        self._mainPrice = mainPrice
    
    @property
    def ingredients(self):
        return self._ingredients
    
    @ingredients.setter
    def ingredient(self, ingredientsList):
            print('Overriding ingredients')
            self._ingredients = ingredientsList
         
    @property
    def ingredientsPrice(self):
        return self._ingredientsPrice
    
    @ingredientsPrice.setter
    def ingredientsPrice(self):
        print('Setting ingredients price')
        self._ingredientsPrice
    
    @property
    def sides(self):
        return self._sides
    
    @sides.setter
    def sides(self, sides):
        print('Setting sides')
        self._sides = sides
        
    @property    
    def drinks(self):
        return self._drinks
    
    @drinks.setter
    def drinks(self, drinks):
        print('Setting drinks')
        self._drinks = drinks
        
    @property
    def sidePrice(self):
        return self._sidePrice
    
    @sidePrice.setter
    def sidePrice(self, sidePrice):
        print('Setting side Price')
        self._sidePrice = sidePrice
        
    @property
    def drinkPrice(self):
        return self._drinkPrice
    
    @drinkPrice.setter
    def drinkPrice(self, drinkPrice):
        print('Setting drink Price')
        self._dirnkPrice = drinkPrice
        
    
