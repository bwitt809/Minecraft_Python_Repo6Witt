from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {'Kasheem': 0, 'Darius': 0, 'Joaquin': 0, 'Barnaby': 0, 'Rando': 0, 'Karim': 0, 'Requis': 0, 'JaJa': 0, 'Cyanide': 0, 'Jaekebulike': 0}

while True:
    name = input("What is your name? ")
    if name == "exit":
        break
    mc.postToChat("Go!")

    time.sleep(10)

    blockHits = mc.events.pollBlockHits()

    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockHitsLength))
    scoreboard[name] = blockHitsLength
    for name in scoreboard:
        print(name + ' ' + str(scoreboard[name]))
    
