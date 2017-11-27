from mcpi.minecraft import Minecraft
mc = Minecraft.create()
Y = "Yes"
N = "No"
answer = input("Do you want blocks to be immutable? Y/N ")
if answer == Y:
    mc.setting("world_immutable", True)
    mc.postToChat("World is immutable")
else:
    mc.setting("world_immutable", False)
    mc.postToChat("World is mutable")
