from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
print("a")
mc.setPos(1600, 10, -400)
mc.setBlocks(1600, 10, -400, 1700, 20, -300, block.WOOD)

