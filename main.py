# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:09:46 2020

@author: ahmet
"""

#bloklar ve blokların içinde transactions
#blocklar hashing ile birbirine bağlantılı
    #digital hash: transaction + önceki bloğun hash

from Block import Block

blockchain = []; #bos array

genesis_block = Block("patates.....", ["acannnnnnn satoshi'ye 10 btc gonderdi","haha 500 eth to acan","vitalik acan'a 100 eth gonderdi"])

second_block = Block(genesis_block.block_hash, ["Acann, Vitalik'e 5 ETH gonderdi","haaaaha"])

third_block = Block(second_block.block_hash, ["A ---> C 5 eth", "V-> S 10 btc","hhhhhhhehe"])


print("Genesis block'un blockhash'i")
print(genesis_block.block_hash)

print("Ikinci block'un blockhash'i")
print(second_block.block_hash)

print("Ucuncu block'un blockhash'i")
print(third_block.block_hash)