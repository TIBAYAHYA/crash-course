from car import Car
new_car = Car("BMW","M4","2024")
new_car.increment_odometer(100)
new_car.read_odometer()
from car import ElectricCar
my_tesla = ElectricCar("Tesla","Cybertruck","2022")
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
