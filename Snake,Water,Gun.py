#Snake,Water,Gun game:

def greet(name):
    print("Bababoi!" + name)

a = input("Your good name: ")

greet(a)

print("Let the game begin! Good luck!\n")
import random
def gameWin(comp, h):
    if comp == h:
        return  None
    elif comp == 's':
        if h =='w':
            return False
        elif h == 'g':
            return True
    elif comp == 'w':
        if h =='g':
            return False
        elif h == 's':
            return True
    elif comp == 'g':
        if h =='s':
            return False
        elif h == 'w':
            return True

print("Computer turn: Snake(s), Water(w), Gun(g) ?\n")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

h = input(str(a) + "'s turn: Snake(s), Water(w), Gun(g) ?\n")
b = gameWin(comp, h)

print(f"Computer chose {comp}")
print(str(a) + f" chose {h} ")

if b == None:
    print("The game ends in a tie!\n")
elif b:
    print(str(a) + " Win!Congratulations!")
else:
    print(str(a) + " Lose! Better luck next time!")
