
from car import Car
from electric_car import ElectricCar
my_car = Car("BMW","M4",2020)
print(my_car.get_descriptive_name())
my_ev = ElectricCar("Tesla","Cybertruck",2025,battery_range=75)
print(my_ev.get_descriptive_name())
my_ev.battery.get_range()