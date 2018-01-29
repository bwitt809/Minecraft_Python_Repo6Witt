from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {'Kasheem', 'Darius', 'Joaquin', 'Barnaby', 'Rando', 'Karim', 'Requis', 'JaJa', 'Cyanide', 'Jaekebulike'}

while True:
    name = input("What is your name? ")
    if name == "exit":
        break
    mc.postToChat("Go!")

    time.sleep(60)

    blockHits = mc.events.pollBlockHits()

    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockHitsLength))


    print(scoreboard)
