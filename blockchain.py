import hashlib as h
'''
I'm going to create a simple blockchain in python and i'm going
to name this as Quaser . The blockchain quaser performs some simple transactions and it will be hashed using SHA256
'''
class Quaser:
     def __init__(self,previousblock,transaction):
         self.previousblock = previousblock
         self.transaction = transaction

         self.blockdata = "\n".join(transaction)+"\n" +previousblock
         self.hashblock =h.sha256(self.blockdata.encode()).hexdigest()      

transaction1 = "Sanjay sends 10 Quaser to Elon Musk"
transaction2 = "Ratan tata sends 12 Quaser to Sanjay"
transaction3 = "Jeff sends 2 Quaser to Bernard Arnault"

Genisis_block = Quaser("",[transaction1,transaction2])
Next_block = Quaser("",[transaction3])

print(Genisis_block.blockdata)
print(Genisis_block.hashblock)

print(Next_block.blockdata)
print(Next_block.hashblock)