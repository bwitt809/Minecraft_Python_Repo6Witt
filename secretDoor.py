from mcpi.minecraft import Minecraft
mc = Minecraft.create()

diamondBlock = 57

gift = mc.getBlock(107, 6, 106)
if gift != 0:
    gift = mc.getBlock(107, 6, 106)
    if gift == diamondBlock:
            mc.setBlock(112, 11, 115, 0)
            mc.setBlock(112, 12, 115, 0)
else:
    mc.postToChat("Place an offering on the pedestal.")
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y - 1, z, 10)

