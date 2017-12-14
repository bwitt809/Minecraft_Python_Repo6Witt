from mcpi.minecraft import Minecraft
mc = Minecraft.create()
userName = input("Enter your username: " )
message = input("Enter your message: ")
count = 1
while count == 1:
    if userName == "You":
        if message == "Exit" or "exit":
            mc.postToChat("Loop Exited")
            break
        else:
            mc.postToChat(message)
            count += 1
