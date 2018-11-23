'''
Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
'''
'''Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
'''

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
        self.okay = Priviledges()

    def describe_user(self):
        okay = "First name is: "+self.first_name.title()+"\nLast name is: "+self.last_name.title()+"\nOther name is: "+str(self.age.title())+"."
        return okay

    def greet_user(self):
        now = "Welcome "+self.first_name.title()+"!!!"
        return now
    
    def increment_login_attempts(self):
            self.login_attempts += 1
            return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

class Priviledges():
    def __init__(self, priviledge = ['Can add user', 'Can remove users', 'Can change passwords']):
        self.priviledge = priviledge

    def admins(self):
        thing = self.priviledge
        for things in thing:
            print("An Admin can: "+things)
    

info =  User("Aweda", "Oluwanifemi", "18")
print(info.describe_user())
print(info.greet_user())
print(info.increment_login_attempts())
print(info.increment_login_attempts())
print(info.increment_login_attempts())
print(info.reset_login_attempts())
info.okay.admins()
    
info1 =  User("Tayo", "Adeoye", "17")
print(info1.describe_user())
print(info1.greet_user())

info2 =  User("Oseni", "Daniel", "18")
print(info2.describe_user())
print(info2.greet_user())
