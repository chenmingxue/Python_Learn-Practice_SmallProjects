class Vehicle: #define class
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity): #constructor
        self._number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    def set_number_of_wheels(self, number=6):#setter
        self._number_of_wheels = number
    def get_number_of_wheels(self):#getter
        return self._number_of_wheels
    def make_noise(self, noise="Weeeeee"):
        print(noise)



if __name__ == "__main__":
    tesla_model_s=Vehicle(4, "electric", 5, 250) #create an instance of a class of objects of Vehicle
    print(tesla_model_s._number_of_wheels)
    tesla_model_s.set_number_of_wheels()#set new number of wheels value
    print(tesla_model_s.get_number_of_wheels())
    tesla_model_s.make_noise("eeeeeeeee")
