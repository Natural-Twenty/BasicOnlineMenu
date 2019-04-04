#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:39:24 2019

@author: z5075710, The Minh Tran
"""
#Need to add validations using isinstance(x, int)/(y, str)

class Food:
    def __init__(self, name, price, quantity, unit, ingredients):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._unit = unit
        self._ingredients = []
        
    #Functions involving food name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        print('Setting food name') #For testing, comment/remove when done testing
        self._name = name
        
    #Functions involving price    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        print('Setting price')
        self._price = price
        
    #Functions involving quantity
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        print('Setting quantity') #For testing, comment/remove when done testing
        self._quantity = quantity
        
    #Functions involving unit
    @property
    def unit(self):
        return self._unit
    
    @unit.setter
    def unit(self, unit):
        print('Setting unit') #For testing, comment/remove when done testing
        self._unit = unit
        
    #Functions involving ingredient
    @property
    def ingredients(self):
        return self._ingredients
    
    @ingredients.setter
    def addIngredients(self, ingredient):
        if isinstance(ingredient, str) == True:
            print('Adding one ingredient')
            self._ingredients.append(ingredient)
        elif isinstance(ingredient, list) == True:
            print('Adding multiple ingredients')
            self._ingredient.extend(ingredient)
        else:
            print('Invalid ingredient/s. Could not add.')
            
    @ingredients.deleter
    def deleteIngredients(self, ingredient):
        if isinstance(ingredient, str) == True:
            print('Deleting one ingredient')
            self._ingredients.remove(ingredient)
        elif isinstance(ingredient, list) == True:
            for i in ingredient:
                self._ingredient.remove(i)
            print('Deleting multiple ingredients')
        else:
            print('Invalid ingredient/s. Could not delete.')
        
        

        
        