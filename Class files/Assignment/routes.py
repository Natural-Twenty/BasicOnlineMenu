from flask import render_template, request, redirect, url_for, abort
from server import app
from datetime import datetime




@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('login.html')




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