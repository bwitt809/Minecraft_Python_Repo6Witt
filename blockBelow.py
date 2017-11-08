from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 10
y = y - 1
mc.setBlock(x, y, z, blockType)
y = y + 10
mc.player.setTilePos(x, y, z)
