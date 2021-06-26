def greet(name):
    print("Bababoi!" + name)

a = input("Your good name: ")
greet(a)

print("Guess a number from 1 - 9\n")

def done():
    Sachin = input("Is it done? Yes or No\n")
    if Sachin == "Yes":
        return "Proceed Further\n"
    elif Sachin == "No":
        return done()

print(done())

print("Double the number by multiplying the number with the same number.\n")
print(done())

import random
randNo = random.randint(1,100)

num = randNo/2
b = randNo

print(f"Now add the {b} to your last answer\n")
print(done())

print("Now divide the number you got in the last answer by 2\n")
print(done())

print("Now subtract the main number from the last answer \n")
print(done())

print(f"The number you got is the {num}\n")
print("Thanks for playing the game!\n")
