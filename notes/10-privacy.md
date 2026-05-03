[↰ back](../../..)

# Week 10: Privacy
## Contents
- [Week 10: Privacy](#week-10-privacy)
  - [Contents](#contents)
  - [What is Privacy?](#what-is-privacy)
    - [Privacy: A Definition](#privacy-a-definition)
    - [Privacy: In Context with Security and Anonymity](#privacy-in-context-with-security-and-anonymity)
    - [Privacy vs Security](#privacy-vs-security)
    - [Privacy vs Anonymity](#privacy-vs-anonymity)
    - [Security vs Anonymity](#security-vs-anonymity)
  - [Privacy Laws](#privacy-laws)
  - [Blockchain Privacy](#blockchain-privacy)
    - [Pseudonymous](#pseudonymous)
    - [Metadata](#metadata)
    - [Public vs Private Blockchains](#public-vs-private-blockchains)
    - [Chainalysis](#chainalysis)
  - [Mixing](#mixing)
  - [Zero Knowledge](#zero-knowledge)
    - [Alibaba's Cave](#alibabas-cave)
    - [Where's Waldo (Wally?)](#wheres-waldo-wally)
- [Summary](#summary)
- [What did we miss?](#what-did-we-miss)
- [Further Reading - the very short list](#further-reading---the-very-short-list)
- [Exercises](#exercises)
- [Video Lecture](#video-lecture)



## What is Privacy?
### Privacy: A Definition
In the digital age, privacy transcends its traditional boundaries to become a critical concern in the realm of computer science and information technology. As data becomes the new currency, the right to privacy stands at the intersection of ethical, legal, and technological debates. Within the context of blockchain technology, privacy takes on additional layers of complexity. While blockchain can enhance privacy through decentralisation and cryptographic techniques, its immutable nature also raises questions about data permanence and the right to be forgotten. Hence, understanding privacy as a basic human right is crucial for responsible technological advancement and policy-making.

[Article 12](https://www.un.org/en/about-us/universal-declaration-of-human-rights) of the Universal Declaration of Human Rights (UDHR), adopted in 1948, states:
> No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honour and reputation. Everyone has the right to the protection of the law against such interference or attacks.

And closer to the point of *privacy* as a concept by Eric Hughes written in the [Cypherpunk manifesto](https://activism.net/cypherpunk/manifesto.html) (1993):
> Privacy is the power to selectively reveal oneself to the world.
<img width="1920" height="1080" alt="Eric Hughes quote slide Cypherpunk's Manifesto" src="https://github.com/user-attachments/assets/d006e004-6348-4c66-a378-f2fae04059e8" />


### Privacy: In Context with Security and Anonymity

> <img width="505" height="447" alt="image" src="https://github.com/user-attachments/assets/7a28f6b7-9898-4b1c-89f2-9014a848a0f1" />\
> Figure: Privacy, Security, and Anonymity closely overlap and relate to each other. Each is, however, a distinct concept. Can you find real-world and digital examples for each intersection? Source: Nijsse.

### Privacy vs Security
Privacy and security, while closely related, serve distinct roles in the digital landscape. Privacy is primarily concerned with the autonomy individuals have over their personal information—what data is collected, how it is used, and with whom it is shared. Security, on the other hand, focuses on safeguarding that data against unauthorized access and breaches. In the context of blockchain technology, the pseudonymous nature of transactions offers a level of privacy, but it is the blockchain's cryptographic security mechanisms that ensure this data cannot be easily tampered with. Both are indispensable in the construction of robust digital systems, but they address different facets of the information management and safeguarding process.

### Privacy vs Anonymity
Privacy and anonymity are often conflated, but they describe fundamentally different relationships between an individual and their information. Privacy is about *control*—the ability to choose what information is disclosed, to whom, and under what conditions. Anonymity, by contrast, is about *identity concealment*—acting or transacting in a way that cannot be traced back to a real-world person at all. You can have privacy without anonymity (a doctor shares your medical record with a specialist under strict confidentiality—your data is shared, but your consent governs it), and you can have anonymity without privacy (posting publicly on an anonymous forum reveals your content to everyone, but not your name). In blockchain systems this distinction is critical: Bitcoin offers a degree of anonymity through pseudonymous addresses, but once an address is linked to an identity—via an exchange's KYC process, for example—all historical privacy is retrospectively lost. True anonymity, as achieved by Monero's ring signatures or Zcash's shielded transactions, goes a step further by making it cryptographically infeasible to link a transaction to its originator.

### Security vs Anonymity
Security and anonymity can appear to pull in opposite directions, which makes their intersection one of the most contested areas in both cryptography and public policy. Security thrives on accountability—audit trails, identity verification, and the ability to attribute and respond to malicious behaviour. Anonymity, by deliberate design, removes that attribution. In blockchain contexts this tension is stark: a fully anonymous network makes it harder to recover stolen funds, enforce sanctions, or prosecute bad actors, yet the same anonymity protects dissidents, journalists, and ordinary users from surveillance. This trade-off is not purely technical—it is a societal negotiation. Protocols like Privacy Pools (the successor proposal to Tornado Cash) attempt to thread this needle by allowing users to cryptographically prove they are *not* associated with a sanctioned set of addresses, without revealing who they actually are. The key insight is that security and anonymity need not be binary opposites; well-designed zero-knowledge systems can provide selective accountability while preserving anonymity for the vast majority of legitimate users.

## Privacy Laws
Laws and regulations designed to safeguard individual privacy vary significantly across national and international boundaries. In the digital realm, these legal frameworks dictate how personal data should be collected, stored, processed, and shared. They aim to strike a balance between technological innovation and the protection of individual rights, particularly in areas like e-commerce, social networking, and emerging technologies such as blockchain.

The **General Data Protection Regulation** (GDPR) serves as a seminal piece of legislation that has set new global standards for data protection and privacy. Its impact extends beyond the European Union, affecting companies and technologies worldwide. Within the context of blockchain technology, GDPR presents both challenges and opportunities. While blockchain's immutable nature complicates the "right to be forgotten," the technology's built-in security features align well with GDPR's emphasis on data protection.

**Data sovereignty** relates to laws and regulations that dictate where data must be stored and processed. These laws vary by jurisdiction and can introduce significant complexities for global technologies like blockchain. For instance, a blockchain network that spans multiple countries must navigate a labyrinth of local and international laws about data residency, potentially affecting the efficiency and legality of cross-border transactions.

## Blockchain Privacy
Blockchain technology has emerged as a revolutionary paradigm for data storage and transactions, offering significant advantages such as decentralisation, transparency, and immutability. However, these strengths also introduce unique privacy challenges. For instance, the transparency and permanence of blockchain transactions can conflict with traditional notions of privacy, such as the ability to erase or modify personal data. Hence, while blockchain holds the promise of enhanced security and user control, it simultaneously raises complex questions concerning data privacy and individual rights.

### Pseudonymous
Blockchain transactions utilise pseudonyms in the form of alphanumeric addresses to represent participants in a transaction. However, it's crucial to understand that pseudonymous does not mean anonymous. Linking a pseudonym to a real-world identity is not straightforward but is possible through techniques such as chain analysis. Therefore, although blockchain provides a higher degree of privacy compared to traditional transaction methods, it does not guarantee full anonymity.

### Metadata
In addition to the primary transaction data, blockchain transactions often include metadata—additional data fields that provide context for the transaction. This metadata can potentially serve as a vector for user identification, especially when correlated with off-chain data or when subjected to sophisticated data analysis techniques. Hence, even if the primary transaction data is pseudonymous, the metadata can inadvertently compromise user privacy.

### Public vs Private Blockchains
Public blockchains are open to anyone and generally offer more transparency, which can be both an advantage and a drawback when it comes to privacy. Private blockchains, on the other hand, are permissioned networks where entry is controlled. Privacy implications vary significantly between the two; for example, a private blockchain might offer more robust data access controls, but it could also be more susceptible to centralized data collection practices, which pose their own set of privacy risks.

### Chainalysis
Chain analysis involves the scrutiny of blockchain data with the aim of tracing digital asset transactions back to individual users. This is done through a variety of techniques, such as clustering algorithms that group together various addresses controlled by a single entity. While useful for legitimate purposes like fraud detection and regulatory compliance, chain analysis poses a significant risk to user privacy, as it can potentially de-anonymise participants in a blockchain network.

## Mixing
Mixing services act as third-party intermediaries that mix different sets of cryptocurrency funds to make it more challenging to trace their original source. These services are particularly relevant in public blockchain networks where transactions are transparent and can be analysed to identify participants. The main objective of mixing services is to obfuscate transaction trails, thereby enhancing privacy and making it difficult to perform chain analysis.

> <img width="622" height="243" alt="image" src="https://github.com/user-attachments/assets/73c994a6-b094-4f59-b317-96700507ef4b" />\
> Figure: Bob and Alice join their transaction UTXOs together via CoinJoin. This still provides the correct output: 8 to Carol and 15 to Ted, however the outputs are mixed together and so we cannot assume which output corresponds with which input. In a large enough pool this become impractical to link outputs with inputs. 

The principle is to combine multiple payments from multiple spenders into a single transaction. In a typical CoinJoin transaction, it becomes unclear which input (spender) is associated with which output (receiver), making it difficult to trace the origin of the funds. However, it's important to note that while CoinJoin obfuscates the transaction path, it does not make it entirely untraceable. Advanced versions of CoinJoin, like CoinShuffle or CashFusion, add extra layers of privacy by further breaking down and randomly recombining payment amounts.

**Tornado Cash** is a privacy-focused protocol built on the Ethereum blockchain, designed to break the on-chain link between the source and destination addresses. It uses a smart contract that accepts deposits of a fixed amount and can later make a withdrawal to a different address. Between the deposit and withdrawal steps, cryptographic commitments and zero-knowledge proofs are employed to ensure the process is secure yet untraceable. Thus, Tornado Cash makes it exceedingly difficult to establish any connection between the sending and receiving addresses, thereby enhancing transaction privacy on the Ethereum network. 


## Zero Knowledge
Zero-knowledge proofs (ZKPs) are cryptographic techniques that allow one party, known as the prover, to demonstrate to another party, known as the verifier, that a particular statement is true without revealing any specific information about the statement itself. Originating in the late 1980s, ZKPs have become a cornerstone in the realm of cryptographic protocols, particularly in bolstering privacy and security in various applications, including blockchain technology. The fundamental characteristic of a zero-knowledge proof is its ability to maintain the confidentiality of the information being verified, a feature that is increasingly critical in an era of growing concerns about data privacy.

### Alibaba's Cave
The Alibaba's Cave analogy serves as an intuitive way to understand the concept of zero-knowledge proofs. Imagine a cave that is shaped like a 'T', with an entrance at one end and a fork inside that leads to two separate chambers. One chamber contains Alibaba's treasure, and the other is empty. The cave's door can only be opened with a special word, known to the prover but not to the verifier.

> <img width="803" height="252" alt="image" src="https://github.com/user-attachments/assets/e38a1738-24aa-422b-b70c-89532ade27ee" />\
> Figure: 1. The Prover (P) randomly choses a path. 2. The Verifier (V) asks the prover to return via a specific path. 3. If the Prover returns from the correct path it proves they knew the password. Repeat multiple times to defeat luck.

In the zero-knowledge context, the prover wants to convince the verifier that they know the secret word to open the treasure chamber, without actually revealing the word itself. The prover enters the cave and chooses either the left or the right path at the fork. The verifier then enters just up to the fork and shouts which path the prover should come out from. If the prover knows the secret word, they can open the door and come out from the path specified by the verifier, proving they know the secret. Importantly, this happens without revealing what the secret word is.

You may now say, "Sure, you just got lucky." This process may be repeated multiple times to reduce the chance of the prover successfully deceiving the verifier by mere luck. After several rounds, the verifier can become statistically convinced that the prover knows the secret, yet the prover hasn't revealed any information about what the secret actually is.

In a zero-knowledge proof, three essential properties must be met: completeness, soundness, and zero-knowledge. Completeness ensures that if the statement is true, the honest verifier will be convinced of its truth by an honest prover. Soundness means that no cheating prover can convince the honest verifier of the truth of a false statement. Lastly, the zero-knowledge property ensures that the verifier gains no additional information from the interaction, apart from the validity of the statement.

In blockchain contexts, ZKPs are often used to enhance transaction privacy. For example, they can prove that a transaction is valid without revealing the amount, sender, or receiver, thereby achieving a balance between transparency and privacy. Overall, zero-knowledge proofs represent a powerful tool for enhancing privacy in digital interactions and are the primary method currently being persued by blockchain developers.

### Where's Waldo (Wally?)
This is another zero knowledge analogy such that I can prove knowledge of Wally's location without revealing the exact coordiates. A 2-D image can hide a secret if its sufficiently large. The prover can visually show they know the location of the secret by hiding the context (coordinates). Although satisfying, this analogy gives up the secret itself and so is not zero-knowledge. See demonstration in the lecture video. 

> <img width="2490" height="1442" alt="image" src="https://github.com/user-attachments/assets/f93ef4c4-bc65-4449-b57d-073f2728f5d5" />\
> Figure: Knowledge of Waldo can be proven by pointing him out. This gives up the location *and* Waldo's identity.

# Summary
| Technology            | Primary Goal                | Privacy Guarantee                                                                                                       | Key Implementations                                                      | Primary Trade-offs                                                                                                     |
| :-------------------- | :-------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **Coin Mixing**       | Breaking Linkability        | Obscures the on-chain link between deposit and withdrawal addresses by pooling funds from many users.                   | Tornado Cash (historical), various centralized and decentralized mixers. | Can have centralized trust points; anonymity set depends on the number of users; subject to intense regulatory action. |
| **Ring Signatures**   | Sender Anonymity            | Plausible deniability; the true sender is hidden within a group (ring) of potential decoys.                             | Monero                                                                   | Increases transaction data size; privacy depends on the quality and size of the ring; can attract regulatory scrutiny. |
| **Stealth Addresses** | Receiver Anonymity          | Generates a unique, one-time address for each transaction, preventing public linking of payments to a single recipient. | Monero, RAILGUN, Umbra Protocol                                          | Primarily protects the receiver, not the sender or amount; requires additional cryptographic computation.              |
| **zk-SNARKs**         | Transaction Confidentiality | Mathematical proof of transaction validity without revealing sender, receiver, or amount.                               | Zcash, Ethereum L2s (e.g., Aztec), dApps (e.g., RAILGUN)                 | High computational cost for proof generation; often requires a "trusted setup" for initial parameter creation.         |

# What did we miss?
* Tools like [RAILGUN](https://docs.railgun.org/wiki) function as a system of smart contracts that create a shielded pool using zk-SNARKs. Users can deposit assets into the RAILGUN contract and then transact privately and interact with other DeFi protocols from within this shielded environment.
* Coins like [FIRO](https://firo.org/guide/privacy-coin-comparison.html) (prev. [Zcoin](https://en.wikipedia.org/wiki/Firo_(cryptocurrency))) have been adopted in some real-world use cases (e.g., voting in Thailand's elections), which supports its uptake.

# Further Reading - the very short list
* Zcash: History, Privacy, and the Future of Web 3 (w/Zooko Wilcox-O'Hearn & Thomas Walton-Pocock) ([YouTube](https://www.youtube.com/watch?v=ibA_4kwd_YI)) 
* [zk-SNARKs: Under the Hood](https://medium.com/@VitalikButerin/zk-snarks-under-the-hood-b33151a013f6) by Vitalik Buterin: A deep dive into zk-SNARKs and their application in blockchain.
* Blockchain Privacy and Regulatory Compliance: Towards a Practical Equilibrium by Vitalik Buterin et.al (2023). An exploration of privacy issues and solutions in blockchain. ([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4563364)) ([pdf](../papers/pdfs/Buterin-Privacy-2023.pdf))
* The Dining Cryptographers Problem: Unconditional Sender and Recipient Untraceability by David Chaum (1988): Introduces the concept of anonymous communication. ([Springer](https://link.springer.com/content/pdf/10.1007/BF00206326.pdf)) ([pdf](../papers/pdfs/Chaum-DiningCryptographers-1988.pdf))
* Radiolab Podcast 'The Ceremony' about the ZCash trusted setup https://radiolab.org/podcast/ceremony
* [Electronic Frontier Foundation](https://www.eff.org/issues/privacy)'s page with resources on digital privacy
* A Gentle Introduction to Zero-Knowledge Proofs [polygon](https://polygon.technology/blog/a-gentle-introduction-to-zero-knowledge-proofs)


# Exercises
1. **The Pseudonymity Illusion.** Go to [Etherscan](https://etherscan.io) and look up the address `0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` (Vitalik Buterin's public address). List three pieces of information about this person that you can infer purely from on-chain data—without using any off-chain source. What does this exercise reveal about the difference between *pseudonymous* and *anonymous*?

2. **Pick Your Privacy Tech.** You are building a payment app for a country where government surveillance of financial transactions is common. Using the summary table in these notes, choose *one* privacy technology (Coin Mixing, Ring Signatures, Stealth Addresses, or zk-SNARKs) and write a short paragraph (150–200 words) justifying your choice. Your argument must address: (a) what threat model you are defending against, (b) why the trade-offs of your chosen technology are acceptable, and (c) one real-world implementation you would build on.

3. **The GDPR Paradox.** Blockchain's immutability means data written to a public chain cannot be deleted. The EU's GDPR, however, grants individuals a "right to be forgotten" (Article 17). Identify a specific scenario where these two principles come into direct conflict—for example, consider a healthcare records system, a land registry, or a supply chain provenance tracker built on a public blockchain. In about 1 page, describe the conflict and evaluate at least two proposed technical or legal approaches that attempt to resolve it (e.g., storing hashes only, off-chain storage with on-chain pointers, or data encryption with key destruction).

4. **Zero-Knowledge.** The Alibaba's Cave analogy uses repeated rounds to statistically eliminate the chance of a lucky prover. (a) Calculate the probability that a cheating prover successfully fools the verifier after *n* = 1, 5, 10, and 20 rounds. (b) A zk-SNARK collapses this interactive process into a single, non-interactive proof. Explain in your own words what property makes this possible and why it is significant for blockchain scalability. (c) Tornado Cash was sanctioned by the US Treasury in 2022. Using Buterin et al.'s (2023) *Privacy Pools* proposal as a reference, describe how a privacy protocol could satisfy regulatory compliance requirements without revealing the identity of every user. What is the key cryptographic mechanism that enables this?

# Video Lecture
* Here's this lecture recorded live September 18, 2023 on [YouTube](https://www.youtube.com/watch?v=1pK6Iiw0fp0)
* and updated on September 09, 2025 on [X/Twitter](https://x.com/Japple/status/1965266378241581245)
