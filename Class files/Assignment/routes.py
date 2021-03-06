from flask import render_template, request, redirect, url_for, abort
from server import app, system
from src.Customer import Customer
from src.Order import Order
from src.Sides import Sides
from src.Main import Main
from src.Ingredient import Ingredient


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
Make an order
'''
@app.route('/login/menu/order', methods=["GET", "POST"])
def order():
    if request.method == "POST":
        food = orderList(request.form.getList)
        food_quantity = orderForm(request.form)
        if "check price" in request.form:
            checkData = dict(fee = system.check_fee(form.main, form.sides, form.drinks, form.ingredient, form.bun_number, form.nuggest_number1, form.nuggest_number2, form.fries_number1, form.fries_number2, form.fries_number3, form.sundae_number1, form.sundae_number2, form.sundae_number3, form.sundae_number4, form.sundae_number5, form.sundae_number6, form.drinks_number1, form.drinks_number2, form.drinks_number3, form.drinks_number4, form.drinks_number5, form.form.drinks_number6)
            return render_template('customise.html', orderList = request.form.getList, orderForm = request.form, data = checkData)
        if "pay now" in request.form:
            order = system.orderList(customer, form.main, form.sides, form.drinks, form.ingredient, form.bun_number, form.nuggest_number1, form.nuggest_number2, form.fries_number1, form.fries_number2, form.fries_number3, form.sundae_number1, form.sundae_number2, form.sundae_number3, form.sundae_number4, form.sundae_number5, form.sundae_number6, form.drinks_number1, form.drinks_number2, form.drinks_number3, form.drinks_number4, form.drinks_number5, form.form.drinks_number6)
            orderData = dict(order = order)
            return render_template('confimation.html', data = orderData)
        return render_template('custoise.html', form={})

        
'''
Home page
May have to use return redirect(url_for('')) instead of render template
'''
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method=="POST":
        orderID = int(request.form.get('orderID'))
        if orderID < 0:
            message = "error"
            return render_template('home.html', message=message)
        orders = Staff.order
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