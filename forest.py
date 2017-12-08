from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
def growTree(x, y, z):
    wood = 17
    leaf = 18
    mc.setBlocks(x, y, z, x, y + 5, z, wood)
    mc.setBlocks(x - 3, y + 4, z - 3, x + 3, y + 7, z + 3, leaf)
def growForest(x, y, z):
    count = 0
    while count < 10:
        growTree(x, y, z)
        x += 7
        z += 7
        count += 1

growForest(x, y, z)
