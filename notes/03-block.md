[↰ back](../../..)
# Lecture 3: Anatomy of a Block and Transaction Flow
## Contents
1. [Introduction](#introduction)
2. [The Lifecycle of a Bitcoin Transaction](#the-lifecycle-of-a-bitcoin-transaction)
3. [The Mempool: A Transaction Waiting Room](#the-mempool-a-transaction-waiting-room)
4. [Data Structure: The Anatomy of a Block](#data-structure-the-anatomy-of-a-block)
5. [Connecting the Blocks: The Chain of Trust](#connecting-the-blocks-the-chain-of-trust)
7. [Summary](#summary)
8. [What did we miss?](#what-did-we-miss)
9. [Exercises](#exercises)
10. [Readings](#readings)

## Introduction
To recap: a useful analogy for the blockchain is a physical ledger (book) for recording customer transactions. The entire blockchain is the book itself, representing the complete history of all transactions. Each block is a new page added to this book. The transactions are the individual lines written on each page, recording the transfer of value. A crucial property of this book is that once a page is filled, validated, and added, it is sealed. It cannot be erased or altered without invalidating all subsequent entries.


## The Lifecycle of a Bitcoin Transaction
### The UTXO Model vs. The Account Model
Before we can build a transaction, we must understand what we are spending. Most of us are familiar with the account model, used in traditional banking (and by many other cryptocurrencies like Ethereum). In this model, the system tracks a balance. If your account holds $100 and you spend $10, the system simply debits your account, and your new balance is $90. The ledger tracks the state of each account's balance.

> ![image](https://github.com/user-attachments/assets/)\
> Account balance model in Ethereum. The native token (ETH) is maintained separate from other token balances. Source: [Etherscan](https://etherscan.io/address/0xfb493d4b693bf7e982153ff7a0d7a955d2f454a5#asset-tokens)

Bitcoin takes a different, less intuitive, but powerful approach: the **Unspent Transaction Output (UTXO)** model. Bitcoin does not track account balances. Instead, the blockchain tracks individual, discrete chunks of bitcoin called UTXOs. Think of your Bitcoin wallet not as a bank account with a single balance, but as a physical wallet containing various bills and coins. You don't have a "balance" of $55; you might have two $20 bills, one $10 bill, and one $5 bill. These individual bills are your UTXOs.   

A user's wallet *balance* is a derived concept. The wallet software scans the blockchain to find all the UTXOs that the user's private keys can unlock (spend) and sums them up to display a total balance.   

UTXOs are indivisible. If you want to pay for a $3 coffee with a $5 bill, you must hand over the entire $5 bill. You cannot tear off a piece of it. The cashier then gives you $2 back in change. Bitcoin transactions work the same way. If you have a 0.05 BTC UTXO and want to send 0.01 BTC, your transaction must consume the entire 0.05 BTC UTXO as an input. It will then create two new outputs: one 0.01 BTC UTXO for the recipient, and one 0.04 BTC UTXO as "change" that is sent back to a new address controlled by your own wallet. This design choice has downstream implications. It makes transaction verification much simpler in a decentralized environment. To validate a transaction, a node doesn't need to know an account's entire history; it only needs to check one thing: is the UTXO being spent currently in the set of all unspent transaction outputs? This stateless verification is more efficient and scalable than reconciling a global state of account balances.   

### Transaction Creation: Assembling Inputs and Outputs
The lifecycle begins when a user decides to make a payment using their wallet application.

> ![image](https://github.com/user-attachments/assets/2cb01b19-93dc-425f-8b55-cc24bd474266)\
> UTXO design. Alex wants to send 5.1 Bitcoin to Julia. He needs to combine two UTXOs from his wallet, #1 and #2. This creates a new input in Julia's wallet for the required amount **and a new input** in Alex's wallet for the change. Source: [River](https://river.com/learn/bitcoins-utxo-model/)

1. Inputs (Alex's bills)

The wallet software scans the blockchain for available UTXOs that it can spend. It then selects one or more of these UTXOs to act as inputs for the new transaction. The sum of these inputs must be greater than or equal to the desired payment amount. By being designated as an input, a UTXO is consumed and will be removed from the global set of unspent outputs once the transaction is confirmed.

2. Outputs (A *new* bill for Julia and a new one for Alex)

The transaction then creates new UTXOs as outputs. Typically, a transaction will have at least two outputs:

* One UTXO representing the payment to the recipient. This output contains a "locking script" (`ScriptPubKey`) that essentially locks the value to the recipient's public address.
* A second UTXO representing the change, which is sent back to a new address controlled by the sender's wallet. Creating a new address for each change output is a key privacy-enhancing feature of modern wallets.

3. Transaction Fee

Bitcoin transactions do not have a dedicated field for the fee. Instead, the fee is implied. It is the total value of all inputs minus the total value of all outputs: $Fee = ∑(Inputs) − ∑(Outputs)$. This leftover amount, which is not assigned to any output address, is collected by the miner who eventually includes the transaction in a block. It serves as a direct economic incentive for the miner to process the transaction.

> Question: Why would the wallet not aggregate *all* the UTXOs to send to Julia?\
> Question: What is the fee in the example in the diagram?

### Signing: Cryptographic Proof of Ownership
With the inputs and outputs defined, the transaction is a structured piece of data, but it is not yet valid. It needs to be authorized. This is where the cryptography from Lecture 2 comes into play.   

The sender's wallet uses the private key corresponding to each input UTXO to generate a unique digital signature via the Elliptic Curve Digital Signature Algorithm (ECDSA). This signature is a mathematical proof that the owner of the funds has authorized this specific transfer. It is attached to the transaction as part of the unlocking script (called `ScriptSig`). This script effectively proves ownership and satisfies the spending conditions of the UTXO's locking script, all without ever revealing the private key to the network.   

### The Role of a Full Node: Validation and Dissemination
Once a transaction is created and signed, it must be broadcast to the Bitcoin network. This is where full nodes take over. They are responsible for validating, propagating, and storing every transaction and block, ensuring the entire system remains secure and consistent.    

> ![image](https://github.com/user-attachments/assets/3fc5d9c6-44af-4601-a2eb-76332fe69b1e)\
> Figure: the high-level data flow within a local node and its interaction with the broader network. Source: Jeff Nijsse.

Inside the node once a transaction is created it is validated along with incoming transactions from the network.

1. Transaction Reception and Validation

When you broadcast a transaction from your wallet, it is sent to a few nearby full nodes. Each node that receives it acts as an independent validator, running a comprehensive checklist to ensure the transaction is legitimate before passing it on.

Key checks include:

* **Syntactic Correctness**: The transaction data must be properly formatted.
* **Input and Output Checks**: Inputs and outputs must be non-empty, and output values cannot exceed input values.
* **Double-Spend Prevention**: The node checks its UTXO database to confirm that each input UTXO is indeed unspent. This is the primary defense against the double-spend problem.
* **Signature Verification**: The node uses the public key to verify the digital signature, confirming authorization from the rightful owner.

2. Propagation (Dissemination)

If a transaction passes all validation checks, the node adds it to its local mempool and then forwards, or propagates, it to all of its connected peers. This process, often called a **gossip** or **flooding** protocol, ensures the transaction spreads exponentially throughout the network, typically reaching nearly every node worldwide within seconds.

This decentralized relay system means senders don't need to trust any single node; as long as the transaction reaches one honest node, it will find its way across the network.

3. Block Reception and Validation

In parallel, nodes listen for newly mined blocks from the network. When a node receives a new block, it performs another round of validation. It checks the block's internal integrity (e.g., valid header, correct Merkle root) and ensures it correctly builds upon the existing blockchain. If the block is valid, the node updates its local copy of the blockchain and relays the block to its peers, continuing the propagation.

This continuous cycle of validation and propagation by thousands of independent nodes is what makes the network resilient. It prevents malicious or invalid data from spreading and ensures that all participants converge on a single, consistent version of the ledger.

## The Mempool: A Transaction Waiting Room
### Defining the Mempool: A Decentralized Queue

Once a node has successfully verified a transaction, it adds it to its local memory pool, or mempool. The mempool is a temporary, in-memory holding area—a "waiting room"—for all valid transactions that are waiting to be included in a block by a miner.   

It is essential to understand that there is no single, global mempool. Every full node on the Bitcoin network maintains its own independent version of the mempool. While the contents of these mempools largely overlap due to the rapid propagation of transactions, they can and do differ. These differences can arise from network latency (which node saw a transaction first) and the individual configuration policies of each node, such as its memory size limit and rules for evicting low-fee transactions.   

### The Fee Market: How Miners Prioritize Transactions
Miners are the ones who construct new blocks. To do this, they look at the transactions waiting in their own mempool and decide which ones to include. Their decision is driven by a simple economic incentive: they keep all the transaction fees from the transactions they include in their block (plus the block subsidy, more on the coinbase reward next lecture).

To maximize their revenue, miners must use the limited space in a block as efficiently as possible. A block has a limit on its size (or more accurately, its "weight"). Therefore, a rational miner will not prioritize transactions based on the total value being sent, nor even the total fee amount. They prioritize based on the fee rate, which is measured in satoshis per virtual byte (sat/vB). A transaction that pays a higher fee for the amount of space it occupies is more profitable for the miner and will be selected first.

Formally, this resembles a **first-price sealed-bid auction**: each user submits a bid (their fee rate) competing for the scarce resource of block space, and miners — acting as auctioneers — greedily select the highest bidders to fill the block weight limit. Unlike a classical single-winner auction, many transactions win per block, making this a multi-unit pay-as-you-bid mechanism. The economic implications of this design — including whether it is incentive-compatible for users to bid their true value — are an active area of research (Lavi et al., 2019).

### Mempool Dynamics: Congestion and Competition
This prioritization creates a dynamic, competitive market for block space. During times of high network usage, more transactions flow into mempools than can be accommodated in the next block (which is mined, on average, every 10 minutes). This causes the mempools across the network to fill up, creating a backlog of unconfirmed transactions.   

This congestion leads to a fee market auction. Users who need their transactions confirmed quickly must outbid others by offering a higher fee rate. Transactions with low fee rates get pushed to the back of the queue and may have to wait for a long time—hours or even days—for confirmation. If congestion remains high, some nodes may eventually drop the lowest-fee transactions from their mempools altogether.   

> ![image](https://github.com/user-attachments/assets/25e1694b-2dbb-4db4-9b1b-313a9b7f6ef0)\
> Figure: [mempool.space](https://mempool.space/block/00000000000000000002333a5906041935688b8fe6e8cc147697921711efbd42) is an excellent resource to visualize realtime bitcoin activity

This chart visualizes the current state of the mempool, organizing pending transactions into color-coded blocks based on their fee rate. The rightmost square (in the [live site](https://mempool.space/mempool-block/0)) represents the transactions with the highest fee rates, which are the most likely to be included in the very next block mined. As you move to the left, the fee rates decrease, representing transactions that will have to wait for subsequent blocks.

## Data Structure: The Anatomy of a Block
After a miner has selected a set of transactions from their mempool, they assemble them into a candidate block. A block is a data structure composed of two primary sections: the Block Header and the Block Body.   

### The Block Header: An 80-Byte Fingerprint
The block header is a concise, 80-byte summary of the block's metadata. This small piece of data is the cornerstone of the blockchain's security. It is the data that miners hash repeatedly during the Proof of Work process, and its final hash becomes the unique identifier for the block. The separation of the small header from the large body is a critical design choice. It allows miners to perform hash computations on a fixed, 80-byte string, rather than on the entire multi-megabyte block. This makes the mining process computationally feasible while still cryptographically securing all the transaction data within the block.   


| Field | Size (Bytes) | Data Type / Format | Description |
| :--- | :--- | :--- | :--- |
| **Version** | 4 | `int32_t` (little-endian) | A version number that indicates which set of block validation rules to follow. It's also used to signal readiness for protocol upgrades. |
| **Previous Block Hash** | 32 | `char[32]` | The `SHA256(SHA256())` hash of the preceding block's header. This cryptographically links the blocks together in a chain. |
| **Merkle Root** | 32 | `char[32]` | The hash of the root of the Merkle tree, which acts as a cryptographic summary of all transactions included in the block. |
| **Timestamp** | 4 | `uint32_t` (little-endian) | The time the miner started hashing the header, expressed in Unix epoch time. It must be greater than the median time of the past 11 blocks. |
| **Difficulty Target (nBits)** | 4 | `uint32_t` (compact format) | An encoded representation of the target threshold. The hash of this block's header must be less than or equal to this target to be valid. |
| **Nonce** | 4 | `uint32_t` (little-endian) | A "**n**umber used **once**." This is the field miners change to alter the output of the hash function in search of a valid Proof of Work. |

The Merkle Root. As we discussed in Lecture 2, a [Merkle tree](https://github.com/millecodex/blockchains101/blob/main/notes/02-cryptography.md#merkle-trees) is built by taking all the individual transaction IDs (TXIDs) in the block, placing them as leaves of a binary tree, and then recursively hashing pairs of nodes until a single root hash is produced. This single 32-byte hash provides a cryptographic commitment to the entire set of transactions. If a single bit in any transaction is altered, the final Merkle Root will change completely, thus invalidating the block header and the proof of work. This structure is also what enables Simple Payment Verification (SPV), allowing lightweight clients to confirm a transaction's inclusion in a block by downloading only the block headers and a small part of the tree (the Merkle proof), rather than the entire multi-megabyte block.

> **SPV Security Caveats.** An SPV client trusts that the chain with the most accumulated proof of work is valid; it cannot independently verify that transactions in a block are themselves valid — only that they were *included*. This means SPV clients must trust the full nodes they query. They are also vulnerable to **eclipse attacks**, where an adversary isolates the client and feeds it a crafted view of the network, potentially hiding transactions or double-spends. SPV is a deliberate trade-off: reduced storage and bandwidth at the cost of reduced security guarantees.

### The Block Body: The Transaction Payload
Following the 80-byte header is the block body, which contains the list of transactions that the block confirms.   

* Transaction Counter: The body begins with a CompactSize integer, a variable-length format that specifies the total number of transactions included in the block.   

* Transactions List: This is the bulk of the block's data. It is simply the full, raw transaction data for every transaction the miner chose to include, concatenated one after another.   

* The Coinbase Transaction: The very first transaction in this list is always the coinbase transaction. This is a special transaction created by the miner. Unlike regular transactions, it has no inputs; it is the mechanism through which new bitcoin is minted. The output of the coinbase transaction pays the miner the block reward, which is composed of two parts: the fixed block subsidy (e.g., 3.125 BTC as of the 2024 halving) and the sum of all transaction fees from every other transaction included in the block.   

## Full Node Storage
How does a full node physically store hundreds of gigabytes of blockchain data on its hard drive? The Bitcoin Core software uses a combination of flat files and a high-performance database to manage this data efficiently.  The main data is stored in a dedicated data directory, which contains several important subdirectories.    

> ![image](https://github.com/user-attachments/assets/)\
> Bitcoin blockchain full node size. In a few years the blockchain will be over 1TB. Source: [CoinLedger](https://coinledger.io/research/bitcoin-blockchain-size-and-growth-over-time)

### Raw Block and Undo Files (`blk*.dat`, `rev*.dat`)
The raw data for every block received from the network is stored sequentially in a series of files named `blkNNNNN.dat` inside the `blocks/` subdirectory.  Each of these files is limited to a maximum size of 128 MB. Once a file is full, the node begins writing to the next one (e.g.,    

`blk00000.dat`, then `blk00001.dat`, etc.  These files contain the complete, unabridged block data, including every transaction, exactly as it was transmitted over the network. Alongside these are `revNNNNN.dat` files. These "undo" files store the information needed to reverse a block's changes to the ledger. This is crucial for handling blockchain reorganizations, where a node might need to switch to a different, longer chain. This does not mean the chain isn't immutable, but it shows that blocks may need to be reorganized depending on the wider network conditions. More on this topic in the Proof of Work lecture.    

### The UTXO Set Database (`chainstate/`)
Validating a new transaction requires checking that its inputs are unspent. Searching through all the raw `blk*.dat` files every time would be very slow. To solve this, Bitcoin Core maintains a separate, highly optimized database of just the UTXOs.    

This database is stored in the chainstate/ subdirectory and uses a key-value database engine called LevelDB. **Key:** The key for each entry is an "outpoint," which is the unique identifier for a specific transaction output (the transaction ID plus the output's index number). **Value:** The value contains the essential data for that UTXO, such as its bitcoin amount and the locking script (`ScriptPubKey`) that defines the conditions for spending it.    

When a new block is confirmed, the chainstate database is updated: the UTXOs that were spent in the block are removed, and the new UTXOs created by the block's transactions are added. This database provides a complete snapshot of all spendable bitcoin at the tip of the chain, making transaction validation extremely fast.    

### The Block Index Database (`blocks/index/`)
Another LevelDB database is kept in the blocks/index/ subdirectory. This is the block index. It contains metadata for every block the node knows about, including a pointer to where the full block data is stored on disk (i.e., in which blk*.dat file and at what byte offset).  This index allows the node to quickly locate and retrieve any specific block from the raw files without having to scan them sequentially.    

### Node data flow
> ![image](https://github.com/user-attachments/assets/3dc1c62e-5b86-4f37-a60e-0e3245e05bcf)\
> Figure: Data flow within the update chain module of a full bitcoin node. This shows where your actual 'bitcoin' are stored. Source: Jeff Nijsse.

1. A valid block is received from the network or mined locally.
2. The block's transactions are used to Update MemPool, removing them from the waiting room since they are now confirmed.
3. The block's header and metadata are used to Update Block Index, a LevelDB database that catalogs all blocks.
4. The raw block data itself is appended to the current blk.dat file (Write blk.dat).
5. Finally, the node processes the transactions in the raw block to Update Chainstate, the LevelDB database containing the UTXO set. It removes the inputs that were spent and adds the newly created outputs.

## Connecting the Blocks: The Chain of Trust
The link between blocks is a simple hash pointer, but it is also so much more. It represents the current network's cumulative proof of computation effort that has been demonstrated in service to the blockchain. The `Previous Block Hash` field in the block header starts the ossification process that leads to immutable transactions.

The header of Block N contains the unique hash of Block N-1's header. The header of Block N-1 contains the hash of Block N-2's header, ..., all the way back to the very first block, the Genesis Block. This creates a direct, ordered, and cryptographically secured chain. This will be the topic of next lecture on Proof of Work consensus.

### Block Propagation and Orphan Blocks
Once a miner finds a valid block, it must propagate to the rest of the network via the gossip protocol. Propagation is not instantaneous. Empirical measurements (Decker & Wattenhofer, 2013) found that in the early Bitcoin network, the mean time for a block to reach 50% of nodes was approximately **6 seconds**, and 95% of nodes received it within **40 seconds**. Block size matters: each kilobyte above ~20 kB added roughly 80 ms of additional delay for the majority of nodes.

This delay has a structural consequence. If two miners find a valid block at roughly the same time — before either block has propagated to the full network — a temporary **fork** occurs. Both blocks are valid, but only one chain will be extended by the next miner, causing the other to become a **stale block** (sometimes called an orphan block). The network discards the losing branch and any transactions unique to it return to the mempool. This represents wasted computational work for the miner whose block was orphaned.

To mitigate this, Bitcoin introduced **Compact Block Relay** (BIP 152) in 2016. Rather than transmitting a full block (~1 MB+) when announcing a new block, a node sends only the block header plus short transaction IDs. Since the receiving node's mempool likely already contains most of those transactions, it can reconstruct the block locally, dramatically reducing transmission size and latency.


## Summary
A transaction's complete lifecycle is traced by its creation in a wallet based on the UTXO model, its authorization through a digital signature, and its broadcast to the network. The examination covers the critical role of full nodes, which validate and disseminate transactions and blocks throughout the peer-to-peer network, a process that ensures system-wide consistency and security.

The mempool is analyzed and presented as a decentralized, competitive waiting area where economically rational miners prioritize transactions based on their fee rate in satoshis per virtual byte. Furthermore, the anatomy of a Bitcoin block is detailed, separating it into the compact 80-byte Header and the much larger Body, which contains the transaction payload.

The full nodes physically store the blockchain in `blk*.dat` files and optimized LevelDB databases for the block index and the UTXO set. The `Previous Block Hash` field forges a cryptographic chain, making the ledger's history prohibitively expensive to alter and giving rise to the fundamental property of immutability.

# What did we miss?
* **Nonce** and **Difficulty Target** get a mention, but we have not yet explored the dynamic and competitive process of how a miner actually finds a valid nonce that satisfies the target.
* Proof of Work **consensus** mechanism that allows a decentralized network to agree on a single version of history, and the process of difficulty adjustment are all critical topics that we will cover in our next lecture.
* **Transaction malleability** and its fix via Segregated Witness (**SegWit**, activated 2017): before SegWit, a third party could alter a transaction's signature data without invalidating the transaction, which also changed its TXID. This "malleability" made certain second-layer protocols (like payment channels) unreliable. SegWit fixed this by moving witness data (signatures) outside the core transaction data used to compute the TXID, decoupling the identifier from the signature. As a side effect, SegWit also introduced the "virtual byte" (vB) weight system visible in mempool.space fee rate calculations.

# Exercises

1.  **Find a Block**: Use a block explorer like `mempool.space` or `blockchain.com` to find the latest Bitcoin block. Identify and list the values for the Block Header components:
    * Timestamp
    * Merkle Root
    * Previous Block Hash
    * Nonce
    * Difficulty

2.  **Transaction Path**: Choose one of the larger (non-coinbase) transactions from that block and click on it.
    * Can you trace its inputs back to previous transactions? Where did the Bitcoins come from?
    * Identify the outputs. How much was sent to the recipient(s), and how much was returned as change?

3.  **Conceptual Question 1**: If you wanted to bribe a miner to include your low-fee transaction quickly, what part of the transaction would you change, and why?

4.  **Conceptual Question 2**: Based on the UTXO model, why might it be a bad privacy practice to combine UTXOs from many different sources (e.g., one from a friend, one from an exchange, one from a salary payment) into a single transaction?

# Readings
* [Block — A Container for Bitcoin Transactions](https://learnmeabitcoin.com/technical/block/) (Learn Me a Bitcoin)
* [What Is a Cryptocurrency Block Header?](https://www.investopedia.com/terms/b/block-header-cryptocurrency.asp)
* [What Is a Mempool?](https://www.ledger.com/academy/what-is-a-mempool) (Ledger)
* [Bitcoin’s UTXO Model: What Is It and How To Manage UTXOs](https://river.com/learn/bitcoins-utxo-model/) (River Financial)

## Supplementary: Web Articles & Video Tutorials
* [Blockchain Demo — Anders Brownworth](https://andersbrownworth.com/blockchain/) — Live interactive demo: build blocks in your browser and see how any change cascades to break the chain
* [Transactions — learnmeabitcoin.com](https://learnmeabitcoin.com/technical/transaction/) — Step-by-step walkthrough of inputs, outputs, locking/unlocking scripts, and TXID
* [Mempool.space FAQ](https://mempool.space/docs/faq) — Explainer for the mempool visualiser used in this lecture; covers fee rate, sat/vB, and block templates
* [Bitcoin Fees Explained — River Financial](https://river.com/learn/bitcoin-fees/) — Plain-English explainer on fee markets, sat/vB, and why fees fluctuate
* [How Bitcoin Transactions Work — Computerphile (YouTube)](https://www.youtube.com/watch?v=em8nsl1iAfE) — 10-minute video covering signing, broadcasting, and UTXOs

 
# Next Lecture
* :point_right: [Proof of Work Consensus](04-pow.md)

# References
1. Corallo, M. (2016). *BIP 152: Compact block relay*. Bitcoin Improvement Proposals. https://github.com/bitcoin/bips/blob/master/bip-0152.mediawiki
2. Dean, J., & Ghemawat, S. (2011). *LevelDB* [Computer software]. Google. https://github.com/google/leveldb
3. Decker, C., & Wattenhofer, R. (2013). *Information propagation in the Bitcoin network*. Proceedings of the 13th IEEE International Conference on Peer-to-Peer Computing (P2P). https://tik-old.ee.ethz.ch/file/49318d3f56c1d525aabf7fda78b23fc0/P2P2013_041.pdf
4. Lavi, R., Sattath, O., & Zohar, A. (2019). *Redesigning Bitcoin's fee market*. Proceedings of the ACM World Wide Web Conference (WWW). https://arxiv.org/abs/1709.08881
5. Nakamoto, S. (2008). *Bitcoin: A peer-to-peer electronic cash system*. https://bitcoin.org/bitcoin.pdf
6. Narayanan, A., Bonneau, J., Felten, E., Miller, A., & Goldfeder, S. (2016). *Bitcoin and cryptocurrency technologies: A comprehensive introduction*. Princeton University Press.
7. Antonopoulos, A. M. (2017). *Mastering Bitcoin: Programming the open blockchain* (2nd ed.). O'Reilly Media.
8. Pérez-Solà, C., Delgado-Segura, S., Navarro-Arribas, G., & Herrera-Joancomartí, J. (2019). *Double-spending prevention for bitcoin zero-confirmation transactions*. International Journal of Information Security. (See also: UTXO set analysis, Financial Cryptography 2018.) https://eprint.iacr.org/2017/1095.pdf

# Video Lectures
* Recorded Live July 15, 2025 on [X](https://x.com/Japple/status/1944991348685520983)
