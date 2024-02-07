from django.contrib import admin
from .models import (
    Toyota, 
    Honda, 
    Nissan, 
    BMW, 
    MercedesBenz, 
    Volkswagen, 
    Lexus, 
    Subaru, 
    Mazda, 
    Ford, 
    Chevrolet,
    PassengerCar
    )

car_brands = [Toyota, 
              Honda, 
              Nissan, 
              BMW, 
              MercedesBenz, 
              Volkswagen, 
              Lexus, 
              Subaru, 
              Mazda, 
              Ford, 
              Chevrolet,
              PassengerCar]

# Register each car brand model
for car_brand in car_brands:
    admin.site.register(car_brand)
