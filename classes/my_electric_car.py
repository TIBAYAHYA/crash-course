from car import ElectricCar
my_tesla = ElectricCar("Tesla","Cybertruck","2023",battery_range=100)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.describe_battery()