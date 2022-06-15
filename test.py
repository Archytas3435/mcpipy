from mcpi.minecraft import Minecraft
import mcpi

mc = Minecraft.create()

for x in range(1602, 1611):
    for y in range(4, 6):
        for z in range(-348, -339):
            print(mc.setBlock(x, y, z, mcpi.block.AIR))
