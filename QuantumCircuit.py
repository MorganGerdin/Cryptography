from qiskit import QuantumCircuit

# set up Quantum Circuit
circ = QuantumCircuit(4)
print(circ)

# add hadamard gates
circ.h(0)
circ.h(1)
circ.h(2)
print(circ)

# add cnot gates
circ.cx(0, 1)
circ.cx(0, 2)
circ.cx(1, 3)
print(circ)
