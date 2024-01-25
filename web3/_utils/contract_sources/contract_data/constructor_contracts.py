"""
Generated by `compile_contracts.py` script.
Compiled with Solidity v0.8.24.
"""

# source: web3/_utils/contract_sources/ConstructorContracts.sol:SimpleConstructorContract  # noqa: E501
SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE = "0x6080604052348015600e575f80fd5b50603e80601a5f395ff3fe60806040525f80fdfea26469706673582212200a1d40c9e75d7b341da1c508f56a232fa2bbbe6a82a50556221ba5139df747fe64736f6c63430008180033"  # noqa: E501
SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME = "0x60806040525f80fdfea26469706673582212200a1d40c9e75d7b341da1c508f56a232fa2bbbe6a82a50556221ba5139df747fe64736f6c63430008180033"  # noqa: E501
SIMPLE_CONSTRUCTOR_CONTRACT_ABI = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"}
]
SIMPLE_CONSTRUCTOR_CONTRACT_DATA = {
    "bytecode": SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE,
    "bytecode_runtime": SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME,
    "abi": SIMPLE_CONSTRUCTOR_CONTRACT_ABI,
}


# source: web3/_utils/contract_sources/ConstructorContracts.sol:ConstructorWithArgumentsContract  # noqa: E501
CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_BYTECODE = "0x608060405234801561000f575f80fd5b506040516101fd3803806101fd833981810160405281019061003191906100af565b815f819055508060018190555050506100ed565b5f80fd5b5f819050919050565b61005b81610049565b8114610065575f80fd5b50565b5f8151905061007681610052565b92915050565b5f819050919050565b61008e8161007c565b8114610098575f80fd5b50565b5f815190506100a981610085565b92915050565b5f80604083850312156100c5576100c4610045565b5b5f6100d285828601610068565b92505060206100e38582860161009b565b9150509250929050565b610103806100fa5f395ff3fe6080604052348015600e575f80fd5b50600436106030575f3560e01c806388ec1346146034578063d4c46c7614604e575b5f80fd5b603a6068565b604051604591906089565b60405180910390f35b6054606d565b604051605f919060b6565b60405180910390f35b5f5481565b60015481565b5f819050919050565b6083816073565b82525050565b5f602082019050609a5f830184607c565b92915050565b5f819050919050565b60b08160a0565b82525050565b5f60208201905060c75f83018460a9565b9291505056fea2646970667358221220e8a44f5524ca2769ffd3a6148a42379a1537ac427f92ce61e9be9f2a9216b45964736f6c63430008180033"  # noqa: E501
CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME = "0x6080604052348015600e575f80fd5b50600436106030575f3560e01c806388ec1346146034578063d4c46c7614604e575b5f80fd5b603a6068565b604051604591906089565b60405180910390f35b6054606d565b604051605f919060b6565b60405180910390f35b5f5481565b60015481565b5f819050919050565b6083816073565b82525050565b5f602082019050609a5f830184607c565b92915050565b5f819050919050565b60b08160a0565b82525050565b5f60208201905060c75f83018460a9565b9291505056fea2646970667358221220e8a44f5524ca2769ffd3a6148a42379a1537ac427f92ce61e9be9f2a9216b45964736f6c63430008180033"  # noqa: E501
CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "a", "type": "uint256"},
            {"internalType": "bytes32", "name": "b", "type": "bytes32"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [],
        "name": "data_a",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "data_b",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
]
CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_DATA = {
    "bytecode": CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_BYTECODE,
    "bytecode_runtime": CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME,
    "abi": CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_ABI,
}


# source: web3/_utils/contract_sources/ConstructorContracts.sol:ConstructorWithAddressArgumentContract  # noqa: E501
CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_BYTECODE = "0x608060405234801561000f575f80fd5b506040516101fa3803806101fa833981810160405281019061003191906100d4565b805f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506100ff565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100a38261007a565b9050919050565b6100b381610099565b81146100bd575f80fd5b50565b5f815190506100ce816100aa565b92915050565b5f602082840312156100e9576100e8610076565b5b5f6100f6848285016100c0565b91505092915050565b60ef8061010b5f395ff3fe6080604052348015600e575f80fd5b50600436106026575f3560e01c806334664e3a14602a575b5f80fd5b60306044565b604051603b919060a2565b60405180910390f35b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f608e826067565b9050919050565b609c816086565b82525050565b5f60208201905060b35f8301846095565b9291505056fea26469706673582212200e7170ae8ca52a832bd7b98dc25509df48ea83cce1e300a4b8fd4a7c1a6edfee64736f6c63430008180033"  # noqa: E501
CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME = "0x6080604052348015600e575f80fd5b50600436106026575f3560e01c806334664e3a14602a575b5f80fd5b60306044565b604051603b919060a2565b60405180910390f35b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f608e826067565b9050919050565b609c816086565b82525050565b5f60208201905060b35f8301846095565b9291505056fea26469706673582212200e7170ae8ca52a832bd7b98dc25509df48ea83cce1e300a4b8fd4a7c1a6edfee64736f6c63430008180033"  # noqa: E501
CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "_testAddr", "type": "address"}],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [],
        "name": "testAddr",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
]
CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_DATA = {
    "bytecode": CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_BYTECODE,
    "bytecode_runtime": CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME,
    "abi": CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_ABI,
}
