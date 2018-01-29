from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x, y, z = (-18.8, 2.0, 11.4)

while True:
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-0.2, 0.2)
    y = mc.getHeight(x, z)

    mc.player.setPos(x, y, z)
    time.sleep(0.1)
