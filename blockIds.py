from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    """ Returns value of the melon block """
    return 103
def water():
    """ Returns value of the water """
    return 8
def wool():
    """ Returns value of the wool block """
    return 35, 3
def lava():
    """ Returns value of the lava """
    return 10
def tnt():
    """ Returns value of the tnt block """
    return 46
def flower():
    """ Returns value of the flower block """
    return 38
def diamond():
    """Returns value of the diamond block """
    return 57
block = wool()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)
