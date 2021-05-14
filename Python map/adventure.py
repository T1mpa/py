import random
import time

class Person():
  def __init__(self, name, age, hp, ad, ap, lvl):
    self.name = name
    self.age = age
    self.hp = hp
    self.ad = ad
    self.ap = ap
    self.lvl = lvl

namn = input("Vad Heter Du")
ålder = input("Hur Gammal är du")

p1 = Person((namn),(ålder), 200, 20, 20, 1)



hpotion = 2



answer = input("Would You Like To Play The Game (yes/no)")

if answer.lower().strip() == "yes":

    answer = input("You Reach a crossroad, Would you like to go left or right?").lower().strip()
    if answer == "left":
        answer = input("You have encountered a monster, Would you like to run or fight?")
        
        if answer == "fight":
            answer = input("You defeated the monster but you got hurt, you have "+ str(hpotion) + " health potions would you like to drink one of them (yes/no)")
            if answer == "yes":
                hpotion -= 1
                answer = input("")
            else:
                print("You went to sleep that night and your blood attracted wild beast that killed you in your sleep")
        
        elif answer == "run":
            answer = input("You")


           


    elif answer == "right":
        print("You died")






        
else:
    print("That's to bad")


print(p1)
time.sleep(10)  