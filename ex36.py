from sys import exit
global hp


def start():
  global hp
  hp=3
  print("Hi and welcome. Enter to continue.")
  input("> ")
  print("You choose to enter")
  hpc()
  main_hall()

def main_hall():
  print("You see a big hall with a red door and a blue door. Where do you go?")
  door = input("> ")
  if "red" in door:
    red_room()
  elif "blue" in door:
    blue_room()
  else:
    die("Unable to choose a sensible answer, the dungeon master kicks you out of the game.")

def red_room():
	global hp
	print("*****")
	print("You enter a room with walls painted red.")
	input()
	print("A little boy with an axe stands in the middle.")
	input()
	print("The little boy says: 'Welcome to the redrum!' with a snark on his face.")
	input()
	print('I like hacking people to pieces!')
	input()
	red_combat()


def red_combat():
  global hp
  print("What do you do?")
  RR = input("> ")
  if "attack" in RR or "hit" in RR or "kill" in RR or "kick" in RR or "lunge" in RR or "beat" in RR or "taunt" in RR:
    print("You attempt to", RR, "the boy, but unfortunately, you fail miserably.")
    input()
    print("The boy blocks your", RR, "attempt and swings his axe.")
    print("The axe hits its mark. You gush blood.")
    hp-=1
    input()
    hpc()
    red_combat()
  elif "dodge" in RR or "prevent" in RR or "anticipate" in RR or "block" in RR or "defend" in RR or "avoid" in RR:
    print("The boy swings his axe, but you manage to", RR, "it, great!")
    hpc()
    red_combat()
  elif "food" in RR or "feed" in RR or "candy" in RR or "cookie" in RR or "treat" in RR or "sweet" in RR or "dessert" in RR :
    print( "You give ", RR, " to the boy. He looks very happy and starts munching on your ", RR,".", sep="")
    input()
    print("The boy falls asleep thanks to the sleeping powder you put in the food, you're smart aren't you?")
    input()
    print("You spot a door behind the sleeping boy.")
    input()
    boss_room()
  else:
    print("You don't have a high enough int to do \"",RR,"\", choose another action!", sep="")
    red_combat()


def blue_room():
  global hp
  print("*****")
  print("You enter a blue room")
  input()
  print("All this blue is making you feel blue")
  input()
  print("You start losing hp")
  input()
  while True:
    hp-=1
    hpc()

def die(why):
  print(why, " Good job!")
  print("Do you wish to restart your adventure? (y/n)")
  choice = input("> ")
  if choice == "y":
    start()
  elif choice == "n":
    exit(0)
  else:
    die("heh")


def hpc():
  global hp
  if hp<=0:
    die("You are at 0 health. You must have lost a limb or maybe burnt to a crisp, too bad.")
  else:
    print("You have", hp, "hp left")
    input()

def boss_room():
  global hp
  hpc()
  print("*****")
  print("You enter the door. The room is dark. Suddenly a metal grating sound erupts in your ears.")
  input()
  print("You turn around and see that metal bars appeared over the door and locked the door. You are trapped!")
  input()
  print("You walk forward, and stumble upon a chest.")
  input()
  print("Do you want to open the chest? (y/n)")
  choice = input("> ")
  if choice=="y":
    print("You kick the chest. A magical golden light seeps through the cracks in the lid. It opens.")
    input()
    print("A familiar jingle resounds, while the contents of the chest starts to float.")
    input()
    print("You lose control of your limbs, and somehow do a little spin, and raise your hand.")
    input()
    print("The piece of heart that was in the chest floats onto your hand.")
    input()
    print("Congratulations! you just regained some life!")
    hp+=1
    hpc()
    boss_fight()
  elif choice=="n":
    boss_fight()
  else:
    boss_fight()

def boss_fight():
  global hp
  print("""
Suddenly a blinding light erupts. You see that the room is circular with grey, barren walls.
A black shadow appears up high, and becomes bigger and bigger every second.
You see both wings touching the walls. You see claws dwarfing your sword.
The black, scaly creature crashes down in the center of the room.\n""")
  print("A shockwave is starting to form. What do you do?")
  choice = input("> ")
  if "jump" in choice or "dodge" in choice:
    print("You jump over the shockwave. Phew, that was close !")
    input()
  else:
    print("You don't react fast enough and get hit by the shockwave. You hear your bones crack")
    hp-=2
    hpc()
  print("The winged creature open its eyes. Dark spheres with a hint of red core glare down at you")
  input()
  print("It opens its mouth. A fireball forms in its gigantic maw.")
  input()
  print("What do you do?")
  c2 = input("> ")
  if "shield" in c2:
    print("The dragon spews its fiery breath at you. You raise your shield in time to protect yourself.")
    input()
    print("Your shield melts a little under the heat, hurting your left arm.")
    hp-=1
    hpc()
  elif "dodge" in c2 or "jump" in c2:
    print("You attempt to", c2, "the wave of fire.")
    print("Unfortunately, you are not agile enough, and you start burning !")
    while True:
      hp-=1
      hpc()
  else:
    print("You want to ", c2,". Too bad that it doesn't work out. The dragon is too smart for you !", sep="")
    input()
    print("The fireball is hurled to your face. You try to evade but your green tunic catches on fire.")
    input()
    while True:
      hp-=1
      hpc()
  print("The dragon is open, it's time to attack! what do you do? Use your best attack!")
  finisher = input("> ")
  print("You", finisher, "the dragon in a heroic and courageous manner")
  input()
  print("The dragon is dead. Congratulations!")
  input()
  print("""
-----------------------------
-------------|||-------------
------------|||||------------
-----------|||||||-----------
----------|||||||||----------
---------|||||||||||---------
--------|||||||||||||--------
-------|||||||||||||||-------
------|||-----------|||------
-----|||||---------|||||-----
----|||||||-------|||||||----
---|||||||||-----|||||||||---
--|||||||||||---|||||||||||--
-|||||||||||||_|||||||||||||-
-----------------------------""")
  die("You finished the game!")


start()
