from mcpi.minecraft import minecraft
from mcpi.minecraft import Minecraft

mc = minecraft.Minecraft.create()
mc = Minecraft.create()
print("a")
for x in range(1602, 1611):
    for y in range(-5, 5):
        for z in range(-348, -339):
            mc.setBlock(x, y, z, 17)
