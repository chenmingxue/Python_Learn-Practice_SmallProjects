#example of encapsulation 1
class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name #public variable
        self._email = email   #private variable, use for encapsulation: the private variable is used only internally

    def update_emai(self, new_email):
        self._email = new_email

    def email(self):
        return self._email

tk = Person('tk','tk@email')
print(tk.first_name, tk.email())
tk.update_emai('new@email')
print(tk.email())

#example of encapsulation 2
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):
        return self._age

tk = Person('tk', 20)
print(tk.show_age())

#example of inheritance
class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def make_noise(self):
        print("YeeHaaaa!")

class Electric_car(Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity, battery):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)
        self.battery = battery
        self.state = ''

    def sold_in_state(self, sold_state):
        self.state = sold_state


electric_car=Electric_car(4, 5, 250, "1000V")
electric_car.sold_in_state("CA")
electric_car.make_noise()
print(electric_car.number_of_wheels)
print(electric_car.battery)
print(electric_car.state)
