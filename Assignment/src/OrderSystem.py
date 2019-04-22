from src.Customer import Customer

class OrderSystem():
	def __init__(self):
		self._customerList = []
		self._orderList = []
		self._inventory = []
		self._mainList = []
		self._oid = 0

	@property
	def customerList(self):
		return self._customerList
	def get_clist(self):
		return self._customerList

	@property
	def orderList(self):
		return self._orderList

	@property
	def inventory(self):
		return self._inventory
	
	@property
	def mainList(self):
		return self._mainList

	@property
	def oid(self):
		return self._oid
	
	def Oid_incre(self):
		self._oid += 1
		return self._oid
	
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

	def check_customer(self, username):
		for ele in self._customerList:
			name = ele.name
			if name == username:
				return self._customerList[0]
		return None

	def add_ingre(self, ingre):
		self._inventory.append(ingre)

	def add_main(self, main):
		self._mainList.append(main)
	
	