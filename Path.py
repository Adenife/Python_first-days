#import os
#or
import subprocess

#os.startfile('C:/Users/OLUWANIFEMI ADEOLA/Pictures')
#to make it default/flexible so it can work on any other system
print('Enter 1 to save, Enter 2 to save as')
choice = input('>')

if choice == "1":
    print('saved')
elif choice == "2":
    subprocess.Popen('explorer "C:/Users/Pictures" ')
    print('save successful')
