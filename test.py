from mcpi.minecraft import Minecraft

mc = Minecraft.create()

for x in range(1602, 1611):
    for y in range(4, 8):
        for z in range(-348, -339):
            print(mc.getBlock(x, y, z))
