from flask import Flask, render_template, request, redirect, url_for, abort
from server import app, system, staff, inventory
from src.Customer import Customer
from src.Order import Order
from src.Sides import Sides
from src.Main import Main
from src.Ingredient import Ingredient
from src.Staff import Staff


@app.route('/', methods=["GET", "POST"])
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=["GET", "POST"])
def login():
    #receive and store into session
    if request.method == 'POST' and request.form.get('username&password') == 'True':
        username = request.form.get('username')
        password = request.form.get('password')
        
        #authenticate the username and password
        success = False
        f = open('user.txt','r')
        lines = f.readlines()
        for user in lines:
            up = user.split()
            r_username = up[0]
            r_password = up[1]
            if username != r_username: continue
            else:
                if r_password == password:
                    success = True
        f.close()
        if success == False:
            error={}
            error['auth'] = 'Invalid Username or Password'
            return render_template('login.html', error = error)
        else:
            return render_template('home.html')
    return render_template('login.html')

@app.route('/register',methods=["GET", "POST"])
def register():
    if request.method == 'POST' and request.form.get('register') == 'True':
        username = request.form.get('username')
        password = request.form.get('password')
        f = open('user.txt','a+')
        towrite = username + ' ' + password + '\n'
        f.write(towrite)
        f.close()
        return render_template('home.html')
    else:
        return render_template('register.html')

'''
Display the menu page
'''
@app.route('/login/menu', methods=["GET", "POST"])
def menu():
    mainList = ['burger', 'wrap', 'muffin', 'sesame', 'chicken', 'vegetarian', 'beef']
    sidesList = ['3 pack nuggets', '6 pack nuggets', '0.2 kg small fries', '0.4 kg medium  fries', '0.6 kg large fries']
    drinksList = ['375mL can of coke', '600mL bottle of water']
    ingredientList = ['Tomato', 'Lettuce', 'Tomato sauce', 'cheddar cheese', 'swiss cheese']
    if request.method == 'GET':
        return render_template('menu.html')
    else:
        return render_template('menu.html', main = mainList, sides = sidesList, drinks = drinksList, ingredient = ingredientList)
'''
Make an order
'''
@app.route('/login/menu/order', methods=["GET", "POST"])
def order():
    if request.method == "POST":
        if "confirm order" in request.form:
            order = system.make_order(customer, car, request.form.getList('mainList', 'sidesList', 'drinksList', 'ingredientList'))
            orderData = dict(order = order)
        return render_template('confirmation.html', request.form.getList('mainList', 'sidesList', 'drinksList', 'ingredientList'), data = orderData)
    else:
        return render_template('menu.html')
        
'''
Home page
May have to use return redirect(url_for('')) instead of render template
To be tested
'''
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method=="POST":
        orderID = int(request.form.get('orderID'))
        if orderID < 0:
            message = "error"
            return render_template('home.html', message=message)
        orders = staff.order
        for i in range(0,len(orders)):
            if orderID == orders[i].orderID:
                main = orders[i].main
                main_bun_no = orders[i].main_bun_no
                main_bun_type = orders[i].main_bun_type
                ingredient = orders[i].ingredients
                sides = orders[i].sides
                drinks = orders[i].drinks
                price = orders[i].mainPrice + orders[i].sidePrice + orders[i].ingredientsPrice + orders[i].drinkPrice
                status = orders[i].status                
                return render_template('StatusPage.html', orderID=orderID, main=main, main_bun_no=main_bun_no, main_bun_type=main_bun_type,
                                        ingredient=ingredient, sides=sides, drinks=drinks, price=price, status=status)
        message = 'error'
        return render_template('home.html', message=message)
    return render_template('home.html')

'''
Pre-order page
To be tested
'''
@app.route('/pre_order', methods=['POST', 'GET'])
def pre_order():
    if request.method=="POST":
        mainObj = Main()
        choice = request.form.get('pre_order')
        if choice == "customise":
            return render_template('customise.html')
        elif choice == "base_burger":
            main = mainObj.name[0]
            bun_type = mainObj.bun_type[0]
            patty_type = mainObj.patty_type[0]
            price = mainObj.price[0]+2*mainObj.price[2]+mainObj.price[3]  
            order = Order(main, bun_type, 2, patty_type, 1, price)
            staff.addOrder(order)
            status = order.status
            orderID = order.orderID
            return render_template('confirmation.html', main=main, bun_no=2, bun_type=bun_type,
                                   patty_type=patty_type, patty_no=1, status=status, orderID=orderID,
                                   price=price)
        elif choice == "base_wrap":
            main = mainObj.name[1]
            bun_type = mainObj.bun_type[1]
            patty_type = mainObj.patty_type[1]
            price = mainObj.price[1]+2*mainObj.price[2]+mainObj.price[3]
            order = Order(main, bun_type, 2, patty_type, 1, price)
            staff.addOrder(order)
            status = order.status
            orderID = order.orderID
            return render_template('confirmation.html', main=main, bun_no=2, bun_type=bun_type,
                                   patty_type=patty_type, patty_no=1, status=status, orderID=orderID,
                                   price=price)
        else:
            message = 'Error, you should not be getting this error.'
            return render_template('pre_order.html', message=message)
    return render_template('pre_order.html')
        
@app.route('/customise', methods=['POST', 'GET'])
def customise():
    MainObj = Main()
    IngredObj = Ingredient()
    SidesObj = Sides()
    if request.method=="POST":
        mainPrice = 0
        sidePrice = 0
        drinkPrice = 0
        mainIndex = int(request.form.get(main))
        main = MainObj.name[mainIndex]
        mainPrice += mainPrice[mainIndex]
        
        mainBunIndex = int(request.form.get(bun_type))
        mainBun = MainObj.bun_type[mainBunIndex]
        mainBunNo = int(request.form.get(bun_no))
        mainPrice += mainBunNo*MainObj.price[2]
        
        patty_typeIndex = int(request.form.get(patty_type))
        mainPatty = MainObj.patty_type[patty_typeIndex]
        mainPattyNo = int(request.form.get(patty_no))
        mainPrice += mainPattyNo*MainObj.price[3]
        
        ingredientIndexList = request.form.get(Ingredient)
        ingredients = []
        for i in ingredientIndexList:
            ingredients.append(IngredObj.name[int(i)])
            mainPrice += IngredObj.price
            
        sidesIndexList = request.form.get(Sides)
        sides = []
        for i in sidesIndexList:
            repeatx = 'repeat' + i
            repeats = int(request.form.get(repeatx))
            for r in range(0, repeats):
                sides.append(SidesObj.sides[int(i)])
                sidePrice += SidesObj.sidePrice[int(i)]
        
        drinksIndexList = request.form.get(Drinks)
        drinks = []
        for j in drinksIndexList:
            repeaty = 'repeat' + i
            repeat = int(request.form.get(repeaty))
            for a in range(0,repeat):
                drinks.append(SidesObj.drinks[int(j)])
                drinkPrice += SidesObj.drinkPrice[int(j)]
        
        price = mainPrice + sidePrice + drinkPrice
        
        order = Order(main, mainBun, mainBunNo, mainPatty, mainPattyNo, mainPrice,
                      ingredients, ingredientsPrice, sides, drinks, sidePrice, drinkPrice)
        orderID = order.orderID
        status = order.status
        staff.addOrder(order)
        return render_template('confirmation.html', orderID=orderID, main=main,
                               mainBun=mainBun, mainBunNo=mainBunNo, mainPattyNo=mainPattyNo,
                               mainPatty=mainPatty, ingredients=ingredients, sides=sides,
                               drinks=drinks, price=price, status=status)
                               
    return render_template('customise.html')

@app.route('/confirmation', methods=['POST', 'GET'])
def confirmation():
    if request.method=="POST":
        orderID = request.form.get('orderID')
        for i in range(0,len(staff.order)):
            if orderID == staff.order[i].orderID:
                status = 'Not Ready'
                main = staff.order[i].main
                mainBun = staff.order[i].mainBun
                mainBunNo = staff.order[i].mainBunNo
                mainPatty = staff.order[i].mainPatty
                mainPattyNo = staff.order[i].mainPattyNo
                ingredients = staff.order[i].ingredients
                sides = staff.order[i].sides
                drinks = staff.order[i].drinks
                mainPrice =staff.order[i].mainPrice
                sidePrice = staff.order[i].sidePrice
                drinkPrice = staff.order[i].drinkPrice
                ingredientsPrice = staff.order[i].ingredeientsPrice
                price = mainPrice + sidePrice + drinkPrice + ingredientsPrice
                return render_template('StatusPage.html', orderID=orderID, main=main,
                               mainBun=mainBun, mainBunNo=mainBunNo, mainPattyNo=mainPattyNo,
                               mainPatty=mainPatty, ingredients=ingredients, sides=sides,
                               drinks=drinks, price=price, status=status)
                
                
        for i in range(0,len(staff.order)):
            if orderID == staff.order[i].orderID:
                status = 'Ready'
                main = staff.order[i].main
                mainBun = staff.order[i].mainBun
                mainBunNo = staff.order[i].mainBunNo
                mainPatty = staff.order[i].mainPatty
                mainPattyNo = staff.order[i].mainPattyNo
                ingredients = staff.order[i].ingredients
                sides = staff.order[i].sides
                drinks = staff.order[i].drinks
                mainPrice =staff.order[i].mainPrice
                sidePrice = staff.order[i].sidePrice
                drinkPrice = staff.order[i].drinkPrice
                ingredientsPrice = staff.order[i].ingredientsPrice
                price = mainPrice + sidePrice + drinkPrice + ingredientsPrice       
                return render_template('StatusPage.html', orderID=orderID, main=main,
                               mainBun=mainBun, mainBunNo=mainBunNo, mainPattyNo=mainPattyNo,
                               mainPatty=mainPatty, ingredients=ingredients, sides=sides,
                               drinks=drinks, price=price, status=status)
    return render_template('confirmation.html')

@app.route('/StatusPage', methods=['POST', 'GET'])
def StatusPage():
    if request.method=="POST":
        orderID = request.form.get('orderID')
        for i in range(0,len(staff.order)):
            if orderID == staff.order[i].orderID:
                status = 'Not Ready'
                main = staff.order[i].main
                mainBun = staff.order[i].mainBun
                mainBunNo = staff.order[i].mainBunNo
                mainPatty = staff.order[i].mainPatty
                mainPattyNo = staff.order[i].mainPattyNo
                ingredients = staff.order[i].ingredients
                sides = staff.order[i].sides
                drinks = staff.order[i].drinks
                mainPrice =staff.order[i].mainPrice
                sidePrice = staff.order[i].sidePrice
                drinkPrice = staff.order[i].drinkPrice
                ingredientsPrice = staff.order[i].ingredientsPrice
                price = mainPrice + sidePrice + drinkPrice + ingredientsPrice               
        for i in range(0,len(staff.order)):
            if orderID == staff.order[i].orderID:
                status = 'Ready'
                main = staff.order[i].main
                mainBun = staff.order[i].mainBun
                mainBunNo = staff.order[i].mainBunNo
                mainPatty = staff.order[i].mainPatty
                mainPattyNo = staff.order[i].mainPattyNo
                ingredients = staff.order[i].ingredients
                sides = staff.order[i].sides
                drinks = staff.order[i].drinks
                mainPrice =staff.order[i].mainPrice
                sidePrice = staff.order[i].sidePrice
                drinkPrice = staff.order[i].drinkPrice
                ingredientsPrice = staff.order[i].ingredientsPrice
                price = mainPrice + sidePrice + drinkPrice + ingredientsPrice       
        return render_template('StatusPage.html', orderID=orderID, main=main,
                               mainBun=mainBun, mainBunNo=mainBunNo, mainPattyNo=mainPattyNo,
                               mainPatty=mainPatty, ingredients=ingredients, sides=sides,
                               drinks=drinks, price=price, status=status)
    return render_template('StatusPage.html')

@app.route('/manageInventory', methods=['POST', 'GET'])
def manageInventory():
    if request.method=="POST":
        inventoryList = request.form.get('inventory')
        for i in inventoryList:
            index = int(i)
            restock = 'restock'
            restockx = restock + i
            amount = request.form.get(restockx)
            if amount < 0:
                message = 'Error: negative number entered'
                return render_template('inventory.html', message)
            inventory.addInventory(index, amount)
            quan0 = inventory.mainQuant[0]
            quan1 = inventory.mainQuant[1]
            quan2 = inventory.mainQuant[2]
            quan3 = inventory.mainQuant[3]
            quan4 = inventory.mainQuant[4]
            quan5 = inventory.mainQuant[5]
            quan6 = inventory.mainQuant[6]
            quan7 = inventory.ingredientQuant[0]
            quan8 = inventory.ingredientQuant[1]
            quan9 = inventory.ingredientQuant[2]
            quan10 = inventory.ingredientQuant[3]
            quan11 = inventory.ingredientQuant[4]
            quan12 = inventory.sideQuant[0]
            quan13 = inventory.sideQuant[1]
            quan14 = inventory.sideQuant[2]
            quan15 = inventory.sideQuant[3]
            quan16 = inventory.sideQuant[4]
            quan17 = inventory.sideQuant[5]
            quan18 = inventory.sideQuant[6]
            quan19 = inventory.sideQuant[7]
            quan20 = inventory.sideQuant[8]
            return render_template('inventory.html', quan0=quan0, quan1=quan1,
                                   quan2=quan2, quan3=quan3, quan4=quan4, quan5=quan5,
                                   quan6=quan6, quan7=quan7, quan8=quan8, quan9=quan9,
                                   quan10=quan10, quan11=quan11, quan12=quan12,
                                   quan13=quan13, quan14=quan14, quan15=quan15,
                                   quan16=quan16, quan17=quan17, quan18=quan18,
                                   quan19=quan19, quan20=quan20)
    quan0 = inventory.mainQuant[0]
    quan1 = inventory.mainQuant[1]
    quan2 = inventory.mainQuant[2]
    quan3 = inventory.mainQuant[3]
    quan4 = inventory.mainQuant[4]
    quan5 = inventory.mainQuant[5]
    quan6 = inventory.mainQuant[6]
    quan7 = inventory.ingredientQuant[0]
    quan8 = inventory.ingredientQuant[1]
    quan9 = inventory.ingredientQuant[2]
    quan10 = inventory.ingredientQuant[3]
    quan11 = inventory.ingredientQuant[4]
    quan12 = inventory.sideQuant[0]
    quan13 = inventory.sideQuant[1]
    quan14 = inventory.sideQuant[2]
    quan15 = inventory.sideQuant[3]
    quan16 = inventory.sideQuant[4]
    quan17 = inventory.sideQuant[5]
    quan18 = inventory.sideQuant[6]
    quan19 = inventory.sideQuant[7]
    quan20 = inventory.sideQuant[8]
    return render_template('inventory.html', quan0=quan0, quan1=quan1,
                                   quan2=quan2, quan3=quan3, quan4=quan4, quan5=quan5,
                                   quan6=quan6, quan7=quan7, quan8=quan8, quan9=quan9,
                                   quan10=quan10, quan11=quan11, quan12=quan12,
                                   quan13=quan13, quan14=quan14, quan15=quan15,
                                   quan16=quan16, quan17=quan17, quan18=quan18,
                                   quan19=quan19, quan20=quan20)

@app.route('/viewOrders', methods=['POST', 'GET'])
def viewOrders():   
    if request.method=="POST":
        if request.form.get('complete') == 'complete':
            staff.setStatus(0)
            order = staff.viewOrder
            return render_template('viewOrders.html', order=order)
        else:
            order = staff.viewOrder
            return render_template('viewOrders.html', order=order)
            
    if any(staff.order) == False:
        return render_template('viewOrders.html')
    else:
        order = staff.viewOrder
        return render_template('viewOrders.html', order=order)

# from src.location import Location
# # from src.error import BookingError, LoginError
# from src.customer import Customer




# '''

# Dedicated page for "page not found"
# '''
# @app.route('/404')
# @app.errorhandler(404)
# def page_not_found(e=None):
#     return render_template('404.html'), 404



# '''
# Search for Cars
# '''
# @app.route('/', methods=["GET", "POST"])
# def cars():

#     if request.method == 'POST':
#         make  = request.form.get('make')
#         model = request.form.get('model')

#         if make == '':
#             make = None

#         if model == '':
#             model = None

#         cars = system.search_car(make, model)
#         return render_template('cars.html', cars = cars)
    
#     return render_template('cars.html', cars = system.cars)




# '''
# Display car details for the car with given rego
# '''
# @app.route('/cars/<rego>')
# def car(rego):
#     car = system.get_car(rego)

#     if not car:
#         abort(404)

#     return render_template('car_details.html', car=car)


# '''
# Make a booking for a car with given rego
# '''
# from src.forms import BookingForm
# @app.route('/cars/book/<rego>', methods=["GET", "POST"])
# def book(rego):
#     car = system.get_car(rego)

#     if not car:
#         abort(404)
    

    
#     if request.method == 'POST':

#         form = BookingForm(request.form)
#         userdata = {}
#         #check the error
#         errors = {}
#         #if the field has an error then it will print it, otherwise print None
#         #print(form._field("customer_name").error)
#         for ele in form.fields:
#             if ele.data is not None:
#                 if isinstance(ele.data, datetime):
#                     userdata[ele.name] = ele.data.strftime("%Y-%m-%d")
#                 else:
#                     userdata[ele.name] = ele.data

#                 # print(ele.data)
#                 # print(type(ele.data))
#             if ele.error is not None:
#                 errors[ele.name] = ele.error


#         #add other error
#         if len(form.other_errors) != 0:
#             # if form.other_errors['period']:
#             errors["period"] = form.other_errors['period']


#         fee = system.check_fee(car,form._field("start_date").data, form._field("end_date").data)

#         if request.form.get("confirmed") == "1":
#             booking = system.make_booking(form.customer_name,car,form.start_date,form.end_date,form.start_location,form.end_location)
#             returnlist = str(booking).split('\n')
#             return render_template('booking_confirm.html', booking = returnlist)
#         #grab user input
#         return render_template('booking_form.html', car = car, errors = errors, userdata = userdata, fee = fee)    

        
# # @app.route('cars/booking_confirm/<rego>', method = ["GET","POST"])
# # def booking_confirm(rego):
# #     form = BookingForm(request.form)

# #     return render_template('booking_confirm.html', )



#         # print(form.)

#         '''
#         IMPLEMENT THIS SECTION
#         '''
        
#         # 1. If form is not valid, then display appropriate error messages


#         # 2. If the user has pressed the 'check' button, then display the fee


#         # 3. Otherwise, if the user has pressed the 'confirm' button, then 
#         #   make the booking and display the confirmation page


#     return render_template('booking_form.html', car=car, errors = None, userdata = None)



# '''
# Display list of all bookings for the car with given 'rego'
# '''
# @app.route('/cars/bookings/<rego>')
# def car_bookings(rego):
#     return render_template('bookings.html', bookings=system.get_bookings_by_car_rego(rego))