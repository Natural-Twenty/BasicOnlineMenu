from flask import render_template, request, redirect, url_for, abort, session
from server import app, system
from src.Customer import Customer
from src.Order import Order
from src.Side import Side
from src.Main import Main
from src.Ingredient import Ingredient




def createObject(name,unitPrice, quantity):
    mainFlag = False
    sideFlag = False
    drinkFlag = False

    for ele in system.mainList:
        if ele.name == name:
            mainFlag = True
            main = Main(name,unitPrice,quantity)
            return main


    # for ele in system.sidesList:
    #     if ele.name == name:
    #         sideFlag = True
    #         side = Side()

    # if mainFlag == False and sideFlag == False:
    #     for ele in system.drinksList:
    #         if ele.name == name:
    #             drinkFlag = True



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST' and request.form.get('logout') == 'True':
        session['username'] = None

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
            #find the customer
            session['username'] = username
            print(session['username'])

            return redirect(url_for('home'))
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
        customer = Customer(username,username+'@gmail.com',username,password,[])
        system.add_customer(customer)
        session['username'] = username
        return render_template('home.html')
    else:
        return render_template('register.html')



@app.route('/menu', methods=['GET','POST'])
def menu():
    if request.method == 'POST' and request.form.get('menu') == 'True':
        print(dict(request.form))
        order = Order(system.Oid_incre())

        print(order)
        for ele in request.form:
            if dict(request.form)[ele] != '' and ele != 'menu' and request.form[ele] != '':
                #get name
                content = ele.split("_")
                name = content[0]
                #get unitPrice
                for ele2 in system.mainList:
                    if name == ele2.name:
                        price = ele2.unitPrice
                        print(request.form[ele])
                        obj = createObject(name,price,request.form[ele])
                        for ele7 in system.mainList:
                            if obj.name == ele7.name:
                                for ele8 in ele7.ingredients:
                                    obj.add_ingre(ele8)



                        order.add_food(obj)
                        break


                
                
        
        #find user
        for ele3 in system.customerList:
            if ele3.username == session['username']:
                ele3.add_order(order)
                break


        order.getPrice()
        #cost ingre
        system.add_order(order)
        err = {}
        for ele4 in order.foods:
            print("here")
            print(ele4)
            print(ele4.ingredients)
            for ele5 in ele4.ingredients:
                print("here2")
                print(ele5)
                for ele6 in system.inventory:
                    if ele6.name == ele5.name:
                        print(ele6.name)
                        print("and")
                        print(ele5.name)
                        tmp = int(ele6.quantity) - int(ele5.quantity)
                        if tmp < 0:
                            err['err'] = 'Ran out of stock'
                        else:
                            ele6.quantity = tmp




        for ele in system.customerList:
            if session['username'] == ele.username:
                user = ele
        return render_template('home.html', user = user, err = err)
    return render_template('menu.html', a = system.mainList)

@app.route('/home',methods=["GET", "POST"])
def home():
    for ele in system.customerList:
        if session['username'] == ele.username:
            user = ele
            if session['username'] == 'admin':
                admin = 'True'

            return render_template('home.html', user = user, admin = admin)




    return render_template('home.html')

@app.route('/inventory',methods=["GET", "POST"])
def inventory():
    if request.method == 'POST':
        print(dict(request.form))
        for ele in request.form:
            if request.form[ele] != '' and ele != 'submit':
                print("yes")
                print(request.form[ele])
                name = str(ele)
                print(name)
                for ele2 in system.inventory:
                    if ele2.name == name:
                        tmp = ele2.quantity+int(request.form[ele])
                        ele2.quantity = tmp



    return render_template('inventory.html', inve = system.inventory)

@app.route('/orders',methods=["GET", "POST"])
def orders():
    if request.method == 'POST':
        for ele in system.orderList:
            ele.status = 1


        for ele in system.customerList:
            if session['username'] == ele.username:
                user = ele
                if session['username'] == 'admin':
                    admin = 'True'
            return render_template('home.html',user = user, admin = admin)

    return render_template('viewOrders.html',orders = system.orderList)
'''
Display the menu page
'''
# @app.route('/login/menu', methods=["GET", "POST"])
# def menu():
#     mainList = ['burger', 'wrap', 'muffin', 'sesame', 'chicken', 'vegetarian', 'beef']
#     sidesList = ['3 pack nuggets', '6 pack nuggets', '0.2 kg small fries', '0.4 kg medium  fries', '0.6 kg large fries']
#     drinksList = ['375mL can of coke', '600mL bottle of water']
#     ingredientList = ['Tomato', 'Lettuce', 'Tomato sauce', 'cheddar cheese', 'swiss cheese']
#     if request.method == 'GET':
#         return render_template('menu.html')
#     else:
#         return render_template('menu.html', main = mainList, sides = sidesList, drinks = drinksList, ingredient = ingredientList)
'''
Make an order
'''
# @app.route('/login/menu/order', methods=["GET", "POST"])
# def order():
#     if request.method == "POST":
#         if "confirm order" in request.form:
#             order = system.make_order(customer, car, request.form.getList('mainList', 'sidesList', 'drinksList', 'ingredientList'))
#             orderData = dict(order = order)
#         return render_template('confirmation.html', request.form.getList('mainList', 'sidesList', 'drinksList', 'ingredientList'), data = orderData)
#     else:
#         return render_template('menu.html')
        
'''
Home page
May have to use return redirect(url_for('')) instead of render template
'''
# @app.route('/home', methods=['POST', 'GET'])
# def home():
#     if session['username'] != 'admin':
#         message = {}
#         message['customer'] = 'True'







#     if request.method=="POST":
#         orderID = int(request.form.get('orderID'))
#         if orderID < 0:
#             message = "error"
#             return render_template('home.html', message=message)
#         orders = Staff.order
#         for i in range(0,len(orders)):
#             if orderID == orders[i].orderID:
#                 main = orders[i].main
#                 main_bun_no = orders[i].main_bun_no
#                 main_bun_type = orders[i].main_bun_type
#                 ingredient = orders[i].ingredients
#                 sides = orders[i].sides
#                 drinks = orders[i].drinks
#                 price = orders[i].mainPrice + orders[i].sidePrice + orders[i].ingredientsPrice + orders[i].drinkPrice
#                 status = orders[i].status                
#                 return render_template('StatusPage.html', orderID=orderID, main=main, main_bun_no=main_bun_no, main_bun_type=main_bun_type,
#                                         ingredient=ingredient, sides=sides, drinks=drinks, price=price, status=status)
#         message = 'error'
#         return render_template('home.html', message=message)


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