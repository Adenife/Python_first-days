#working with lists
#creating a list having sublists
fam = [['dami',440],
       ['tobi',320],
       ['nifemi',600]]
#creating a normal list
fam2 = ['me',220,'dami',340,'tobi',330]

#changing the value in index 3
fam2[3] = 210
#changing the value of index 1 and 2
fam2[0:2] = ['Nifemi', 110]
#deleting the value of index 2
del(fam2[2])
#adding a new value to the list
fam2 = fam2 + ['daniel',330]
#another way of adding a new value to the list
fam2.append(['nifei',3300])
#inserting a new value to a particular index in the list
fam2.insert(3, 'tayo')

print(fam2)
print (fam)
#printing the value in index 2 and 3
print(fam2[2:4])
#printin gthe values from index 0 to 2
print(fam2[:2])
#printing the values from index 2 upwards
print(fam2[2:])
