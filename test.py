from mcpi.minecraft import Minecraft

mc = Minecraft.create()

print(mc.events.pollBlockHits())
