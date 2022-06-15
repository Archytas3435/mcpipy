from mcpi.minecraft import Minecraft
from utils import *
from qiskit import QuantumCircuit, Aer, assemble
from time import sleep

mc = Minecraft.create()

def start():
    change_blocks(mc, start_x-10, start_y-10, start_z-10, end_x+10, end_y+10, end_z+10, air_block)
    change_blocks(mc, start_x, start_y, start_z, start_x, end_y, end_z, border_block)
    change_blocks(mc, start_x, start_y, start_z, end_x, start_y, end_z, border_block)
    change_blocks(mc, start_x, start_y, start_z, end_x, end_y, start_z, border_block)
    change_blocks(mc, end_x, start_y, start_z, end_x, end_y, end_z, border_block)
    change_blocks(mc, start_x, start_y, end_z, end_x, end_y, end_z, border_block)
    change_blocks(mc, end_x, start_y, start_z, end_x, end_y, end_z, border_block)
    for i in range(0, end_z-start_z, 2):
        change_blocks(mc, start_x, start_y, start_z+i, end_x, start_y, start_z+i, stripe_block)
    teleport(mc, (start_x+end_x)//2, (start_y+end_y)//2, (start_z+end_z)//2)

start()