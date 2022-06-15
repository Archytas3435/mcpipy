from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
print("a")
mc.setPos(1600, 10, -400)
mc.setBlocks(1600, 10, -400, 1620, 12, -390, block.OBSIDIAN)

