prompt = '~'
print"Pick a number between 1 and 2"
pick = raw_input(prompt)

if pick == "1":
    print"You are a very good boy!"
    print"Pic a random number"

    num = raw_input(prompt)
    if num > 10:
        print"Coveteous"

elif pick == "2":
    print"Bad boy!!!"

else:
    print"Get Away!!!!"
