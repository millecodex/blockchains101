[↰ back](../../..)

# Lecture 06: Ethereum
## Contents
- [Lecture 06: Ethereum](#lecture-06-ethereum)
  - [Contents](#contents)
- [Motivation](#motivation)
    - [What was the problem that Vitalik Buterin was looking to solve?](#what-was-the-problem-that-vitalik-buterin-was-looking-to-solve)
  - [Initial Coin Offering](#initial-coin-offering)
    - [ICO Boom Times](#ico-boom-times)
    - [Token Standards](#token-standards)
  - [Smart Contracts](#smart-contracts)
    - [Oracles](#oracles)
    - [Gas](#gas)
- [Ethereum Architecture](#ethereum-architecture)
  - [Consensus: From PoW to PoS](#consensus-from-pow-to-pos)
  - [Beacon Chain](#beacon-chain)
  - [Ethereum Virtual Machine](#ethereum-virtual-machine)
    - [VMs](#vms)
    - [World State](#world-state)
  - [The Journey of a Smart Contract](#the-journey-of-a-smart-contract)
  - [Applications](#applications)
    - [So what are people doing with this decentralised state machine?](#so-what-are-people-doing-with-this-decentralised-state-machine)
- [Characteristics and Quirks](#characteristics-and-quirks)
- [What did we miss?](#what-did-we-miss)
- [Further Reading - the very short list](#further-reading---the-very-short-list)
  - [Supplementary Resources](#supplementary-resources)
- [Exercises](#exercises)
- [Video Lecture](#video-lecture)

# Motivation
### What was the problem that Vitalik Buterin was looking to solve?
Bitcoin provided a solution to the double-spend problem of creating digital cash by using proof-of-work mining to both maintain the state of the ledger and allow open participation in the network based on computing power. By assigning value to these digitally-scarce coins the ledger can be used as a monetary system. This works great for money but comes up short when using Bitcoin's scripting language to make simple extensions such as a decentralized exchange -- how to determine the NZD/BTC rate? or how to do some arbitrary calculation, e.g. what is the probability that your game character encounters a villain?

In late 2013, While writing for *Bitcoin Weekly* and co-founding [*Bitcoin Magazine*](https://bitcoinmagazine.com/),  a nineteen-year-old Russian-Canadian computer science dropout, Vitalik saw the limitations in Bitcoin as an opportunity to create a new blockchain from scratch that can allow developers to build general applications. The first feature to include in this new blockchain was *Turing-completeness*. Turing-complete refers to a class of computers (programming languages) that can perform arbitrary computation. Named after computer scientist Alan Turing[^Turing], a more practical way of thinking of Turing-completeness is that the language has loops; structures that allow for (potentially) infinite computation, or that recursive functions can be coded. HTML is not Turing-complete as it cannot calculate digits of π, whereas most programming languages are. Bitcoin's scripting language, called *Script*, is not Turing-complete, and intentionally limits the more exotic opcodes.

[^Turing]: The same namesake as the Turing test in which an artificial intelligence can convince a human they are human. Or, in other words, the human cannot tell if the terminal is answering on behalf of a human or AI.

The second feature was to use an account-based system. The benefit of this style is that each account (address) has a balance *and* the option of some code and storage. (This is in contrast to Bitcoin that uses a UTXO model that only keeps track of coins and not any additional data or code.)

There are two types of accounts in Ethereum, and understanding the difference is fundamental to everything that follows:

- **Externally Owned Accounts (EOAs)** are controlled by a private key — this is what most people think of as a "wallet." An EOA has an address and an ether balance, and it can initiate transactions by signing them with its private key. EOAs have no associated code.
- **Contract Accounts** are controlled by code rather than a key. They are created when a smart contract is deployed to the blockchain. Like an EOA, a contract account has an address and can hold ether — but it also has *code* (the compiled smart contract logic) and *storage* (a persistent key-value store that lives on-chain). A contract cannot initiate a transaction on its own; it can only execute in response to being called.

This distinction explains why a smart contract's address looks identical to a user's wallet address on the surface, but behaves very differently underneath. When you send a transaction to a contract address, the EVM runs the contract's code. When you send it to an EOA address, funds simply transfer.

The whitepaper for *Ethereum* was published online in 2013 and a year later a formal specification was written by Gavin Wood and the project raised funds through their initial coin offering. This was followed by the network launch in 2015.

Summarizing Ethereum from the whitepaper[^Buterin2014]:
> [Ethereum] is essentially the ultimate abstract foundational layer: a blockchain with a built-in Turing-complete programming language, allowing anyone to write smart contracts and decentralized applications where they can create their own arbitrary rules for ownership, transaction formats, and state transition functions.

[^Buterin2014]: Buterin, V. (2014). Ethereum: A next-generation smart contract and decentralized application platform.

## Initial Coin Offering
In order to fund their new proposed blockchain network, the founders embarked on a unique [fundraising scheme](https://blog.ethereum.org/2014/07/22/launching-the-ether-sale/) that laid down the template for future crowdfunding sales. An initial coin offering (ICO) seeks to bootstrap user adoption and funding by combining the style of an initial public offering (IPO) with a crowd fund model. A marked difference from the IPO model is that the token sale was open to anyone without geographic or regulatory restriction. All users had to do to participate was deposit bitcoin and receive *ether* tokens that represent their stake in the new network. The token sale was successful resulting in more than 50 million ether (the native currency of ethereum) being sold. Investors were aware of the token distribution from the beginning which included 9.9% of the tokens reserved for the founders (to fund development, salaries, bug bounties, etc.) and another 9.9% for a [foundation](https://ethereum.foundation/) that was set up to guide the long term mission of the network. These tokens didn't have to be purchased in a traditional sense; a practice now known as *pre-mining*.

### ICO Boom Times
The success of Ethereum's ICO and its smart contract capability combined with its open source code made it an ideal model for other founders to fund their projects. A new project could easily copy and modify smart contract code and host their own ICO and issue their own new ERC-20 tokens. (ERC-20 refers to the token standard that most coins that run on Ethereum use.) 2017--2018 was a boom period for ICOs with many projects and tokens launching. Unfortunately many of them had questionable products and practices or were outright scams and because there was no regulation in crypto (as there is for an IPO), there was no recourse for those that invested and lost their money.

### Token Standards

The ERC-20 tokens mentioned during the ICO boom all follow a common interface — a specification that defines how a token contract must behave so that wallets, exchanges, and other contracts can interact with it predictably. But ERC-20 is only one of several token standards and the differences between them matter:

- **ERC-20** tokens are *fungible* — every unit is identical and interchangeable, like banknotes. One USDC is the same as any other USDC. These are the tokens issued in ICOs, used throughout DeFi, and held in cryptocurrency wallets.
- **ERC-721** tokens are *non-fungible* — each token has a unique identifier and is distinguishable from every other token in the same contract. These are **NFTs** (Non-Fungible Tokens). An ERC-721 token represents ownership of something unique: a piece of digital art, a game item, a concert ticket. The blockchain guarantees *who owns token #42*, not the value or quality of what it represents.

The term *fungible* comes from economics: a good is fungible if one unit can be substituted for another without loss. Cash is fungible; a painting is not. Ethereum's token standards are a formalisation of this economic concept in code. The NFT market saw significant growth in 2020–2022, with projects like CryptoPunks and Bored Ape Yacht Club generating billions in trading volume. OpenSea (visible in the dapp table in Applications below) is the largest NFT marketplace on Ethereum.

## Smart Contracts
The term *smart contract* refers to some executable code that lives on the blockchain. This code may be a snippet, small or large, it may be straightforward or complex, it may contain bugs, not compile, it may never even be executed. Ethereum allows for code to be stored on the blockchain in *contracts* which have a callable address that looks just like a user's address. All of these bits of code are generically called smart contracts. Pedants will like to tell you that they are not smart nor are they contractual and they might be right in a traditional sense, however, the term has come to be redefined in a blockchain context.

Earlier we mentioned that Ethereum is turing-complete, and here is where that comes in. A developer can write a program, say to issue crop insurance based on weather data, and store this program in a smart contract on the blockchain. As the blockchain is immutable this code will live there forever, it is also visible and thus can be easily verified or audited. The only limits to the applications that can be deployed on Ethereum come from the creativity & skill of the developer, and the amount of computation that program needs to do. Solidity is the name of the most common high-level language used to write code that compiles to bytecode to be executed on the Ethereum virtual machine. Created by the co-founder of Ethereum, Gavin Wood, Solidity was intended to resemble JavaScript and be recognizable to web developers.

**Example Contract 1**
Here is an example from *Mastering Ethereum* (Antonopoulos, 2019) to create a faucet which will give out ether[^2] to anyone that interacts with it.

```solidity
// Our first contract is a faucet!
contract Faucet {
    // Give out ether to anyone who asks
    function withdraw(uint withdraw_amount) public {
        
        // Limit withdrawal amount
        require(withdraw_amount <= 100000000000000000);
        
        // Send the amount to the address that requested it
        msg.sender.transfer(withdraw_amount);
    }
    // Accept any incoming amount
    function () public payable {}
}
```

> *Note: This example uses Solidity 0.4.x syntax. Modern Solidity (0.8+) requires an explicit `pragma solidity` version statement, uses named fallback functions (`receive()` and `fallback()` instead of the anonymous `function()`), and adds automatic overflow/underflow protection. Code written in 0.4.x will not compile with a 0.8 compiler without modification.*

[^2]: Ether (ETH) is the currency used on the Ethereum platform. Gas is the name for the fees that the network will charge to execute contracts, this is priced in very small amounts of ETH.

**Example Contract 2**
A more substantial example is taken from the [solidity documentation](https://solidity.readthedocs.io/en/v0.4.24/introduction-to-smart-contracts.html) and details some functions of a simple cryptocurrency:

```solidity
pragma solidity ^0.4.21;

contract Coin {
    // The keyword "public" makes those variables
    // readable from outside.
    address public minter;
    mapping (address => uint) public balances;

    // Events allow light clients to react on
    // changes efficiently.
    event Sent(address from, address to, uint amount);

    // This is the constructor whose code is
    // run only when the contract is created.
    function Coin() public {
        minter = msg.sender;
    }

    function mint(address receiver, uint amount) public {
        if (msg.sender != minter) return;
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        if (balances[msg.sender] < amount) return;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
}
```

> *Note: In Solidity 0.5.0 and later, constructors must be written as `constructor()` rather than using the contract name. The `function Coin() public { }` pattern was deprecated because a typo in the contract name would silently create a callable function rather than a one-time initialiser — a subtle but dangerous bug.*

**Example Contract 3**
The Ethereum DAO hack took place in 2016 when a hacker drained US $50 million from a [fundraising account](https://www.gemini.com/cryptopedia/the-dao-hack-makerdao#section-the-dao-hack-remedy-forks-ethereum). Here is some logic from the attack:

```solidity
contract donateDAO {
    mapping (address => uint256) public credit;

    // add funds to the contract
    function donate(address to) payable {
        credit[msg.sender] += msg.value;
    }

    // show ether credited to address
    function assignedCredit(address) returns (uint) {
        return credit[msg.sender];
    }

    // withdrawal ether from contract
    function withdraw(uint amount) {
        if (credit[msg.sender] >= amount) {
            msg.sender.call.value(amount)();
            credit[msg.sender] -= amount;
        }
    }
}
```

> *Note: The `call.value()` pattern used in this exploit was superseded by the Checks-Effects-Interactions pattern now enforced by style guides and auditors: always update state **before** transferring funds. Modern tooling (Slither, OpenZeppelin's `ReentrancyGuard`) would flag this code as vulnerable at compile time.*

The problem is in the `withdraw()` function. In line 17, `call.value()` sends funds, in this case to the sender, before updating the balance. Here, the hacker can request their funds back, and then a fallback function triggers a recursive call that keeps sending funds back without updating the balance[^Humiston2018].

[^Humiston2018]: Humiston, I. (2018). Attacks and Incidents. In *Ethereum Smart Contract Development* (pp. 81-94). Apress. <!-- TODO: PDF not downloadable — Apress book chapter behind paywall -->

### Oracles
There is a limitation to the EVM design: smart contracts cannot fetch data from outside the blockchain. The network is deterministic — every node must reach the same result when re-executing the same transaction — so any external call that might return different answers to different nodes is forbidden. This means a contract cannot look up a stock price, check the weather, or call a REST API. The solution is **oracles** — services that bring off-chain data on-chain by posting it in a transaction, where it can be read by smart contracts. Oracles are covered in the [lecture on Decentralisation and DeFi](08-decentral.md#oracles-bridging-on-chain-and-off-chain-data).

### Gas
Computation occurs in the EVM (Ethereum virtual machine) and because it's a blockchain, all the nodes need to have a copy of the data and verify any updates. This includes running *all* smart contracts and doing *any* calculation. A scenario could arise, either accidentally or maliciously, to halt the network by deploying a contract with an infinite loop:
```solidity
contract InfiniteLoop { 
  function runOutOfGas() public {
    while (true) { 
	jeff++
} } }
 ```
The simple code above continually updates the counter because the stop condition of `false` never occurs. To avoid this scenario all computation in the EVM needs gas. As a contract is executed gas is consumed and if the contract runs out of the gas then the update fails. All gas is paid in ether (`ETH`) and goes to the nodes that perform the calculations. A follow up question is: "What if I am wealthy and have enough gas to spam the network in this manner?" To prevent this there is a gas-limit on all transactions that is calculated based on how busy the network is. The  *London* upgrade to Ethereum changed the way that gas is distributed. Previously the miner would be compensated by receiving the entire gas fee in the transaction. Now, part of this fee is *burned*, and the validator gets the remainder. Burning some ETH offsets the overall issuance of the token.

> <img width="1200" alt="ultrasound money showing ETH issuance since the merge" src="https://github.com/user-attachments/assets/301de07f-d490-4708-b898-778a76913d3d" />\
> Since the merge the issuance of Ether has stayed relatively flat due to the burning of fees. (BTC inflated due to the decreasing block reward.) Source: [Ultrasound.money](https://ultrasound.money/?timeFrame=since_merge)

Gas fees are important for funding the network validators, preventing spam, but also for scaling. As more users need the blockspace, block fees will adapt to the increase in demand. This has resulted in many Layer-2s that process transactions for a cheaper cost, then batch-post back to the Ethereum base layer. More on this topic in the [lecture on scaling](09-scaling.md). In brief: a **rollup** executes transactions off the main chain, compresses the results, and posts a commitment back to Ethereum.

# Ethereum Architecture
Looking at Ethereum from an individual node point of view there are three main clients that work together to (a) maintain consensus and (b) update the state.
> <img width="800" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/fa95396b-7bad-4e43-982a-770405ab08a7">\
> Architecture of an Ethereum node, i.e. Geth, Parity, showing three main clients: Validator, Consensus (Beacon chain), and Execution (EVM). Modified from: https://eth-docker.net/

## Consensus: From PoW to PoS
On September 15, 2022, the Ethereum network executed "[The Merge](https://ethereum.org/en/roadmap/merge/)" which transferred consensus from the main chain that was operating by proof of work to the beacon chain that was running (in parallel) proof of stake. It was always the ethos of the Ethereum community to transition the network to a fully stake-based validation mechanism. What was unknown at the time was how hard it would be; it took developers ~7 years to do it. 

In a PoS system consensus is handled by validators that maintain skin in the game by contributing a stake in ether and are rewarded in a similar fashion to miners. A validator's rewards are proportional to their stake in the system. The rules of the game dictate the validators must not be able to cheaply spam the network with multiple identities (Sybil resistance), which is enforced by a known list of validators with rewards in proportion to total stake. So multiple entities can join, but you must have >32 ETH to do so.

To enforce honest behaviour, validators who sign conflicting blocks have a portion of their staked ETH permanently destroyed by the protocol. This penalty is called **slashing**[^slashing] (also covered in [Lecture 05 — the nothing-at-stake problem](05-proof-of-other.md#proof-of-stake)). It is the economic mechanism that gives PoS its security: just as PoW miners lose real energy expenditure when they behave dishonestly, PoS validators lose real capital. A validator caught double-signing is ejected from the active validator set and loses a portion of their 32 ETH deposit.

[^slashing]: Slashing conditions were first proposed in Buterin's [Slasher post](https://blog.ethereum.org/2014/01/15/slasher-a-punitive-proof-of-stake-algorithm) (2014) and formalised in the Casper FFG paper (Buterin & Griffith, 2017). [PDF](../papers/pdfs/Buterin-Casper-2017.pdf)

One dimension of The Merge that received significant public attention was its environmental impact. Pre-Merge, Ethereum's annual energy consumption was estimated at roughly 78 TWh — comparable to a small country.[^energy] The transition to proof-of-stake reduced this by approximately **99.95%**.[^merge_energy] PoS validators run on ordinary consumer hardware; there are no SHA-256 hashing races or warehouse-scale mining operations. The contrast with Bitcoin is often cited in policy and ESG discussions, though it is worth noting that the narrative is contested on both sides: critics argued Ethereum's energy use was never the problem some claimed, while proponents of the switch emphasise that the reduction should reshape how regulators and institutions think about the two networks. Social consensus around energy and sustainability in blockchain remains a live and sometimes fraught debate.

[^energy]: Cambridge Centre for Alternative Finance, *Cambridge Blockchain Network Sustainability Index*. [https://ccaf.io/cbnsi/ethereum](https://ccaf.io/cbnsi/ethereum)

[^merge_energy]: Ethereum Foundation estimate. See [ethereum.org — Energy Consumption](https://ethereum.org/en/energy-consumption/).

> <img width="800" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/24925a07-ad77-46cc-a6d6-132359547d39">\
> Figure: Ethereum consensus enforces sybil resistance by slashing penalties, and uses committee voting to determing the chain-head.

## Beacon Chain
The beacon chain launched at the end of 2020 to act as the proof of stake consensus chain alongside the proof of work chain. It is now the 'main' Ethereum chain. Forks in Ethereum are resolved through voting. Block ordering is done by collecting attestations on each block as to whether or not it is the 'chain-head'. Block proposers are selected in a BFT-style leader election process, and finality is determined by validator voting on checkpoints. There is 1 check point in each epoch (32 slots). There is 1 block proposer and block per slot. Supermajority, or greater than 2/3 of the votes are required for selecting the chain-head[^LMDGHOST] and the epoch check-point. This means that up to 1/3 can be malicious. Each block takes 12 seconds to be published, and thus each epoch is $12*32=384$ seconds, or 6:24.

[^LMDGHOST]: The name of the fork-choice rule algorithm. The acronym stands for Latest Message Driven Greediest Heaviest Observed SubTree. Read the paper: Buterin et al. (2020). *Combining GHOST and Casper*. [arXiv:2003.03052](https://arxiv.org/abs/2003.03052) | [PDF](../papers/pdfs/Buterin-CombiningGHOSTCasper-2020.pdf)

Once the beacon chain decides on the chain-head and has a block proposer, the node has 12 seconds to execute transactions and advance the state before publishing the updated block. The block is propagated by sending it out through the network gossip protocol. Executing transactions means it will process all the smart contract code, deploy new contracts, and update account balances. These are all handled by the Ethereum Virtual Machine.

## Ethereum Virtual Machine
### VMs
Virtual machines (VMs) in computer science are emulations of a computer system that provide the functionality of a physical computer, operating on the basis of a host system and creating a separate environment known as the guest system. The main purpose of a VM is to enable multiple operating systems to share the same physical hardware resources, promoting flexibility and isolation for applications such as testing and development.

This concept of emulation is shared with the **EVM**, although they serve different purposes. While regular VMs simulate physical hardware, the EVM is a virtual runtime environment designed specifically for executing smart contracts on the Ethereum blockchain. The EVM operates independently of the underlying hardware, ensuring deterministic computation that yields the same result across all network nodes. Each full node runs a copy of the EVM to verify transactions and smart contract executions, playing a crucial role in the decentralisation and security of the Ethereum network.

### World State
When the EVM processes a transaction, it reads from and writes to something called the **world state** — Ethereum's global database of all account information. You can think of it as a giant lookup table: every address on the network maps to its account data (balance, nonce, code, storage). Every block appended to the chain represents a new snapshot of this world state.

Storing this efficiently across thousands of nodes is non-trivial. Ethereum uses a data structure called a **Merkle Patricia Trie** (MPT) to encode the world state.[^mpt] The key property of a Merkle trie is that its root — a single 32-byte hash — *cryptographically summarises the entire state* (recall [Merkle trees from Lecture 02](02-cryptography.md#merkle-trees)). Two nodes with the same state root are guaranteed to have identical world states. This is how the network confirms agreement without transmitting the entire database.

[^mpt]: The Merkle Patricia Trie is a hybrid of a Patricia trie (efficient prefix-compressed key-value store) and Merkle hashing at each internal node. Specified in the Yellow Paper (Wood, 2014), Appendix D. [PDF](../papers/pdfs/Wood-EthereumYellowPaper-2014.pdf). Readable explainer: [ethereum.org — Patricia Merkle Tries](https://ethereum.org/en/developers/docs/data-structures-and-encoding/patricia-merkle-trie/).

> <img width="800" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/9c3de5ff-de3f-44e9-bbb7-6a80abf43e4d">\
> Figure: Ethereum EVM shown in the inner box (execution cycle) determines the next state. Source: https://github.com/4c656554/BlockchainIllustrations/ 

When processing a transaction, the EVM takes the following steps:
1. **State Retrieval**: Before executing the transaction, the EVM retrieves the current state of involved accounts (sender and receiver) from the blockchain's state database.
2. **Gas Cost Estimation**: The EVM estimates the computational cost of the transaction, measured in 'gas,' to ensure it doesn't exceed the gas limit specified by the sender.
3. **Nonce Verification**: The EVM checks the nonce of the transaction (a counter that must match the sending account’s current nonce). If it doesn't match, the transaction is invalid.
4. **Balance Verification**: The EVM checks if the sender's account has sufficient Ether to cover both the value being sent and the gas fees.
5. **Transaction Execution**: If the transaction is to a contract address, the EVM executes the contract’s code. Inputs are provided through the 'data' field of the transaction, and any output is recorded as a 'logs' event. If it's a value transfer, the EVM updates the state of the sender and receiver accounts.
6. **State Update**: After successful execution, the EVM updates the world state database (red, immutable, above). The state of the sender’s account is modified to decrease the balance by the total cost (gas used multiplied by gas price), and the receiver’s state is updated accordingly.

In step 5, the actual execution, if the transaction's target is a contract address, the EVM executes the associated smart contract code. The smart contract code is compiled into EVM bytecode, which is a series of opcodes that the EVM understands. This execution takes place in individual nodes and uses the Ethereum world state for reading and writing data. The stack plays an essential role in EVM's computational model. It's a data structure that follows the Last-In, First-Out (LIFO) principle, and is used to store variables temporarily during the execution of opcodes. Operations like `ADD`, `MUL`, `DIV`, etc., typically pop operands off the stack and push the result back onto it. This stack-based execution model allows for deterministic and atomic operations, which is pivotal in maintaining the integrity and consistency of the blockchain state across nodes.

## The Journey of a Smart Contract
Now that we have some of the background information about the EVM we can appreciate this low-level view of a smart contract.
> ![SmartContractJourney](https://github.com/user-attachments/assets/9fae4d0d-69d2-41c8-bca4-2ae3409a7f52)
> Credit to [0xGojoArc](https://x.com/0xGojoArc)

I'll highlight a few things:

**Initcode vs. runtime bytecode.** When you deploy a contract, the EVM first executes *initcode* — the constructor logic that sets up initial state. Initcode runs once and is then discarded. What gets stored permanently on-chain is the leaner *runtime bytecode*, the code that handles all future calls.

**Separate clients, separate responsibilities.** The diagram makes visible what the node architecture diagram earlier summarised: the *Execution Client* (Geth, Nethermind) and the *Consensus Client* (Prysm, Lighthouse) are distinct pieces of software with distinct responsibilities. The Execution Client runs the EVM and assembles the Block Template; only then does the Consensus Client take over to propose, broadcast, and finalise the block. Execution happens before consensus, the block template including the new state root must exist before validators can vote on it.

**The State Root.** The Block Template assembled by the Execution Client contains three things: the list of transactions, metadata (parent hash, receipts), and the *State Root* — a single hash that cryptographically commits to the entire updated world state (recall the Merkle Patricia Trie). Other validators re-execute every transaction independently and check that they arrive at the same state root. If they do, they attest. If they don't, the block is rejected.

**Atomicity.** If any of the runtime checks fail (invalid opcode, stack overflow, out of gas, permission violation), the transaction *reverts* — the world state is unchanged, no partial writes occur. The user loses their gas but the chain stays consistent.

**The GossipSub layer.** Block propagation broadcast via the *GossipSub* peer-to-peer protocol. GossipSub is a publish-subscribe mesh network that ensures blocks reach all nodes efficiently without a central relay.


## Applications
### So what are people doing with this decentralised state machine?
Decentralised applications, or *dapps* just refer to smart contracts that are executed on a blockchain. When combined with a frontend these dapps can appear just like any other web application with the key difference being that that code and/or user data and token transfer information is stored on the blockchain. 

The most used dApps on Ethereum in April 2026 ranked by Unique Active Wallets (UAW, 30-day):

| Rank | dApp            | Category               | UAW (k/30 days) |
| ---: | :-------------- | :--------------------- | --------------: |
|    1 | Uniswap V2      | Decentralised Exchange |           129.4 |
|    2 | OpenSea         | NFT Marketplace        |           123.9 |
|    3 | MetaMask Swap   | DEX Aggregator         |           103.5 |
|    4 | Uniswap V4      | Decentralised Exchange |            74.6 |
|    5 | Uniswap V3      | Decentralised Exchange |            62.6 |
|    6 | Jumper Exchange | Bridge / DEX           |            58.9 |
|    7 | Banana Gun      | Trading Bot            |            54.9 |
|    8 | 1inch           | DEX Aggregator         |            39.3 |
|    9 | edgex           | Decentralised Exchange |            36.9 |
|   10 | Rango           | Bridge / DEX           |            30.0 |

Now ranking by total value locked (TVL)

| Rank | dApp               | Category         | TVL ($B) |
| ---: | :----------------- | :--------------- | -------: |
|    1 | Aave               | Lending          |     19.6 |
|    2 | Lido               | Liquid Staking   |     19.0 |
|    3 | EigenLayer         | Restaking        |      8.4 |
|    4 | Binance Staked ETH | Liquid Staking   |      7.1 |
|    5 | Sky (Maker)        | Stablecoin/CDP   |      6.7 |
|    6 | Ethena             | Synthetic Dollar |      6.6 |
|    7 | Spark              | Lending          |      5.3 |
|    8 | ether.fi           | Liquid Restaking |      4.9 |
|    9 | Morpho             | Lending          |      3.8 |
|   10 | Tether Gold        | RWA              |      3.3 |

> *Data sourced from [DappRadar](https://dappradar.com/rankings/protocol/ethereum) and [DeFiLlama](https://defillama.com/chain/Ethereum), April 2026. TVL figures reflect Ethereum mainnet deployments. UAW rankings can shift significantly week-to-week; Uniswap, Aave, and OpenSea have been consistently prominent over multiple years.*


# Characteristics and Quirks
* The DAO hack was an important event in Ethereum's history. There was a bug, and a lot of money was lost, but then the *immutable* blockchain was rolled back, the community split, now there still exists Ethereum Classic (ETC) and an ongoing question over the decentralised nature of Ethereum. See Laura Shin's book [The Cryptoptians](https://laurashin.com/book/) for an excellent accounting of the events. This event is the canonical example of a **hard fork** — a non-backward-compatible protocol change where the chain diverges into two incompatible versions. Nodes that accepted the code change continued on Ethereum (ETH); nodes that rejected it on the grounds that *code is law* continued on Ethereum Classic (ETC), diverging from block 1,920,000. The two chains still coexist today. Not all hard forks are contentious — most Ethereum upgrades (London, Shanghai, Dencun) are also technically hard forks but the community adopts them unanimously with no chain split.
* **Difficulty Bomb (Retired):** Also known as the "Ice Age," the difficulty bomb was a mechanism written into Ethereum at launch that made proof-of-work mining exponentially harder over time — a ticking clock to force the community toward proof-of-stake. In practice it was delayed by a series of hard forks (Byzantium 2017, Constantinople 2019, Muir Glacier 2020, Arrow Glacier 2021, Gray Glacier 2022) as PoS development ran years over schedule. Once The Merge retired PoW in September 2022, the bomb was formally removed in the **Paris** upgrade ([EIP-5133](https://eips.ethereum.org/EIPS/eip-5133)).
* Self-Destruct and Resurrection: A quirky feature in Solidity is the selfdestruct function. When a contract self-destructs, it can send its remaining Ether to another address. Interestingly, if someone sends Ether to a self-destructed contract's address, and a new contract is created at the same address, the new contract will have the Ether sent to the "[dEaD](https://etherscan.io/address/0x000000000000000000000000000000000000dEaD)" address.

# What did we miss?
* [MEV](https://ethereum.org/en/developers/docs/mev/) — Maximal Extractable Value; validators and searchers can reorder transactions within a block to extract profit.
* [zkEVM](https://www.alchemy.com/overviews/zkevm) — a ZK-proof-based execution environment compatible with the EVM; enables ZK-Rollups that run Solidity contracts.
* **Other token standards** — beyond ERC-20 and ERC-721, the ecosystem has developed: ERC-1155 (semi-fungible, single contract for multiple token types), ERC-4626 (tokenised vault standard for DeFi yield), ERC-6551 (token-bound accounts, giving NFTs their own wallets), and account abstraction via ERC-4337 (smart contract wallets without a separate EOA).

# Further Reading - the very short list
* [The Whitepaper by Vitalik Buterin](https://ethereum.org/en/whitepaper/)
* [The Yellowpaper by Gavin Wood](https://github.com/ethereum/yellowpaper), & [pdf](https://ethereum.github.io/yellowpaper/paper.pdf)
* [Extensive list of learning resources](https://ethereum.org/en/learn/)
* [EVM Illustrated (slides)](https://github.com/takenobu-hs/ethereum-evm-illustrated)
* [Beacon Chain Explained](https://ethos.dev/beacon-chain)

## Supplementary Resources
* [Introduction to Smart Contracts — ethereum.org](https://ethereum.org/en/developers/docs/smart-contracts/) — Official developer docs introducing smart contracts, their anatomy, and how they interact with the EVM.
* [Ethereum Virtual Machine (EVM) — ethereum.org](https://ethereum.org/en/developers/docs/evm/) — Technical but accessible guide to how the EVM executes bytecode, manages state, and uses gas.
* [Mastering Ethereum — Antonopoulos & Wood (GitHub)](https://github.com/ethereumbook/ethereumbook) — Open-source book; free to read online. Chapters 1–3 and 7 are especially relevant to this lecture.
* [Gas and Fees — ethereum.org](https://ethereum.org/en/developers/docs/gas/) — Clear explanation of gas mechanics, EIP-1559, base fees, and tips.

# Exercises
1. Turing-Completeness of Ethereum. Discuss the implications of Ethereum being Turing-complete in contrast to Bitcoin. What opportunities and challenges does Turing-completeness introduce in the context of blockchain applications? Consider aspects such as computational complexity, attack vectors, and flexibility in contract development.
2. Initial Coin Offering (ICO) Analysis. Critically examine the ICO model used for Ethereum and compare it with the traditional IPO model. Address questions like: What are the ethical and regulatory considerations? How does the ICO model promote or hinder decentralisation? What are the economic risks associated with the ICO model for investors and the network?
3. The DAO Hack Look at the Solidity code snippet for donateDAO. Identify and analyse the vulnerabilities present in this smart contract that led to the DAO hack. Propose alternative code or solutions to mitigate such vulnerabilities. It might be helpful to refer to security practices in smart contract development.

# Video Lecture
* Here's this lecture recorded live August 28, 2023 on [YouTube](https://www.youtube.com/watch?v=bIWsS8o9VAE),
* and an update on August 19, 2025 on [X/Twitter](https://x.com/Japple/status/1963519909935399029).
