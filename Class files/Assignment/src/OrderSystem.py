class OrderSystem():
	def __init__(self, customerList, orderList, inventory):
		self._customerList = customerList
		self._orderList = orderList
		self._inventory = inventory

	def check_fee(self, customer, main, main_num, sides, sides_num, drinks, drinks_num, ingredient, ingredient_num): 
        return main._price(main, main_num) + sides._sidePrice(sides, sides_num) + drinks._drinkPrice(drinks, drinks_num) + ingredient._price(ingredient, ingredient_num)

	@property
	def customerList(self):
		return self._customerList


	@property
	def orderList(self):
		return self._orderList

	@property
	def inventory(self):
		return self._inventory

	@customerList.setter
	def customerList(self, customerList):
		self._customerList = customerList

	@orderList.setter
	def orderList(self, orderList):
		self._orderList = orderList

	@inventory.setter
	def inventory(self, orderList):
		self._inventory = inventory

	def add_customer(self, customer):
		self._customerList.append(customer)

	def delete_customer(self, customer):
		self._customerList.remove(customer)

	def add_order(self, order):
		self._orderList.append(order)

	def delete_order(self, order):
		self._orderList.remove(order)

	