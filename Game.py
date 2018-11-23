import random

my_dict = {
                "Base-2 number system" : "binary",
                "Number system that uses the characters 0-F" : "hexidecimal",
                "7-bit text encoding standard" : "ascii",
                "16-bit text encoding standard" : "unicode",
                "A number that is bigger than the maximum number that can be stored" : "overflow",
                "8 bits" : "byte",
                "1024 bytes" : "kilobyte",
                "Picture Element. The smallest component of a bitmapped image" : "pixel",
                "A continuously changing wave, such as natural sound" : "analogue",
                "the number of times per second that a wave is measured" : "sample rate",
                "A bunary representation of a program" : "machine code"
            }

print("Computing Reevision quize")
print("=================")

playing = True
while playing == True:

    score = 0
    num = int(input("\nHow many questions would you like: "))

    for i in range(num):
        question = random.choice(list(my_dict.keys()))
        #answer = my_dict.values()
        answer = my_dict[question]

        print("\nQuestion " + str(i+1))
        print(question + "?")
      #  print(answer)

        guess = input(">")

        if guess.lower() == answer.lower():
            print("Correct!")
            score +=1
        else:
            print("Nope!")
    print("\nYour final score is: " +str(score))
    again = input("Enter any key to play again, or 'q' to quit:      ")
    if again.lower() == 'q':
        playing = False

    