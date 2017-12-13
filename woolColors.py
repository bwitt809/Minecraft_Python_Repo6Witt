from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getWoolState(color):
    """ Takes a color as a string and returns the wool block state for
    that color """
    if color == "pink":
        blockState = 6
    elif color == "white":
        color = 0
    elif color == "orange":
        color = 1
    elif color == "magenta":
        color = 2
    elif color == "light blue":
        color = 3
    elif color == "yellow":
        color = 4
    elif color == "lime":
        color = 5
    elif color == "gray":
        color = 7
    elif color == "light gray":
        color = 8
    elif color == "cyan":
        color = 9
    elif color == "purple":
        color = 10
    elif color == "blue":
        color = 11
    elif color == "brown":
        color = 12
    elif color == "green":
        color = 13
    elif color == "red":
        color = 14
    elif color == "black":
        color = 15
    return color
        
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
