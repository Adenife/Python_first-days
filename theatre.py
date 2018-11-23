initial = True
score1 = 0
score2 = 0
score3 = 0
#age = int(input("Input age: "))
while initial:
    print("Enter  81 and above to quit")
    age = int(input("Input age: "))
    end = input
    if age < 3:
        print("Tickets for children of age "+str(age)+" is free")
        score1 += 1
    elif age >= 3 and age <= 12:
        print("Tickets for children of age "+str(age)+" is $10")
        score2 += 1
    elif age > 12 and age <= 80:
        print("Tickets for children of age "+str(age)+" is $15")
        score3 += 1
    else:
        print("Thank you")
        #break ---- ends the program and restarts it immediately
        #using a flag ends the program totally
        initial = False
        #continue ---- continues the program from this point and ignores the rest of the program
        print("Free watchers are: "+str(score1)+".")
        print("$10 watchers are: "+str(score2)+".")
        print("$15 watchers are: "+str(score3)+".")
