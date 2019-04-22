from flask import Flask
from init import order_system
from src.Staff import Staff
from src.Inventory import Inventory

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

system = order_system()

staff = Staff()
inventory = Inventory()