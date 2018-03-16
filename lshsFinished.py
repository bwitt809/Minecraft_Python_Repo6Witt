"""This program will create of completely flat world and will also create a soccer field on the flat world"""
"""Created by: Brandon Witt"""
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
#Creates flat world
import sys
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.setBlocks(-128,0,-128,128,64,128,0)
if(len(sys.argv) > 1):
    bid = int(sys.argv[1])
else:
    bid = block.GRASS.id

if bid < 0 or bid > 108:
    bid = block.GRASS.id

mc.setBlocks(-128,0,-128,128,-64,128,bid)

x = 0.0
y = 1.0
z = 0.0
mc.player.setPos(x, y, z)
#Creates field
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 31
length = 52
blockType = 35
air = 2
mc.setBlocks(x, y - 1, z, x + width, y - 1, z + length, blockType)
mc.setBlocks(x + 1, y - 1, z + 1, x + width - 1, y - 1, z + length - 1,air)
#Creates goals
blocks = [[[42, 42, 42, 42, 42, 42, 42, 42], [42, 0, 0, 0, 0, 0, 0, 42], [42, 0, 0, 0, 0, 0, 0, 42], [42, 0, 0, 0, 0, 0, 0, 42]],
          [[30, 30, 30, 30, 30, 30, 30, 30], [30, 30, 30, 30, 30, 30, 30, 30], [30, 30, 30, 30, 30, 30, 30, 30], [30, 30, 30, 30, 30, 30, 30, 30]]]

startingX = 12.0
startingY = 1.0

for depth in blocks:
    for height in reversed(depth):
        for block in height:
            mc.setBlock(startingX, startingY, z, block)
            startingX += 1
        startingY += 1
        startingX = 12
    z -= 1
    startingY = 1.0

startingX = 12.0
startingY = 1.0
startingZ = 52

for depth in blocks:
    for height in reversed(depth):
        for block in height:
            mc.setBlock(startingX, startingY, startingZ, block)
            startingX += 1
        startingY += 1
        startingX = 12
    z += 1
    startingY = 1.0
    startingZ += 1
#Makes outline and goal box on field
blockType = 35
mc.setBlock(1.0, 0.0, 26.0, blockType)
mc.setBlock(2.0, 0.0, 26.0, blockType)
mc.setBlock(3.0, 0.0, 26.0, blockType)
mc.setBlock(4.0, 0.0, 26.0, blockType)
mc.setBlock(5.0, 0.0, 26.0, blockType)
mc.setBlock(6.0, 0.0, 26.0, blockType)
mc.setBlock(7.0, 0.0, 26.0, blockType)
mc.setBlock(8.0, 0.0, 26.0, blockType)
mc.setBlock(9.0, 0.0, 26.0, blockType)
mc.setBlock(10.0, 0.0, 26.0, blockType)
mc.setBlock(11.0, 0.0, 26.0, blockType)
mc.setBlock(12.0, 0.0, 26.0, blockType)
mc.setBlock(13.0, 0.0, 26.0, blockType)
mc.setBlock(14.0, 0.0, 26.0, blockType)
mc.setBlock(15.0, 0.0, 26.0, blockType)
mc.setBlock(16.0, 0.0, 26.0, blockType)
mc.setBlock(17.0, 0.0, 26.0, blockType)
mc.setBlock(18.0, 0.0, 26.0, blockType)
mc.setBlock(19.0, 0.0, 26.0, blockType)
mc.setBlock(20.0, 0.0, 26.0, blockType)
mc.setBlock(21.0, 0.0, 26.0, blockType)
mc.setBlock(22.0, 0.0, 26.0, blockType)
mc.setBlock(23.0, 0.0, 26.0, blockType)
mc.setBlock(24.0, 0.0, 26.0, blockType)
mc.setBlock(25.0, 0.0, 26.0, blockType)
mc.setBlock(26.0, 0.0, 26.0, blockType)
mc.setBlock(27.0, 0.0, 26.0, blockType)
mc.setBlock(28.0, 0.0, 26.0, blockType)
mc.setBlock(29.0, 0.0, 26.0, blockType)
mc.setBlock(30.0, 0.0, 26.0, blockType)
mc.setBlock(9.0, 0.0, 1.0, blockType)
mc.setBlock(9.0, 0.0, 2.0, blockType)
mc.setBlock(9.0, 0.0, 3.0, blockType)
mc.setBlock(9.0, 0.0, 4.0, blockType)
mc.setBlock(9.0, 0.0, 5.0, blockType)
mc.setBlock(9.0, 0.0, 6.0, blockType)
mc.setBlock(9.0, 0.0, 7.0, blockType)
mc.setBlock(9.0, 0.0, 8.0, blockType)
mc.setBlock(9.0, 0.0, 9.0, blockType)
mc.setBlock(10.0, 0.0, 10.0, blockType)
mc.setBlock(11.0, 0.0, 10.0, blockType)
mc.setBlock(12.0, 0.0, 10.0, blockType)
mc.setBlock(13.0, 0.0, 10.0, blockType)
mc.setBlock(14.0, 0.0, 10.0, blockType)
mc.setBlock(15.0, 0.0, 10.0, blockType)
mc.setBlock(16.0, 0.0, 10.0, blockType)
mc.setBlock(17.0, 0.0, 10.0, blockType)
mc.setBlock(18.0, 0.0, 10.0, blockType)
mc.setBlock(19.0, 0.0, 10.0, blockType)
mc.setBlock(20.0, 0.0, 10.0, blockType)
mc.setBlock(21.0, 0.0, 10.0, blockType)
mc.setBlock(22.0, 0.0, 10.0, blockType)
mc.setBlock(9.0, 0.0, 10, blockType)
mc.setBlock(22.0, 0.0, 9.0, blockType)
mc.setBlock(22.0, 0.0, 8.0, blockType)
mc.setBlock(22.0, 0.0, 7.0, blockType)
mc.setBlock(22.0, 0.0, 6.0, blockType)
mc.setBlock(22.0, 0.0, 5.0, blockType)
mc.setBlock(22.0, 0.0, 4.0, blockType)
mc.setBlock(22.0, 0.0, 3.0, blockType)
mc.setBlock(22.0, 0.0, 2.0, blockType)
mc.setBlock(22.0, 0.0, 1.0, blockType)
mc.setBlock(22.0, 0.0, 51, blockType)
mc.setBlock(22.0, 0.0, 50, blockType)
mc.setBlock(22.0, 0.0, 49, blockType)
mc.setBlock(22.0, 0.0, 48, blockType)
mc.setBlock(22.0, 0.0, 47, blockType)
mc.setBlock(22.0, 0.0, 46, blockType)
mc.setBlock(22.0, 0.0, 45, blockType)
mc.setBlock(22.0, 0.0, 44, blockType)
mc.setBlock(22.0, 0.0, 43, blockType)
mc.setBlock(22.0, 0.0, 42, blockType)
mc.setBlock(21.0, 0.0, 42, blockType)
mc.setBlock(20.0, 0.0, 42, blockType)
mc.setBlock(19.0, 0.0, 42, blockType)
mc.setBlock(18.0, 0.0, 42, blockType)
mc.setBlock(17.0, 0.0, 42, blockType)
mc.setBlock(16.0, 0.0, 42, blockType)
mc.setBlock(15.0, 0.0, 42, blockType)
mc.setBlock(14.0, 0.0, 42, blockType)
mc.setBlock(13.0, 0.0, 42, blockType)
mc.setBlock(12.0, 0.0, 42, blockType)
mc.setBlock(11.0, 0.0, 42, blockType)
mc.setBlock(10.0, 0.0, 42, blockType)
mc.setBlock(9.0, 0.0, 42, blockType)
mc.setBlock(9.0, 0.0, 43, blockType)
mc.setBlock(9.0, 0.0, 44, blockType)
mc.setBlock(9.0, 0.0, 45, blockType)
mc.setBlock(9.0, 0.0, 46, blockType)
mc.setBlock(9.0, 0.0, 47, blockType)
mc.setBlock(9.0, 0.0, 48, blockType)
mc.setBlock(9.0, 0.0, 49, blockType)
mc.setBlock(9.0, 0.0, 50, blockType)
mc.setBlock(9.0, 0.0, 51, blockType)

