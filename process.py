from qiskit import QuantumCircuit, Aer, assemble
from parse import parse
from utils import *
import numpy as np
from matplotlib import pyplot as plt

def process():
    current_state = parse()

    qc = QuantumCircuit((current_state==qubit_0_block.id).sum()+(current_state==qubit_25_block.id).sum()+(current_state==qubit_50_block.id).sum()+(current_state==qubit_75_block.id).sum()+(current_state==qubit_100_block.id).sum(), 1)

    for row in current_state:
        for qubit in [qubit_0_block.id, qubit_25_block.id, qubit_50_block.id, qubit_75_block.id, qubit_100_block.id]:
            if qubit in row:
                row = list(row)
                if sum(row[:row.index(qubit)]) > 0:
                    print("Qubit not first element in row")
                    return None

    for step in range(len(current_state[0])):
        for row in range(len(current_state)):
            element = current_state[row][step]
            if element == hadamard_block.id:
                try:
                    qc.h(row)
                except:
                    print("You must not skip rows when inserting qubits")
            elif element == not_block.id:
                try:
                    qc.x(row)
                except:
                    print("You must not skip rows when inserting qubits")
            elif element == cnot_start_block.id:
                a = False
                for row2 in range(len(current_state)):
                    if currentstate[row2][step] == cnot_end_block.id:
                        qc.cnot(row, row2)
                        a = True
                        break
                if a == False:
                    print("No output for cx at appropriate timestep")
            elif element == measure_block.id:
                qc.measure(row, 0)

    qobj = assemble(qc)
    sim = Aer.get_backend("aer_simulator")
    counts = sim.run(qobj).result().get_counts()

    print(counts)
    # fig = qc.draw("mpl")
                
