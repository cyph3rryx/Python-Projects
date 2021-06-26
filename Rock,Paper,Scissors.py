#Rock, Paper, Scissors game:

def greet(name):
    print("Bababoi!" + name)

a = input("Your good name: ")

greet(a)

print("Let the game begin! Good luck!\n")
import random
def gameWin(comp, h):
    if comp == h:
        return  None
    elif comp == 'r':
        if h =='s':
            return False
        elif h == 'p':
            return True
    elif comp == 's':
        if h =='r':
            return False
        elif h == 'p':
            return True
    elif comp == 'p':
        if h =='r':
            return False
        elif h == 's':
            return True

print("Computer turn: Rock(r), Paper(p), Scissors(s) ? ?\n")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

h = input(str(a) + "'s turn: Rock(r), Paper(p), Scissors(s) ?\n")
b = gameWin(comp, h)

print(f"Computer chose {comp}")
print(str(a) + f" chose {h} ")

if  b:
    print(str(a) + " Win!Congratulations!")
else:
    print(str(a) + " Lose! Better luck next time!")




















    