from mcpi.minecraft import Minecraft
mc = Minecraft.create()

try:
    blockType = int(input("Enter a block type: "))
    mc.setBlock(x, y, z, blockType)
except:
    mc.postToChat("Please enter a number next time.")
    
