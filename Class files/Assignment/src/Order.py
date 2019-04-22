#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:43:40 2019

@author: z5075710
"""
import random
from src.Inventory import Inventory
from src.Main import Main
from server import inventory
class Order:
    def __init__(self, main, mainBun, mainBunNo, mainPatty, mainPattyNo, mainPrice, 
                 ingredients = [], ingredientsPrice= 0,
                 sides = [], drinks=[], sidePrice = 0, drinkPrice = 0, status = 'Not ready'):
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
        self._status = status
        self._obj_inventory = Inventory()
        self._obj_main = Main()
        if main == 'burger':
            mainBunList = self._obj_main.bun_type
            mainQuant = self._obj_inventory.mainQuant[mainBunList.index(mainBun)]
            print(f'Checking inventory... {mainQuant} {mainBun} {main} in stock')
            print(f'{mainBun} {mainBunNo} buns ordered')
            if mainBun == 'sesame':
                inventory.useInventory(1,mainBunNo)
            else:
                inventory.useInventory(0,mainBunNo)
        else:
            mainBunList = self._obj_main.bun_type
            mainQuant = self._obj_inventory.mainQuant[2+mainBunList.index(mainBun)]
            print(f'Checking inventory... {mainQuant} {mainBun} in stock')
            print(f'{mainBunNo} buns ordered')
            if mainBun == 'sesame':
                inventory.useInventory(3,mainBunNo)
            else:
                inventory.useInventory(2, mainBunNo)
        
        pattyList = self._obj_main.patty_type
        pattyQuant = self._obj_inventory.mainQuant[4+pattyList.index(mainPatty)]
        print(f'Checking inventory... {pattyQuant} kg of {mainPatty} patties in sotck')
        print(f'{mainPattyNo} {mainPatty} ordered')
        pattyIndex = 4+pattyList.index(mainPatty)
        inventory.useInventory(pattyIndex, mainPattyNo)
        
        if any(ingredients) is True:
            for i in ingredients:
                ingredientList = self._obj_inventory.ingredient
                ingredientQuant = self._obj_inventory.ingredientQuant[ingredientList.index(i)]
                print(f'Checking inventory... {ingredientQuant} {i} in stock')
                ingredientIndex = 7+ingredientList.index(i)
                inventory.useInventory(ingredientIndex, 0.1)
                
        if any(sides) is True:
            for s in sides:
                sideSplit = s.split(' ')
                if len(sideSplit) > 1:
                    sideList = self._obj_inventory.side
                    if sideSplit[0] == 'small':
                        sideOrder = 0.2
                    elif sideSplit[0] == 'medium':
                        sideOrder = 0.4
                    elif sideSplit[0] == 'large':
                        sideOrder = 0.6
                    else:
                        sideOrder = float(sideSplit[0])
                    sideName = sideSplit[-1]
                    sideQuant = self._obj_inventory.sideQuant[sideList.index(sideName)]
                    if sideName == 'nuggets':
                        inventory.useInventory(12, sideOrder)
                    elif sideName == 'fries':
                        print(f'Checking inventory... {sideQuant} kg of {sideName} in stock')
                        print(f'(sideOrder) of {sideName} ordered')
                        inventory.useInventory(13, sideOrder)
                    else:
                        print(f'Checking inventory... {sideQuant} of {sideName} in stock')
                        print(f'{sideOrder} {sideName} ordered')
                        if sideName == 'sundae-chocolate':
                            inventory.sundae(0, sideOrder)
                        else:
                            inventory.sundae(1, sideOrder)
                    
        if any(drinks) is True:
            for d in drinks:
                drinkList = self._obj_inventory.side
                drinkSplit = d.split(' ')
                drinkName = drinkSplit[-1]
                drinkType = drinkSplit[0]
                drinkQuant = self._obj_inventory.sideQuant[drinkList.index(drinkName)]
                print(f'Checking inventory... {drinkQuant} {drinkType}s of {drinkName} in stock')
                if drinkType == 'small':
                    drinkOrder = 0.2
                if drinkType == 'medium':
                    drinkOrder = 0.4
                if drinkType == 'large':
                    drinkOrder = 0.6
                    
                if drinkName == 'coke':
                    if drinkType == '375mL':
                        inventory.useInventory(15, 1)
                    else:
                        inventory.useInventory(14, 1)
                elif drinkName == 'water':
                    inventory.useInventory(16, 1)
                else:
                    inventory.useInventory(17, drinkOrder)
                    
        
        
        print(f'Here is your order ID: {self._orderID}')
        print(f'Total cost = ${mainPrice+sidePrice+drinkPrice+ingredientsPrice}')
         
        
    @property
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
        
    @property
    def status(self):
        return self._status
    
    def setStatus(self, status):
        self._status = status
        
    @property
    def orderID(self):
        return self._orderID
        
    def __str__(self):
        output = ''
        output += f'{self._main} with\n'
        output += f'{self._mainBunNo} {self._mainBun} buns and\n'
        output += f'{self._mainPattyNo} {self._mainPatty} patties.\n'
        if any(self._ingredients) is True:
            output += 'Extra ingredients: |'
            for i in self._ingredients:
                output += f'   {i}   |'
        output += '\n'
        if any(self._sides) is True:
            output += 'Sides: |'
            for s in self._sides:
                output += f'   {s}   |'
        output += '\n'
        if any(self._drinks) is True:
            output += 'Drinks: |'
            for d in self._drinks:
                output += f'   {d}   |'
        output += '\n'
        return output