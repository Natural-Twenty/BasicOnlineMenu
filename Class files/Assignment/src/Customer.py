
class Customer():
	def __init__(self, name, email, username, password, orders):
		self._name = name
		self._email = email
		self._username = username
		self._password = password
		self._orders = []

	@property
	def name(self):
		return self._name
	
	@property
	def email(self):
		return self._email
	
	@property
	def username(self):
		return self._username
	
	@property
	def password(self):
		return self._password
	
	@property
	def orders(self):
		return self._orders
	
	@name.setter
	def name(self, name):
		self._name = name

	@email.setter
	def email(self, email):
		self._email = email

	@username.setter
	def username(self, username):
		self._username = username

	@password.setter
	def password(self, password):
		self._password = password

	@orders.setter
	def orders(self, orders):
		self._orders = orders

	def add_order(self, order):
		self._orders.append(order)

	def delete_order(self, order):
		self._orders.remove(order)

	

