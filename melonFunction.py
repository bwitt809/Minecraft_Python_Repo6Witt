from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def getMelon (x, y, z):
    count = 0
    while count < 6:
        pos = mc.player.getPos()
        x = pos.x
        y = pos.y
        z = pos.z
        mc.setBlock(x, y - 1, z, 103)
        time.sleep(10)
        count += 1
getMelon(x, y, z)
