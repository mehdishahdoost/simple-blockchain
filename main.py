
from Block import Block

genesis_block = Block("Chancellor on the brick", ["satoshi sent 5 btc to Hal Finney"])
second_block = Block(genesis_block.block_hash, ["mehdi sent 1 btc to ali"])
third_block = Block(second_block.block_hash, ["ali sent 5 btc to mehdi"])

print(genesis_block.block_hash)
print(second_block.block_hash)
print(third_block.block_hash)
