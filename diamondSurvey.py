from mcpi.minecraft import Minecraft
mc = Minecraft.create()


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
    
for distance in range(0, 50):
    
    block = mc.getBlock(x, y - 1, z)
    if block == 56:
        mc.postToChat("Diamond ore is " + str(pos.y - y) + " below you.")
    else:
        y = y - 1
    
        mc.postToChat("No diamond ore found below you.")
    if block == 56:
        break
    
