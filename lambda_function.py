# Qubits must be numbered from 1-101 with 0 indicating an empty location, 1 indicating 0%, 2 indicating 1%, ...
# All other components must be >= 102

from qiskit import QuantumCircuit, Aer, assemble
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt
from datetime import datetime
import os
import json
import matplotlib
matplotlib.use("Agg")

def upload_file(file_name):
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECERT_KEY)
    response = s3_client.upload_file(file_name, BUCKET, file_name)
    return response

def lambda_handler(event, context):

    error = ""

    try:
        current_state = np.array(json.loads(event)["current_state"]) # only quantum portion
        num_quantum_registers = current_state.shape[0]
        num_classical_registers = 1 # for now
        qc = QuantumCircuit(num_quantum_registers, num_classical_registers)
        
        # TODO: add all gates in https://qiskit.org/documentation/apidoc/circuit_library.html
        single_register_gate_codes = {
            102: qc.h,
            103: qc.x,
            104: qc.y,
            105: qc.z,
            106: qc.id,
            107: qc.s,
            108: qc.sdg,
            109: qc.t,
            110: qc.tdg,
        }
        # ids for start components given; id for end component := id for respective start component + 1
        double_register_gate_codes = {
            200: qc.ch,
            202: qc.cx,
            204: qc.cy,
            206: qc.cz,
        }
        measure_gate_id = 1000

        for i in range(len(current_state)):
            if np.where(current_state[i] >= 102)[0][0] < np.where(1 <= current_state[i] <= 101)[0][0]:
                raise Exception("Qubit not first element in row")
            if np.where(1 <= current_state[i] <= 101)[0].shape[0] > 1:
                raise Exception("Multiple qubits in register")
            x = current_state[i][np.where(1 <= current_state[i] <= 101)[0][0]]
            qc.initialize([sqrt(1-(x-1)/100), sqrt((x-1)/100)], i)

        for step in range(current_state.shape[1]):
            for row in range(current_state.shape[0]):
                element = current_state[row][step]
                if element in single_register_gate_codes.keys():
                    single_register_gate_codes[element](row)
                elif element in double_register_gate_codes.keys():
                    column = current_state[:, step]
                    if (element + 1) not in column:
                        raise Exception("End not found for multi-register gate")
                    else:
                        double_register_gate_codes[element](row, column.where(element+1)[0][0])
                elif element == measure_gate_id:
                    qc.measure(row, 0) # 0 should change when more classical registers added

        qobj = assemble(qc)
        sim = Aer.get_backend("aer_simulator")
        counts = sim.run(qobj).result().get_counts()

        time = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        qc.draw("mpl").savefig(f"/tmp/{time}.png")
        upload_file(f"/tmp/{time}.png")
        url = f"https://quantum-circuit-images.s3.amazonaws.com/{time}.png"
        os.remove(f"/tmp/{time}.png")
        status_code = 200

    except Exception as e:
        error = e
        status_code = 400
        counts = "Error"
        url = "Error"

    return {
        "statusCode": status_code,
        "outputs": counts,
        "image_url": url,
        "error": error
    }

