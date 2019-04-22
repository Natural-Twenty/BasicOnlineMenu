from src.OrderSystem import OrderSystem
from src.Customer import Customer
from src.Main import Main
from src.Ingredient import Ingredient
from src.Side import Side

def order_system():
	system = OrderSystem()
	#read user
	f = open('user.txt','r')
	lines = f.readlines()
	for user in lines:
		up = user.split()
		r_username = up[0]
		r_password = up[1]
	#create user
		customer = Customer(r_username,r_username+"@gmail.com",r_username,r_password,[])
		system.add_customer(customer)
	f.close()

	#inventory
	#self, name, quantity, unitprice
	f2 = open('ingre.txt','r')
	lines = f2.readlines()
	for line in lines:
		content = line.split()
		i_name = content[0]
		i_quantity = content[1]
		i_unit = content[2]
		i_unitPrice = content[3]
		ingre = Ingredient(i_name,int(i_quantity),i_unit, int(i_unitPrice))
		system.add_ingre(ingre)
	f2.close()


	#create main menu
	bur1I1= Ingredient('Burger',1,'Buns',1)
	burger1 = Main('Muffin Burger',3,0,)
	burger1.add_ingre(bur1I1)

	burger2 = Main('Sesame Burger',3,0)
	bur2I1 = Ingredient('Burger',1,'Buns',1)
	burger2.add_ingre(bur2I1)

	wrap1 = Main('Muffin Wrap', 4, 0)
	wr1I1 = Ingredient('Wrap',2,'Buns',1)
	wrap1.add_ingre(wr1I1)

	wrap2 = Main('Sesame Wrap', 4, 0)
	wr2I1 = Ingredient('Wrap',2,'Buns',1)
	wrap2.add_ingre(wr2I1)

	#create side menu
	#self, name, unit, quantity, unitPrice)
	Side1 = Side('3 pack nuggets','pack',0,6)
	S1I1 = Ingredient('Nugget', 3, 'pieces',2)
	Side1.add_ingre(S1I1)

	Side2 = Side('6 pack nuggets', 'pack',0,12)
	S2I1 = Ingredient('Nugget', 6,'pieces' ,2)
	Side2.add_ingre(S2I1)

	Side3 = Side('0.2 kg small fries', 'kg',0,2)
	S3I1 = Ingredient('Fries', 0.2,'kg' ,1)
	Side3.add_ingre(S3I1)

	Side4 = Side('0.4 kg medium fries', 'kg',0, 4)
	S4I1 = Ingredient('Fries', 0.4,'kg' ,1)
	Side4.add_ingre(S4I1)

	Side5 = Side('0.6 kg large fries', 'kg',0,6)
	S5I1 = Ingredient('Fries', 0.6, 'kg',1)
	Side5.add_ingre(S5I1)


	print(system.customerList)
	system.add_main(burger1)
	system.add_main(burger2)
	system.add_main(wrap1)
	system.add_main(wrap2)
	
	return system
