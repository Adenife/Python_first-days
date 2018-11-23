'''
Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
'''
'''
Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and
print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any
number you like that could represent how many customers were served in, say, a day of business.
'''
'''
Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        ok = "Welcome to "+self.restaurant_name.title()+".\nCuisine type is "+self.cuisine_type+".\nNumber of customers served is "+str(self.number_served)+"."
        return ok

    def open_restaurant(self):
        now = self.restaurant_name.title()+" is now open."
        return now

    def set_number_served(self):
        self.number_served = 20
        new = "Number of customers served is "+str(self.number_served)+"."
        return new

    def increment_number_served(self):
       #print("Number of customers served is "+str(self.number_served)+".")
       self.number_served += 1
       return self.number_served
    
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour_type = ['Peanuts', 'Strawberry']

    def flavour(self):
        old = self.flavour_type
        for olds in old: 
            print("This flavours is available: ")
            print(olds)
        
info = Restaurant("Adenife's Treat", "VVIP")
info1 = IceCreamStand("Adenife's Treat", "VVIP")
info.number_served = 5
print(info.describe_restaurant())
print(info.open_restaurant())
print(info.set_number_served())
print(info.increment_number_served())
print(info1.describe_restaurant())
info1.flavour()




