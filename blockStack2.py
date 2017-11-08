from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -5
y = 5
z = 30
blockType = 60
up = 1
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + up, z, blockType)
mc.setBlock(x + up, y, z, blockType)
mc.setBlock(x + up, y + up, z, blockType)
mc.setBlock(x, y, z + up, blockType)
mc.setBlock(x, y + up, z + up, blockType)
mc.setBlock(x - up, y, z, blockType)
mc.setBlock(x - up, y + up, z, blockType)
mc.setBlock(x, y, z - up, blockType)
mc.setBlock(x, y + up, z - up, blockType)
mc.setBlock(x, y + 2, z, blockType)
mc.setBlock(x, y - up, z, blockType)


