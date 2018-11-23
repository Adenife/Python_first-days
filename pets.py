'''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
'''

'''animal = [2,5,6,7,8]
animal.append(9)
print(animal)

Dic = {[glory: 08064235676], [bolu: 09056748976]}
print(dic[1])'''


kiva = {'Dog': 'Daniel'}
troll = {'Cat': 'Joshua'}
zain = {'Dog': 'Jeremiah'}

pets = []

#for pet in pets:
  #  print(pet)
    

for no, nam in kiva.items():
    one = "The pet is a "+no+" and "+nam+" is the owner."
    pets.append(one)

for pet in pets:
    print(pet)
