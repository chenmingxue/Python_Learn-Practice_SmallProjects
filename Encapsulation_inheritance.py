#example of encapsulation 1
class Person:
    def __init__(self, fname, email):
        self.first_name = fname #public variable
        self.email = email   #private variable, use for encapsulation: the private variable is used only internally

    def update_email(self, email):
        self.email = email

    def email(self):
        return self.email

tk = Person('tk','tk@email')
print(tk.fname, tk.email())
tk.update_email('new@email')
print(tk.email())

#example of encapsulation 2
class Person:
    def __init__(self, fname, age):
        self.first_name = first_name
        self.age = age

    def show_age(self):
        return self.get_age()

    def get_age(self):
        return self.age

tk = Person('tk', 20)
print(tk.show_age())

#example of inheritance
class Car:
    def __init__(self, num_of_wheels, seating_capacity, max_velocity):
        self.num_of_wheels = num_of_wheels
        self.seating_capacity = seating_capacity
        self.max_velocity = max_velocity

    def make_noise(self):
        print("YeeHaaaa!")

class ElectricCar(Car):
    def __init__(self, num_of_wheels, seating_capacity, max_velocity, battery):
        Car.__init__(self, num_of_wheels, seating_capacity, max_velocity)
        self.battery = battery
        self.state = ''

    def sold_in_state(self, sold_state):
        self.state = sold_state


electric_car = ElectricCar(4, 5, 250, "1000V")
electric_car.sold_in_state("CA")
electric_car.make_noise()
print(electric_car.num_of_wheels)
print(electric_car.battery)
print(electric_car.state)
