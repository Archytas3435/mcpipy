from qiskit import QuantumCircuit, Aer, assemble
from parse import parse
from utils import *
import numpy as np

current_state = parse()

qc = QuantumCircuit((current_state==qubit_0_block.id).sum()+(current_state==qubit_25_block.id).sum()+(current_state==qubit_50_block.id).sum()+(current_state==qubit_75_block.id).sum()+(current_state==qubit_100_block.id).sum())

