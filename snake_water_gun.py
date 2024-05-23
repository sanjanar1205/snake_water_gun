import random

def game(i, you):
    if i == you:
        return None
    if i == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    if i == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    if i == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

name = input("Your Name: ")
print("My Turn: Snake(s) Water(w) or Gun(g)")
num = random.randint(1, 3)

if num == 1:
    i = 's'
elif num == 2:
    i = 'w'
elif num == 3:
    i = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = game(i, you)
print("I chose", i)
print(name, "chose", you)
if a is None:
    print("It's a TIE!") 
elif a:
    print("Congratulations",name,"you WON!")
else:
    print("Sorry",name,"you LOST!")
