from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
print("a")
mc.player.setPos(1600, 8, -400)
mc.setBlocks(1600, 10, -400, block.OBSIDIAN)

