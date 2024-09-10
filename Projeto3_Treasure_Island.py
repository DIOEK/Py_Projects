"""A little interactive word game. May be cool to come back to and elaborate it with some new mechanics or other stuff"""


print("Welcome to treasure island!\nYour mission is to find the pirate's treasure!\nYAAAAARRRRRGGHHH!!")
print("Pay attention, only type exactly the answers offered!")
print(100*("-"))
print("Suddenly, you stand before a rock corridor, the sound of your steps echo through the rocky walls.\nYou stand before a bifurcation")
left_or_right = input("Do you want to go left or right? (left/right): ")
if left_or_right.lower() == "left":
 print('As you keep going foward, you find yourself before a great subterranean lake.\nYou can see a rope, that goes into the waters bellow.')
 pull_or_swim = input("Will you pull the rope? Or shall you swim through the murky waters?(pull/swim): ")
 if pull_or_swim.lower() == "pull":
   print("As you pull the rope, you distinguish a small boat appearing in the distance.\nIt seems old, but sturdy enough to support your weight, you traverse the dark lake. "
        "\nAfter a while in the damp darkness, you spot a faint light. "
        "\nAs you come closer, you can see a lit torch, that illuminates three doors: one Yellow, one Red and one Green." )
   door = input("Which door would you like to open? the Yellow one, the Red one or the Green one?(Y/R/G): ")
   if door.lower() == "y":
       print("Before you stands a vicious pirate, it runs you through with his cutlass.")
   elif door.lower() == "r":
       print("Before you stans a dark, hungry beast, before you can run, it is upon you.")
   elif door.lower() == "g":
       print("Before you stands gold and riches untold! Congratulations, you are now a rich man!")
   else:
       print("As you just stand there and wait trying to find a way to put your new plan into action, a band of pirates approaches you through by the lake"
             "\nOne of them pulls a flintlock and shoots you in the back.")
 else:
     print("You have been eaten by crocodiles you fool!")

else:
 print("You fell into a chasm and died, sorry my guy!")
