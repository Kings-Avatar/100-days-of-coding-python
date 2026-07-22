print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\nYou are at a wall.")
x=input("Do you wanna jump or go back to find other ways? if jump then type j if you wanna go back type gb")
if x=="j":
    print("You just encountered an lion")
    l=input("Do you want to throw stone at it or run? If you want to throw ston type s or type r")
    if l=="s":
        print("You've just killed a lion, keep walking\nA waterfalls has been spotted\nDo you want to go near or stay.")
        w=input("If go near type n or type s")
        if w=="n":
            print("You've found the lost treasure!!")
        elif w=="s":
            print("You've been killed by an arrow")
        else:
            print("Can't even follow instructions properly. YOU'RE DEAD")
    elif l=="r":
        print("The lion caught you up,and chewed you alive!!. YOU'RE DEAD")
    else:
        print("Can't even follow instructions properly. YOU'RE DEAD")
elif x=="gb":
    z=input("A group of zombies has been spotted\nRun or fight back. If run then type r or type fb")
    if z=="r":
        print("You've reached a safe spot, continue your journey walking\nA waterfalls has been spotted\nDo you want to go near or stay.")
        w=input("If go near type n or type s")
        if w=="n":
            print("You've found the lost treasure!!")
        elif w=="s":
            print("You've been killed by an arrow")
        else:
            print("Can't even follow instructions properly. YOU'RE DEAD")

    elif z=="fb":
        print("You're officially a living dead now!!")
    else:
        print("Can't even follow instructions properly. YOU'RE DEAD")
else:
    print("Can't even follow instructions properly. YOU'RE DEAD")
