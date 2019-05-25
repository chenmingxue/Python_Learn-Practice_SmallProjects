#example of encapsulation 1
class Person:
    def __init__(self, fname, email):
        self.first_name = fname #public variable
        self._email = email   #private variable (_string) is used for encapsulation: the private variable is used only internally

    def update_email(self, email):
        self._email = email

    def get_email(self):
        return self._email

tk = Person('tk','tk@email')
print(tk.first_name, tk.get_email())
tk.update_email('new@email')
print(tk.get_email())

#example of encapsulation 2
class Person:
    def __init__(self, fname, age):
        self.first_name = fname
        self._age = age

    def show_age(self):
        return self._get_age() #here function is private and cannot be reached externally

    def _get_age(self):
        return self._age

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
        #Car.__init__(self, num_of_wheels, seating_capacity, max_velocity)
        super().__init__(num_of_wheels, seating_capacity, max_velocity) #use super()
        self.battery = battery
        self.state = ''

    def sold_in_state(self, sold_state):
        self.state = sold_state


electricCar = ElectricCar(4, 5, 250, "1000V")
electricCar.sold_in_state("CA")
electricCar.make_noise()
print(electricCar.num_of_wheels)
print(electricCar.battery)
print(electricCar.state)
