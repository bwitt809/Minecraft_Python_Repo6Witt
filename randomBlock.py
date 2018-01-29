from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

gold = 41
diamond = 57
melon = 103
pumpkin = 86
iron = 42
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

blocks = [gold, diamond, melon, pumpkin, iron]
blocksChosen = random.choice(blocks)
mc.setBlock(x, y, z, blocksChosen)
