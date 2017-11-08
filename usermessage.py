from mcpi.minecraft import Minecraft
mc = Minecraft.create()

message = input("Anything: ")
mc.postToChat(message)
