import pytest
from Ingredient import Ingredient
from Inventory import Inventory
from Main import Main
from Order import Order
from Sides import Sides
from Staff import Staff


main = Main()
ingred = Ingredient()
side = Sides()
# Order1 = Order('burger','muffin',3,'chicken',2, 4)




def test_ingredient():
	assert(ingred.price == 0.5)
	assert(len(ingred.name) == 5)

def test_main():
	assert(len(main.name) == 2)
	assert(len(main.patty_type) == 3)
	assert(main.price[2] == 0.5)


def test_sides():
	assert(len(side.sidePrice) == 5)


# def test_status():
# 	assert(Order1.status == 'Not ready')


test_ingredient()
test_main()
test_sides()

