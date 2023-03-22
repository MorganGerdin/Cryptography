import hashlib


class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


# t1 = "Anna sends 2.00 NC to Mike"
# t2 = "Bob sends 4.10 NC to Mike"
# t3 = "Mike sends 3.20 NC to Bob"
# t4 = "Daniel sends 0.30 NC to Anna"
# t5 = "Mike sends 1.00 NC to Charlie"
# t6 = "Mike sends 5.40 NC to Daniel"
t1 = input("enter transaction 1:")
t2 = input("enter transaction 2:")
t3 = input("enter transaction 3:")
t4 = input("enter transaction 4:")
t5 = input("enter transaction 5:")
t6 = input("enter transaction 6:")


first_block = NeuralCoinBlock("Initial String", [t1, t2])
print("Data:", first_block.block_data)
print("Hash:", first_block.block_hash)

second_block = NeuralCoinBlock(first_block.block_hash, [t3, t4])
print("Data:", second_block.block_data)
print("Hash:", second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])
print("Data:", third_block.block_data)
print("Hash:", third_block.block_hash)