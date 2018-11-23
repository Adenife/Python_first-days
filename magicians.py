'''
8-9. Magicians: Make a list of magician’s names. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

8-10. Great Magicians: Start with a copy of your program from Exercise 8-9. Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.

8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list. Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name
'''

def show_magicians(names, name):
    for magicians in names:
  #while magician:
           print(magicians.title())
           great_magician.append(magicians)
           #return magicians.title()
        
def make_great(great_magician):
    for magicina in great_magician:
          print("Great "+magicina)
            #return magicina
        
magician = ['merlin', 'lancelot', 'cassie', 'goblin', 'grim-reaper']
great_magician = []

show_magicians(magician[ : ], great_magician)
make_great(great_magician)

#print("Great " +make_great(great_magician))
#print(show_magicians(magician, great_magician))


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('albert', 'einstein',
                                    location='princeton',
                                    field='physics')
print(user_profile)

