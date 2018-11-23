import random

'''playing = True
while playing:
    answer = random.choice(range(101))
    guess = input("Enter your lucky number ")

    if int(guess) == answer:
        print("You really are lucky")
            
    else:
        print("Wrong Number")

    again = input("Enter any number to continue and enter 0 to quit: ")
    if int(again) == 0:
        playing = False
    else:
        playing = True
        '''

while True:
    answer = random.choice(range(101))
    guess = input("Enter your lucky number ")

    if int(guess) == answer:
        print("You really are lucky")
            
    else:
        print("Wrong Number")

    again = input("Enter any number to continue and enter 0 to quit: ")
    if int(again) == 0:
        break
    else:
        continue
        
    
