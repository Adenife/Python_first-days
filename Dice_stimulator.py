import random


def roller():
        playing = True
        while playing == True:
                #for i in range(6):
                go = random.choice(range(7))
                print("The selected number is: "+str(go))
                print("Enter any number to play again and 0 to  exit")
                now = int(input("Enter reply--"))

                if now == 0:
                        playing = False

roller()

