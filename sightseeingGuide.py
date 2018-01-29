from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'misty mountain' :(-5.2, 54.0, 18.8),
          'Brandons happy place':(-66, 66, -66),
          'The pit':(36.3, 29.0, -12.3),
          'On the Edge of glory':(-32.5, 47.0, -127.7),
          'Great Wall of China':(51.4, 14.0, 75.8),
          'Landons Tower of Erectilness':(111.5, 25.0, 46.7)}
choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        
        mc.player.setTilePos(x, y, z)
          
