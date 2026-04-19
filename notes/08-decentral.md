[↰ back](../../..)

# Lecture 08: Decentralisation & DeFi
## Contents
- [Lecture 08: Decentralisation \& DeFi](#lecture-08-decentralisation--defi)
  - [Contents](#contents)
- [Decentralisation](#decentralisation)
  - [The Decentralisation Spectrum](#the-decentralisation-spectrum)
  - [The Blockchain Trilemma](#the-blockchain-trilemma)
  - [Mining Concentration and 51% Attacks](#mining-concentration-and-51-attacks)
  - [The Re-centralisation Problem](#the-re-centralisation-problem)
- [Decentralised Finance (DeFi)](#decentralised-finance-defi)
  - [Automated Market Makers](#automated-market-makers)
    - [The Constant Product Formula](#the-constant-product-formula)
    - [Liquidity Providers and Impermanent Loss](#liquidity-providers-and-impermanent-loss)
    - [DEX Landscape](#dex-landscape)
  - [Lending and Borrowing](#lending-and-borrowing)
    - [Overcollateralisation](#overcollateralisation)
    - [Liquidation](#liquidation)
    - [Flash Loans](#flash-loans)
    - [Key Protocols](#key-protocols)
  - [Stablecoins](#stablecoins)
  - [Yield Farming and Liquidity Mining](#yield-farming-and-liquidity-mining)
  - [Governance Tokens and DAOs](#governance-tokens-and-daos)
- [Oracles: Bridging On-Chain and Off-Chain Data](#oracles-bridging-on-chain-and-off-chain-data)
  - [Centralised vs. Decentralised Oracles](#centralised-vs-decentralised-oracles)
  - [Oracle Attack Vectors](#oracle-attack-vectors)
- [Risks and Challenges](#risks-and-challenges)
  - [Smart Contract Vulnerabilities](#smart-contract-vulnerabilities)
  - [Flash Loan Attacks](#flash-loan-attacks)
  - [Systemic Risks](#systemic-risks)
  - [User-Level Risks](#user-level-risks)
- [What did we miss?](#what-did-we-miss)
- [Further Reading - the very short list](#further-reading---the-very-short-list)
  - [Supplementary Resources](#supplementary-resources)
- [Exercises](#exercises)
- [Video Lecture](#video-lecture)
- [Appendix: Case Study - The Terra/Luna Collapse (May 2022)](#appendix-case-study---the-terraluna-collapse-may-2022)

---

# Decentralisation
Decentralisation is both a technical property and a political ideology in the blockchain space. Decentralisation means the dispersion of power away from a central authority. But isn't that the same as a distributed system? No, and the distinction matters.

- **Centralised systems** have a single point of control. Traditional banks, Google Drive, AWS — all centralised. Someone, somewhere, can flip a switch.
- **Distributed systems** spread processing across multiple nodes, but decisions may still be centralised. A Content Delivery Network like Cloudflare serves content from hundreds of edge nodes worldwide, but Cloudflare itself decides what gets served. It is distributed but not decentralised.
- **Decentralised systems** have no single decision-making authority. Every node makes decisions for itself, and emergent system behaviour results from those individual decisions. BitTorrent is a good example — no central tracker is needed; peers find each other and share files without any coordinator.

> <img width="1966" height="804" alt="image" src="https://github.com/user-attachments/assets/67caf88c-cf42-4329-b3c4-c6411cbe20a6" />\
> Figure: Network topology spectrum. A centralised system has one decision-making hub; a distributed system spreads processing across many nodes but retains central control; a decentralised system has no hub — every peer is equal.


Bitcoin is designed to be both distributed (thousands of nodes worldwide) and decentralised (no company or government controls which transactions are valid). Whether it stays that way in practice is a different question, and one worth asking.

The terms "decentralised" and "distributed" cause confusion because computer science already had a long-standing discipline of distributed systems before blockchains arrived. When a blockchain project claims to be "decentralised," they usually mean something closer to "no single entity controls the system" — a specific and meaningful claim, but one that's surprisingly hard to verify.


## The Decentralisation Spectrum
Blockchain systems don't exist in binary states of centralised or decentralised — they exist on a spectrum, measurable along several independent dimensions:

- **Network Decentralisation:** How many nodes in total? Are they full nodes?Where are they? In how many jurisdictions?
- **Mining/Validator Decentralisation:** What fraction of hashpower or stake do the top participants control? Is it plausbile that a group could form that controls 51%? How hard would it be to coordinate such a group?
- **Dev Decentralisation:** How many independent teams can ship client software? Who/what is funding them?
- **Governance Decentralisation:** Who can propose and ratify protocol changes? Can they be coerced or bought? Is the messaging clear?

Bitcoin scores well on network and mining dimensions but its development is dominated by a small group of Core developers and the community rarely reaches consensus on significant changes. Ethereum has multiple competing execution clients (Geth, Nethermind, Besu, Erigon) which is excellent for resilience — no single client bug can take down the network — but its validator set is increasingly dominated by liquid staking protocols (Lido alone controls ~30% of staked ETH as of 2025, we talked about this last lecture).

The point is that "decentralised" is not a label you can attach permanently to a protocol. It's a multi-dimensional property that requires ongoing measurement and active maintenance.

## The Blockchain Trilemma
Vitalik Buterin articulated a fundamental constraint on blockchain design that has become known as the **blockchain trilemma**: it is extremely difficult — possibly impossible — for a blockchain to simultaneously achieve all three of:

1. **Decentralisation** — no single point of control; open participation; censorship resistance
2. **Security** — resistance to attacks and manipulation
3. **Scalability** — high transaction throughput as the network grows

> <img width="400" alt="The blockchain trilemma: pick any two ideal properties at the risk of sacrificing the third." src="https://github.com/millecodex/COMP842/assets/39792005/7489c108-9d92-47c0-8b26-94f8a0920163">\
> Figure: The blockchain trilemma — pick any two ideal properties at the risk of sacrificing the third.

The intuition is straightforward: adding more nodes increases decentralisation but slows consensus, because every node must verify every transaction. Reducing the number of nodes speeds things up but centralises control. Adding security requirements (larger PoW targets, higher stake minimums) makes participation expensive, concentrating power among wealthier participants or groups.

|                   | Bitcoin | Ethereum | Solana |
| :---------------- | :-----: | :------: | :----: |
| **Decentralised** |    ✅    |    ✅     |   ⚠️    |
| **Secure**        |    ✅    |    ✅     |   ✅    |
| **Scalable**      |    ❌    |    ⚠️     |   ✅    |

Bitcoin handles around seven transactions per second, Ethereum around 15–30 on the base layer[^baseTPS] — compared to Visa's peak of ~24,000 TPS. Solana can process tens of thousands of TPS, but has suffered multiple network outages and its validator set is small enough that critics question its decentralisation credentials. 

[^baseTPS]: Layer 1 TPS only. With Layer-2 rollups, Ethereum's effective capacity is far higher — see [Lecture 09: Scaling](09-scaling.md).

The trilemma is not proven to be an absolute physical law[^trilemmaproof], but it accurately describes the trade-offs observed in every major blockchain system to date, and it's a useful lens for evaluating claims.

[^trilemmaproof]: The trilemma is not as debated a it used to be, likely due to low blockspace demand, but some have attempted to formalise it. Here is a recent 2024 paper The Blockchain Trilemma: A Formal Proof, *Applied Sciences* (2024). [Link (MDPI)](https://www.mdpi.com/2076-3417/15/1/19)

## Mining Concentration and 51% Attacks
One of the most concrete tests of decentralisation is whether any single entity can gain majority control of the consensus mechanism. In a Proof of Work system, this means >50% of hashrate. In Proof of Stake, it means >33% of staked assets for liveness attacks (halting the chain) or >50% for censorship.

In mid-2014, the mining pool GHash.io briefly held more than 50% of Bitcoin's global hashrate — for about 12 hours. No attack was launched, but the event demonstrated that "decentralisation" was a design goal, not a guarantee. As of 2026, two mining pools — Foundry USA (~34%) and AntPool (Singapore/China) (~18%) — together control just under 50% of Bitcoin's hashrate.

> <img width="1496" height="724" alt="image" src="https://github.com/user-attachments/assets/b3c4aaa1-ae73-4282-9b3e-579969063d31" />
> Figure: As of April 2026 the top 2 mining pools control just a hair under 50% of Bitcoin's hashrate. Source: [Hashrate Index](https://hashrateindex.com/hashrate/pools)

With majority control, an attacker could:
- **Double-Spend** their own transactions: spend coins, then rewrite history to reverse the payment and spend again
- **Censor Transactions** by refusing to include specific addresses in any block
- **Orphan Competing Miners' Blocks**, thereby reducing the earnings of their competitors

A rational attacker would hesitate, though: a successful 51% attack would probably cause Bitcoin's price to collapse, destroying the value of both their mining hardware and their coins. The attack is deterred less by technical impossibility and more by economic self-interest — which is a different kind of security guarantee than cryptographic impossibility.


## The Re-centralisation Problem
Here is where the blockchain story gets genuinely complicated: even when systems start genuinely decentralised, market forces push them back toward centralisation.

Tim O'Reilly observed that blockchain "turned out to be the most rapid recentralization of a decentralized technology that I've seen in my lifetime." Economists at the Bank for International Settlements have described a "decentralisation illusion" — apparent decentralisation masking an inescapable need for centralised governance, and a tendency for consensus mechanisms to concentrate power.[^BIS]

[^BIS]: Halaburda, H. & Bakos, Y. "The Hidden Danger of Re-centralization in Blockchain Platforms" (2025). Brookings Institution. [Link](https://www.brookings.edu/articles/the-hidden-danger-of-re-centralization-in-blockchain-platforms/)

The mechanisms are structural:

- **Infrastructure concentration:** The majority of Ethereum nodes run on AWS, Hetzner, or similar cloud providers. A single provider outage creates correlated failures network-wide.
- **Exchange centralisation:** Most retail users access crypto through Coinbase, Binance, or Kraken — all centralised entities that can freeze accounts, comply with government orders, and apply their own listing standards.
- **Liquid staking concentration:** Lido Finance controls ~30% of all staked ETH. If Lido's operators acted maliciously in concert, they would be the largest single validator bloc on Ethereum.
- **DAO governance in practice:** Research has found that in protocols like Compound, eight addresses control approximately 50% of voting power.[^DAO] Voting rights in decentralised autonomous organisations tend toward concentration faster than in traditional financial markets.

[^DAO]: "Governance of Decentralized Autonomous Organizations" (2024). arXiv:2407.10945. [Link](https://arxiv.org/html/2407.10945v1)

None of this means blockchain decentralisation is impossible or fraudulent — it means it's a moving target that requires active work to maintain. The DeFi governance section later in this lecture will explore what that looks like in practice.


# Decentralised Finance (DeFi)
Decentralised Finance — DeFi — refers to financial services built on public blockchains (primarily Ethereum) using smart contracts, without relying on traditional intermediaries like banks, brokers, or clearing houses.[^Schar2021]

[^Schar2021]: Schär, F. (2021). Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets. *Federal Reserve Bank of St. Louis Review*, 103(2), 153–174. [PDF](../papers/pdfs/Schar-DeFi-2021.pdf)

The key properties that distinguish DeFi from traditional finance:

- **Permissionless:** No account application, KYC, or approval required. Anyone with an Ethereum wallet can interact with any DeFi protocol.
- **Programmable:** Smart contracts execute financial logic automatically — interest accrues block-by-block, liquidations happen algorithmically, no human needs to approve anything.
- **Composable:** Protocols can call other protocols. A single transaction can borrow from Aave, swap on Uniswap, deposit into a yield vault, and return the loan — all atomically. This has been called "money legos."
- **Transparent:** All code and all transactions are publicly visible on-chain. Anyone can audit the smart contract logic and verify balances in real time.

**Total Value Locked (TVL)** is the primary metric used to measure the size of DeFi. It is the total USD value of assets deposited into DeFi smart contracts — think of it as "how much money has been entrusted to these protocols." TVL is useful but imperfect: it's denominated in USD, so it can fall simply because crypto prices fall even if no assets were actually withdrawn. DeFi TVL peaked at over $180B in late 2021, collapsed to under $40B during the 2022 bear market, and was around $50B in mid-2024.

DeFi replicates most traditional financial services: trading, lending, borrowing, insurance, derivatives, asset management. The question isn't whether these services can be built on-chain — they clearly can — but whether the benefits (permissionless, composable, transparent) outweigh the risks (smart contract bugs, oracle manipulation, regulatory uncertainty, no deposit insurance). That's genuinely contested, and the honest answer depends on what you're trying to do.

## Automated Market Makers

Traditional financial exchanges use an **order book**: buyers post bids ("I'll pay $X for Y shares"), sellers post asks ("I'll sell Y shares for $Z"), and the exchange matches them. This works well when there are enough buyers and sellers to create liquid markets, but thin markets suffer from wide bid-ask spreads and low volume.

DeFi introduced a different model: the **Automated Market Maker (AMM)**. Instead of matching individual buyers and sellers, an AMM uses a *liquidity pool* — a smart contract holding reserves of two tokens — and a mathematical formula to determine prices automatically.

### The Constant Product Formula

Uniswap, the most widely-used AMM, uses the **constant product formula**:

> **x × y = k**

Where `x` and `y` are the quantities of the two tokens in the pool, and `k` is a constant that the protocol maintains across every trade.

**Worked example.** Suppose a Uniswap pool holds:
- `x` = 10 ETH
- `y` = 20,000 USDC
- `k` = 10 × 20,000 = **200,000**

The implied price of ETH is 20,000 ÷ 10 = **$2,000**.

Now suppose you want to buy 1 ETH. You're removing 1 ETH from the pool, leaving `x′ = 9`. To preserve `k`:

> y′ = k ÷ x′ = 200,000 ÷ 9 ≈ **22,222 USDC**

The pool currently holds 20,000 USDC, so you must deposit **2,222 USDC** to receive 1 ETH. The effective price you paid was **$2,222** per ETH, not $2,000. The extra $222 is **price impact** — the cost of your trade moving the pool price. Larger trades in shallower pools move the price more dramatically, which is why *slippage* matters in DeFi. Split a large trade into smaller pieces, and each piece causes less impact.

### Liquidity Providers and Impermanent Loss

Who supplies the tokens to the pool in the first place? **Liquidity providers (LPs)** — users who deposit equal value of both tokens in return for LP tokens representing their ownership share of the pool. They earn a fraction of every trading fee (typically 0.3% on Uniswap v2) proportional to their share.

But LPs face a risk unique to AMMs: **impermanent loss**. If the price of one token changes significantly, the AMM's constant rebalancing leaves the LP with less value than if they had simply held the tokens in a wallet.

**Continuing the example.** Suppose ETH doubles from $2,000 to $4,000. Arbitrageurs will trade against the pool until its implied price matches the market. At the new price ratio:

- We need `y ÷ x = 4,000` (the new price) *and* `x × y = 200,000`
- Solving: `x = √(200,000 ÷ 4,000)` ≈ **7.07 ETH** in the pool
- And: `y = 200,000 ÷ 7.07` ≈ **28,284 USDC** in the pool
- LP portfolio value: 7.07 × $4,000 + $28,284 ≈ **$56,568**

If the LP had simply *held* the original 10 ETH and 20,000 USDC:
- Value: 10 × $4,000 + $20,000 = **$60,000**

The impermanent loss is $60,000 − $56,568 = **$3,432** (~5.7%). If trading fees earned during this period exceed the loss, providing liquidity is profitable. The loss is called "impermanent" because if prices return to the original ratio, the loss disappears entirely — but if the LP exits while prices are different, the loss is realised.

### DEX Landscape

Uniswap dominates DEX volume, but several alternatives have distinct designs worth knowing:

- **Curve Finance** — optimised for swaps between assets that *should* trade near parity (e.g., USDC/USDT, stETH/ETH). Uses a hybrid formula that dramatically reduces slippage between similarly-priced assets.
- **Balancer** — allows pools with more than two assets and custom weight ratios (e.g., 80% ETH / 20% USDC), enabling passive index-like portfolios.
- **Uniswap v3** — introduced *concentrated liquidity*, allowing LPs to provide liquidity only within a specified price range. An LP who correctly predicts ETH will trade between $1,800 and $2,200 earns fees as if their capital were many times larger — but earns nothing if the price leaves their range.

## Lending and Borrowing

In traditional finance, lending requires a credit check, collateral, an application, and a human approval process. DeFi lending is **peer-to-pool**: you deposit assets into a smart contract that algorithmically determines interest rates based on supply and demand, and anyone who posts collateral can borrow instantly.

### Overcollateralisation

Because DeFi is pseudonymous — the protocol doesn't know who you are — it can't rely on creditworthiness or legal recourse. Every loan must be **overcollateralised**: you deposit *more* value than you borrow.

**Example.** Aave requires a typical collateralisation ratio of 150% for ETH/USDC positions. If ETH is at $2,000:
- Deposit 1.5 ETH ($3,000) as collateral
- Borrow up to $2,000 USDC

Why would anyone borrow $2,000 when they already have $3,000 of collateral? Legitimate reasons include: maintaining ETH exposure while wanting liquidity (and avoiding a taxable sale), using borrowed stablecoins to lever into a yield strategy, or swapping collateral types without selling.

### Liquidation

If the value of your collateral falls below the protocol's required ratio, a **liquidation** occurs. Third parties called *liquidators* can repay your outstanding loan and receive your collateral at a discount — typically 5–10% — as their reward for keeping the protocol solvent.

**Continuing the example.** Suppose ETH falls from $2,000 to $1,200:
- Collateral value: 1.5 × $1,200 = **$1,800**
- Outstanding loan: **$2,000 USDC**
- Collateralisation ratio: $1,800 ÷ $2,000 = 90% — well below the required 150%

A liquidator steps in, repays the $2,000 USDC, and receives the $1,800 of ETH plus a liquidation bonus paid by the protocol. The borrower loses their collateral position entirely. Liquidations execute in a single transaction, automatically, with no court order or negotiation required. This is one of the genuinely novel properties of DeFi — the enforcement mechanism is the code.

### Flash Loans

A **flash loan** is a loan with no collateral requirement, subject to one condition: it must be borrowed and repaid within the *same transaction*. If repayment fails, the entire transaction reverts as if nothing happened, so the lender has zero default risk.

Flash loans are a genuine DeFi primitive with no equivalent in traditional finance. Legitimate uses include arbitrage (borrow capital, trade across two DEXs where prices differ, repay the loan, pocket the spread — all atomically) and collateral swaps (replace one form of collateral with another without pausing your position). They have also been used as attack capital — see the Risks section.

### Key Protocols

- **Aave** — the largest lending protocol by TVL (~$19.6B, April 2026). Introduced flash loans and supports dozens of assets across multiple chains.
- **Compound** — pioneered algorithmic interest rates and was the first protocol to distribute governance tokens (COMP) to users.
- **Morpho** — a lending optimiser that routes deposits between Aave and Compound to continuously find the better rate.

## Stablecoins

Stablecoins solve a fundamental problem: cryptocurrency prices are volatile, but most financial applications require stability. A stablecoin is a token designed to maintain a fixed value, almost always pegged to $1 USD. There are three main mechanisms:

| Type                      | Examples                    | How Peg Is Maintained                              | Primary Risk                          |
| :------------------------ | :-------------------------- | :------------------------------------------------- | :------------------------------------ |
| **Fiat-backed**           | USDC, USDT                  | Issuer holds $1 in a bank for every token          | Counterparty risk; regulatory seizure |
| **Crypto-collateralised** | DAI                         | Smart contract holds >$1 of crypto for every token | Volatility; liquidation cascades      |
| **Algorithmic**           | TerraUSD *(collapsed 2022)* | Protocol mechanism; no external collateral         | Death spiral                          |

Fiat-backed stablecoins are the most widely used. USDC (issued by Circle) publishes monthly reserve attestations and is considered the most transparent. USDT (Tether) is the largest by volume but has historically been opaque about reserve composition.

DAI is crypto-collateralised and genuinely non-custodial: you deposit ETH into a MakerDAO vault, lock at least $1.50 of collateral per $1 of DAI minted, and the protocol liquidates your position automatically if collateral falls too far. This decentralisation has costs — DAI is vulnerable to rapid market crashes that cause collateral shortfalls before liquidations can clear.

> **See Appendix** — The Terra/Luna collapse (May 2022) is a detailed case study in algorithmic stablecoin failure and death spirals. [Jump to case study ↓](#the-terraluna-collapse-may-2022)

## Yield Farming and Liquidity Mining

When Compound Finance launched its COMP governance token in June 2020, it made a decision that defined an era: it distributed COMP tokens to anyone who borrowed or lent through the protocol, proportional to their activity. This was **liquidity mining** — using protocol-issued tokens to bootstrap liquidity and user adoption. The results were dramatic: billions of dollars poured into Compound within days as users chased COMP rewards.

**Yield farming** is the broader strategy of actively moving assets between DeFi protocols to maximise return — typically stated as APY (Annual Percentage Yield). A farmer might:

1. Deposit USDC into Aave at 5% interest, receiving aUSDC (an interest-bearing token)
2. Use aUSDC as collateral to borrow more USDC
3. Deposit that USDC into Compound to earn 4% + COMP governance tokens
4. Supply Compound's cUSDC to a Curve pool to earn trading fees + CRV tokens

Each step compounds the yield — but also compounds the risk. Every protocol hop adds smart contract risk, liquidation risk, and the risk that incentive token prices (COMP, AAVE, CRV) fall faster than they are earned.

The economics of liquidity mining follow a predictable arc: high initial APYs attract capital, more capital dilutes yield per dollar, sophisticated capital moves on to the next protocol, and APYs normalise or the protocol fails. The early summers of DeFi (2020–2021) saw APYs in the thousands of percent — almost entirely from token inflation rather than real protocol revenue. Understanding this pattern is essential for evaluating DeFi opportunities honestly.

## Governance Tokens and DAOs

Most major DeFi protocols are governed by a **Decentralised Autonomous Organisation (DAO)** — a structure where governance decisions are made through on-chain votes by holders of a governance token. Uniswap holders vote on fee structures. MakerDAO holders vote on collateral risk parameters for DAI. Compound holders vote on which assets can be listed.

The appeal is clear: transparent, community-driven governance instead of opaque corporate decision-making. The reality is more complicated. **Token-weighted voting** means one token equals one vote — which sounds democratic, but tokens concentrate quickly. Founders and venture investors receive large allocations at launch. Wealthy participants accumulate tokens over time. Research on Compound found that eight addresses controlled approximately 50% of voting power — closer to plutocracy than democracy — and typical voter turnout in DAO proposals is below 5% of eligible tokens.[^DAOpower]

[^DAOpower]: "Governance of Decentralized Autonomous Organizations" (2024). arXiv:2407.10945. [Link](https://arxiv.org/html/2407.10945v1)

**On-chain vs. off-chain governance** is another dimension. Some DAOs (including Uniswap) use off-chain signalling (via Snapshot) before executing decisions on-chain, reducing gas costs for votes. Research suggests on-chain voting correlates with higher capital raised — whether this reflects genuine governance quality or investor signalling remains an open question.



**Governance attacks** are a real threat. In April 2023, a malicious governance proposal on a Tornado Cash DAO fork granted the attacker 1.2 million votes, giving them full control of the protocol — not through a smart contract exploit, but through the legitimate governance mechanism. This is a design failure, not a bug: if governance can be captured by a sufficiently large token position, then "decentralised governance" is only as secure as the cost of acquiring that position.

---

# Oracles: Bridging On-Chain and Off-Chain Data

We introduced oracles briefly in [Lecture 06](06-ethereum.md#oracles), noting that smart contracts cannot fetch external data. This section covers the oracle problem in the depth needed to understand DeFi.

A lending protocol needs the current ETH price to decide whether a position should be liquidated. A synthetic asset needs to track a stock price. A parametric insurance contract needs weather data. All of these require a mechanism to bring *trusted* external data on-chain — that mechanism is an oracle.

The **oracle problem** is: how do you bring real-world data on-chain without introducing a new point of trust or failure? If a single party controls the price feed, they can manipulate it — causing misdirected liquidations, incorrect settlements, or protocol insolvency.

## Centralised vs. Decentralised Oracles

A centralised oracle is a single trusted data provider that posts signed data on-chain. Simple, but creates a single point of failure.

**Chainlink** addresses this with a decentralised oracle network: multiple independent node operators each fetch price data from multiple sources, independently aggregate their answers, and post a signed median on-chain.[^chainlink] The network uses economic incentives — staked LINK collateral that can be slashed — to punish dishonest operators. As of 2025, Chainlink secures tens of billions of dollars in DeFi value.

[^chainlink]: Chainlink 2.0 whitepaper. [PDF](https://research.chain.link/whitepaper-v2.pdf)

## Oracle Attack Vectors

Despite these protections, oracle manipulation remains a major DeFi attack vector.[^oracles]

[^oracles]: Eskandari, S. et al. (2020). A First Look into DeFi Oracles. [PDF](../papers/pdfs/Eskandari-DeFiOracles-2020.pdf) | [arXiv](https://arxiv.org/abs/2005.04377)

**AMM-based oracle manipulation:** If a protocol uses the current spot price from a Uniswap pool as its price oracle, an attacker can use a flash loan to temporarily distort the pool price, trigger a protocol action (a favourable liquidation, or minting at an inflated price), and repay the flash loan — all in one transaction. The protocol sees a price that nobody actually traded at in equilibrium.

**Time-Weighted Average Price (TWAP)** is the standard defence. Rather than using the current spot price, the protocol reads the average price over many preceding blocks. Sustaining a manipulated price across many blocks requires holding the distortion open, which is expensive and exposes the attacker to arbitrage. Uniswap v3's built-in TWAP oracle has become a widely used reference implementation.

---

# Risks and Challenges

DeFi's composability is its greatest technical achievement and its greatest risk factor. Because protocols stack on top of each other, a failure anywhere in the stack can cascade through all dependent protocols.

## Smart Contract Vulnerabilities

Smart contracts are immutable once deployed — bugs cannot be patched the way server software can be. Every major DeFi protocol has undergone extensive security audits, but no audit provides a guarantee. Novel logic errors continue to be the primary source of large-scale losses.

Common vulnerability classes:
- **Reentrancy** — a contract sends ETH before updating its own state; the recipient calls back recursively before the balance is updated. This is how the DAO was hacked in 2016 (see [Lecture 06](06-ethereum.md#smart-contracts)). The fix is the Checks-Effects-Interactions pattern: check conditions, update state, *then* transfer funds.
- **Integer overflow/underflow** — arithmetic that exceeds the data type's range wraps around silently. Solidity 0.8+ added automatic protection, but legacy contracts remain vulnerable.
- **Access control flaws** — admin-only functions left publicly callable, or ownership transfer mechanisms that can be exploited.
- **Logic errors** — the contract does exactly what it was programmed to do, but the programmer's intent was different.

Modern tooling (Slither, MythX, OpenZeppelin's auditing libraries) catches many of these issues at development time, but sophisticated attackers focus on application-layer logic that automated tools can't reason about.

## Flash Loan Attacks

Flash loans lower the capital barrier for attacks to near zero. Instead of an attacker needing tens of millions of their own capital, a flash loan attack requires only gas fees.

**Example — Platypus Finance (2023):** An attacker borrowed $44M in a flash loan, exploited a logic error in Platypus's emergency withdrawal function to extract ~$8.5M in profit, and repaid the flash loan — all within a single transaction. The attacker's net cost was a few dollars of gas.

[REKT News](https://rekt.news/) maintains a running post-mortem of DeFi exploits. At time of writing, over $6 billion has been extracted from DeFi protocols through various exploits since 2020.

## Systemic Risks

**Contagion:** DeFi's composability means failures cascade. When Terra/Luna collapsed in May 2022, it triggered liquidations across Aave and Compound (UST was used as collateral), caused billion-dollar losses at crypto hedge funds like Three Arrows Capital, and contributed to the collapse of centralised lenders (Celsius, Voyager) that were deeply exposed to DeFi yields. A single protocol failure became a multi-sector crisis.

**Regulatory uncertainty:** DeFi exists in an ambiguous regulatory space. The US SEC has argued that many governance tokens are unregistered securities. The EU's MiCA regulation provides a framework for centralised crypto businesses but largely exempts fully decentralised protocols — and very few protocols are fully decentralised. Tax treatment of yield farming rewards, LP fees, and governance token receipts varies by jurisdiction and is largely unsettled.

## User-Level Risks

- **Private key loss** = permanent loss of funds. No password reset, no recovery phrase email, no customer service.
- **Phishing via fake frontends** — the smart contract may be entirely sound, but a cloned website can return malicious transaction data that drains your wallet when you sign.
- **Impermanent loss** — covered above, but it's a material risk for LP positions in volatile markets.
- **Gas fee volatility** — during periods of high network activity, transaction costs spike unpredictably. Ethereum gas prices have exceeded $100 per transaction during peak demand.

---

# What did we miss?
- **Real World Assets (RWAs)** — tokenisation of traditional financial assets (US Treasuries, real estate, private credit) is one of the fastest-growing DeFi sectors; Tether Gold and BlackRock's BUIDL fund are early examples.
- **MEV (Maximal Extractable Value)** — validators and searchers can reorder, include, or exclude transactions within a block to extract profit; this is a significant and ongoing structural issue for DeFi fairness. Covered further in [Lecture 11](11-security.md).
- **Account Abstraction (ERC-4337)** — smart contract wallets that allow recovery mechanisms, session keys, and gas sponsorship; a major improvement to UX that doesn't require holding ETH to interact with DeFi.
- **Cross-chain bridges** — the infrastructure for moving assets between blockchains, and the source of over $2B in losses to bridge exploits (Ronin, Wormhole, Nomad).
- **Privacy in DeFi** — all DeFi transactions are public on-chain; projects like Tornado Cash (privacy mixer, later OFAC-sanctioned) and Aztec (ZK-based private DeFi) attempt to address this. The regulatory battle between financial surveillance and financial privacy is ongoing. More in the lecture on privacy.

---

# Further Reading - the very short list
- Buterin, V. "The Meaning of Decentralization" (2017). [Medium post](https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274).
- Schär, F. (2021). *Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets*. Federal Reserve Bank of St. Louis Review, 103(2), 153–174. [PDF](../papers/pdfs/Schar-DeFi-2021.pdf).
- "The Hidden Danger of Re-centralization in Blockchain Platforms" (2025). Brookings Institution. [Link](https://www.brookings.edu/articles/the-hidden-danger-of-re-centralization-in-blockchain-platforms/)

## Supplementary Resources
- [Finematics — History of DeFi Explained](https://finematics.com/history-of-defi-explained/).
- [Uniswap v2 Core whitepaper](https://uniswap.org/whitepaper.pdf).
- [Finematics — Flash Loans Explained (Aave, dYdX)](https://finematics.com/flash-loans-explained/).
- [Chainlink — What Is a Blockchain Oracle?](https://chain.link/education/blockchain-oracles).

---

# Exercises
1. **Trilemma Evaluation.** Evaluate Bitcoin, Ethereum, and Solana on the three trilemma dimensions (security, decentralisation, scalability). Which dimension does each prioritise? Find current metrics: number of validators/nodes, hashrate or stake distribution, and observed TPS for each chain.
2. **AMM Walkthrough.** A Uniswap pool holds 500 LINK tokens and 5,000 USDC (so `k = 500 × 5,000 = 2,500,000`). (a) What is the implied price of LINK in USDC? (b) A trader buys 50 LINK. How much USDC must they deposit to preserve `k`? (c) What is the effective price per LINK, and why does it differ from (a)?
3. **Governance in Practice.** Go to [snapshot.org](https://snapshot.org) and find a recent governance proposal. Summarise: what was the proposal, what was the voter turnout as a percentage of total supply, and how did the top five wallet addresses vote? What does this tell you about the practical decentralisation of governance in that protocol?
4. **Oracle Design.** A DeFi lending protocol needs a reliable ETH/USD price feed to trigger liquidations. Compare these three approaches: (a) spot price from a Uniswap pool, (b) Chainlink decentralised oracle, and (c) Uniswap TWAP over 30 minutes. For each: what attack vectors exist, and approximately how much capital would be required to manipulate the price?


# Video Lecture

* TBC

---

# Appendix: Case Study - The Terra/Luna Collapse (May 2022)

TerraUSD (UST) was an algorithmic stablecoin that maintained its $1 peg through an arbitrage mechanism with LUNA, a companion token:

- If UST traded *below* $1: burn $1 of LUNA to mint 1 UST. Buy cheap UST on the market, burn it, receive $1 of newly minted LUNA, sell LUNA. The buying pressure returns UST toward $1.
- If UST traded *above* $1: the reverse — burn 1 UST, receive $1 of LUNA. The selling pressure returns UST toward $1.

This worked as long as participants had confidence that LUNA itself had value. In May 2022, coordinated large-scale selling of UST broke the peg slightly. Arbitrageurs began burning LUNA to defend the peg — which increased LUNA's supply, diluting its price. As LUNA's price fell, confidence in the mechanism collapsed, triggering more UST selling, which required more LUNA minting, further diluting LUNA's price. This self-reinforcing collapse is the **death spiral**:

- LUNA supply: 340 million → 6.5 **trillion** tokens within days
- LUNA price: ~$80 → near zero
- UST price: $1.00 → near zero
- Total value destroyed: ~**$60 billion**

The Terra collapse prompted regulatory scrutiny of stablecoins globally. The EU's MiCA regulation now requires fiat-backed reserves for stablecoins above certain thresholds, effectively ruling out pure algorithmic models in the EU. A cautionary tale not just about a single protocol, but about the risks of systems that rely entirely on confidence loops with no external anchor.

> <img width="2002" height="1392" alt="image" src="https://github.com/user-attachments/assets/a88458c4-a987-44e4-bab8-5aa589003756" />\
> Figure: Terra/Luna death spiral (May 2022). The top strip shows the normal arbitrage mechanism that was supposed to maintain the $1 UST peg. Once confidence in the LUNA collateral collapsed, the same mechanism became a self-reinforcing feedback loop: defending the peg required minting more LUNA, which diluted LUNA’s price, which undermined confidence further, driving more UST selling. LUNA’s circulating supply grew from 340 million to 6.5 trillion tokens within days; approximately $60 billion of value was destroyed.