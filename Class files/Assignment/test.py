#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:46:34 2019

@author: z5075710
"""
import pytest
from Order import Order
from Ingredient import Ingredient
from Main import Main
from Sides import Sides

from Staff import Staff

#Customer Ordering main
print('Ordering ...')
Main = Main()
Sides = Sides()
Ingredient = Ingredient()
Staff = Staff()


main = Main.name[0]
print(main)
main = Main.name[1]
print(main)

mainBun = Main.bun_type[0]
print(mainBun)
mainBun = Main.bun_type[1]
print(mainBun)

mainBunNo = 3
print(mainBunNo)
mainBunNo = 2
print(mainBunNo)

mainPatty = Main.patty_type[0]
print(mainPatty)
mainPatty = Main.patty_type[1]
print(mainPatty)

mainPattyNo = 1
print(mainPattyNo)
mainPattyNo = 2
print(mainPattyNo)

mainPrice = Main.price[1] + Main.price[2]*mainBunNo + Main.price[3]*mainPattyNo 
print(mainPrice)


ingredient = []
ingredient.append(Ingredient.name[0])
ingredientPrice = Ingredient.price*len(ingredient)
print(ingredient, ingredientPrice)
ingredient.append(Ingredient.name[1])
ingredientPrice = Ingredient.price*len(ingredient)
print(ingredient, ingredientPrice)
ingredient.remove(Ingredient.name[0])
ingredientPrice = Ingredient.price*len(ingredient)
print(ingredient, ingredientPrice)

#Customer ordering sides and drink

sides = []
sidePrice = 0
sides.append(Sides.sides[0])
sidePrice += Sides.sidePrice[0]
print(sides, sidePrice)
sides.append(Sides.sides[1])
sidePrice += Sides.sidePrice[1]
print(sides, sidePrice)
sides.remove(Sides.sides[0])
sidePrice -= Sides.sidePrice[0]
print(sides, sidePrice)

drinks = []
drinkPrice = 0
drinks.append(Sides.drinks[0])
drinkPrice += Sides.drinkPrice[0]
print(drinks, drinkPrice)
drinks.append(Sides.drinks[1])
drinkPrice += Sides.drinkPrice[1]
print(drinks, drinkPrice)
drinks.remove(Sides.drinks[0])
drinkPrice -= Sides.drinkPrice[0]

print('Sending in order ...\n')
customerOrder = Order(main, mainBun, mainBunNo, mainPatty, mainPattyNo, mainPrice, ingredient,
                      ingredientPrice, sides, drinks, sidePrice, drinkPrice)

Staff.checkStatus(customerOrder.orderID)

Staff.addOrder(customerOrder)

Staff.viewOrder

Staff.setStatus(0)

Staff.checkStatus(customerOrder.orderID)

