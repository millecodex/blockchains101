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
  - [The Asset Landscape](#the-asset-landscape)
  - [Stablecoins](#stablecoins)
  - [Decentralised Exchanges (DEXs)](#decentralised-exchanges-dexs)
    - [Pools](#pools)
    - [Automated Market Makers (AMMs)](#automated-market-makers-amms)
    - [The Constant Product Formula](#the-constant-product-formula)
    - [Liquidity Providers and Impermanent Loss](#liquidity-providers-and-impermanent-loss)
    - [DEX Landscape](#dex-landscape)
  - [Lending and Borrowing](#lending-and-borrowing)
    - [Overcollateralisation](#overcollateralisation)
    - [Flash Loans](#flash-loans)
  - [Governance Tokens and DAOs](#governance-tokens-and-daos)
    - [Governance Attacks](#governance-attacks)
- [Oracles: Bridging On-Chain and Off-Chain Data](#oracles-bridging-on-chain-and-off-chain-data)
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
Decentralisation is both a technical property and a political ideology in the blockchain space. Decentralisation means the dispersion of power and influence away from a central authority and towards the individual. This is distint from a distributed system, yet there is no clear boundary between centralised, distributed, and decentralised, it is more of a spectrum.

- **Centralised systems** have a single point of control. Traditional banks, Google Drive, AWS — all centralised. Someone, somewhere, can flip a switch.
- **Distributed systems** spread processing across multiple nodes, but decisions may still be centralised. A Content Delivery Network like Cloudflare serves content from hundreds of edge nodes worldwide, but Cloudflare itself decides what gets served. It is distributed but not decentralised.
- **Decentralised systems** have no single decision-making authority. Every node makes decisions for itself, and emergent system behaviour results from those individual decisions. BitTorrent is a good example — no central tracker is needed; peers find each other and share files without any coordinator.

> <img width="1966" height="804" alt="image" src="https://github.com/user-attachments/assets/67caf88c-cf42-4329-b3c4-c6411cbe20a6" />\
> Figure: Network topology spectrum. A centralised system has one decision-making hub; a distributed system spreads processing across many nodes but retains central control; a decentralised system has no hub — every peer is equal.


Bitcoin is designed to be both distributed (thousands of nodes worldwide) and decentralised (no company or government controls which transactions are valid).  Whether it stays that way in practice is a different question, and one worth asking. When deciding on the degree of decentralisation is can be helpful to ask: Who can censor this? or Who may participate? I think these are very important questions to ask and there is no straightforward answer.

The terms "decentralised" and "distributed" cause confusion because computer science already had a long-standing discipline of distributed systems before blockchains arrived. When a blockchain project claims to be "decentralised," they usually mean something closer to "no single entity controls the system" — a specific and meaningful claim, but one that's surprisingly hard to verify.


## The Decentralisation Spectrum
Blockchain systems don't exist in binary states of centralised or decentralised — they exist on a spectrum, measurable along several independent dimensions:

- **Network Decentralisation:** How many nodes in total? Are they full nodes? Where are they? In how many jurisdictions?
- **Mining/Validator Decentralisation:** What fraction of hashpower or stake do the top participants control? Is it plausbile that a group could form that controls 51%? How hard would it be to coordinate such a group?
- **Dev Decentralisation:** How many independent teams can ship client software? Who/what is funding them?
- **Governance Decentralisation:** Who can propose and ratify protocol changes? Can they be coerced or bought? Is the messaging clear?

Bitcoin scores well on network and mining dimensions but its development is dominated by a small group of Core developers and the community rarely reaches consensus on significant changes. Ethereum has multiple competing execution clients (Geth, Nethermind, Besu, Erigon) which is excellent for resilience — no single client bug can take down the network — but its validator set is increasingly dominated by liquid staking protocols (Lido alone controls ~30% of staked ETH as of 2025, we talked about this last lecture). The point is that "decentralised" is not a label you can attach permanently to a protocol. It's a multi-dimensional property that requires ongoing measurement and active maintenance.

## The Blockchain Trilemma
Vitalik Buterin articulated a fundamental constraint on blockchain design that has become known as the blockchain trilemma: it is extremely difficult — possibly impossible — for a blockchain to simultaneously achieve all three of:

1. **Decentralisation** — no single point of control; open participation; censorship resistance
2. **Security** — resistance to attacks and manipulation and bribery
3. **Scalability** — high transaction throughput as the network grows

> <img width="400" alt="The blockchain trilemma: pick any two ideal properties at the risk of sacrificing the third." src="https://github.com/millecodex/COMP842/assets/39792005/7489c108-9d92-47c0-8b26-94f8a0920163">\
> Figure: The blockchain trilemma — pick any two ideal properties at the risk of sacrificing the third.

The intuition is straightforward: adding more nodes increases decentralisation but slows consensus, because every node must verify every transaction. Reducing the number of nodes speeds things up but centralises control. Adding security requirements (larger PoW targets, higher stake minimums) makes participation expensive, concentrating power among wealthier participants or groups.

|                   | Bitcoin | Ethereum | Solana |
| :---------------- | :-----: | :------: | :----: |
| **Decentralised** |    ✅    |    ✅     |   ⚠️    |
| **Secure**        |    ✅    |    ✅     |   ✅    |
| **Scalable**      |    ❌    |    ⚠️     |   ✅    |

Bitcoin handles around seven transactions per second, Ethereum around 15–30 on the base layer[^baseTPS] — compared to Visa's peak of ~83,000 TPS. Solana can process tens of thousands of TPS, but has suffered multiple network outages and its validator set is small enough that critics question its decentralisation credentials. The trilemma is not proven to be an absolute physical law, but it accurately describes the trade-offs observed in every major blockchain system to date, and it's a useful lens for evaluating claims. The trilemma is not as debated a it used to be, likely due to low blockspace demand, but some have attempted to formalise it. For example, here is a recent 2024 paper: The Blockchain Trilemma: A Formal Proof, *Applied Sciences* (2024). [Link (MDPI)](https://www.mdpi.com/2076-3417/15/1/19)

[^baseTPS]: Layer 1 TPS only. With Layer-2 rollups, Ethereum's effective capacity is far higher — see [Lecture 09: Scaling](09-scaling.md); VISA quoted [here](https://coinlaw.io/visa-statistics/) as 83k.

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
Recentralisation is an interesting social phenomena: even when systems start decentralised, market forces push them back toward centralisation.

Tim O'Reilly observed that blockchain "turned out to be the most rapid recentralization of a decentralized technology that I've seen in my lifetime." Economists at the Bank for International Settlements have described a "decentralisation illusion" — apparent decentralisation masking an inescapable need for centralised governance, and a tendency for consensus mechanisms to concentrate power.[^BIS]

[^BIS]: Halaburda, H. & Bakos, Y. "The Hidden Danger of Re-centralization in Blockchain Platforms" (2025). Brookings Institution. [Link](https://www.brookings.edu/articles/the-hidden-danger-of-re-centralization-in-blockchain-platforms/)

The mechanisms are structural:

- **Infrastructure concentration:** The majority of Ethereum nodes run on AWS, Hetzner, or similar cloud providers. A single provider outage creates correlated failures network-wide.
- **Exchange centralisation:** Most retail users access crypto through Coinbase, Binance, or Kraken — all centralised entities that can freeze accounts, comply with government orders, and apply their own listing standards.
- **Liquid staking concentration:** Lido Finance controls ~30% of all staked ETH. If Lido's operators acted maliciously in concert, they would be the largest single validator bloc on Ethereum.
- **DAO governance in practice:** Research has found that in protocols like Compound, eight addresses control approximately 50% of voting power.[^DAO] Voting rights in decentralised autonomous organisations tend toward concentration faster than in traditional financial markets.

[^DAO]: "Governance of Decentralized Autonomous Organizations: Voter characteristics, engagement and power concentration" (2024). arXiv:2407.10945. [Link](https://arxiv.org/html/2407.10945v1)

This means blockchain decentralisation is a moving target that requires active work to maintain. The DeFi governance section later in this lecture will explore what that looks like in practice.


# Decentralised Finance (DeFi)
Why DeFi at all? In one word: trust. Or, ironically, trustlessness. For the same reason Bitcoin works without a central party — you can transact with a perfect stranger in a foreign country by trusting the protocol, not the person — the cascade of financial products that can be built on digital money is an ideal fit for blockchains. Anything you can do at a bank, an investment bank, a hedge fund, or a stock exchange can be built in code and run on a blockchain. More practical reasons to be interested include higher yields, lower fees, transparency, easier access to foreign markets, and more fine-grained programmable control.

Decentralised Finance — DeFi — refers to financial services built on public blockchains (primarily Ethereum) using smart contracts, without relying on traditional intermediaries like banks, brokers, or clearing houses.[^Schar2021]

[^Schar2021]: Schär, F. (2021). Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets. *Federal Reserve Bank of St. Louis Review*, 103(2), 153–174. [PDF](../papers/pdfs/Schar-DeFi-2021.pdf)

The key properties that distinguish DeFi from traditional finance:

- **Permissionless:** No account application, KYC, or approval required. Anyone with an Ethereum wallet can interact with any DeFi protocol.
- **Programmable:** Smart contracts execute financial logic automatically — interest accrues block-by-block, liquidations happen algorithmically, no human needs to approve anything.
- **Composable:** Protocols can call other protocols. A single transaction can borrow from Aave, swap on Uniswap, deposit into a yield vault, and return the loan — all atomically. This has been called "money legos."
- **Transparent:** All code and all transactions are publicly visible on-chain. Anyone can audit the smart contract logic and verify balances in real time.

DeFi replicates most traditional financial services: trading, lending, borrowing, insurance, derivatives, asset management. The question is not whether these services can be built on-chain — they clearly can — but whether the benefits (permissionless, composable, transparent) outweigh the risks (smart contract bugs, oracle manipulation, regulatory uncertainty, no deposit insurance).

**Total Value Locked (TVL)** is the primary metric used to measure the size of DeFi — the total USD value of assets deposited into DeFi smart contracts. TVL is useful but imperfect: it is denominated in USD, so it can fall simply because crypto prices fall even if no assets were actually withdrawn. DeFi TVL peaked at over $180B in late 2021, collapsed to under $40B during the 2022 bear market, and was around $50B in mid-2024.

## The Asset Landscape
> <img width="800" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/335a3ecd-849b-4af7-bae3-8d91dddc3407">\
> Figure: The asset landscape. Assets can be digital, real, or crossover with both fungible and non-fungible traits.

DeFi lives largely in the fungible-digital box — although stablecoins are also considered DeFi, as they only became possible once blockchain technology made them so.

## Stablecoins
Stablecoins solve a fundamental problem: cryptocurrency prices are volatile, but most financial applications require stability. The primary advantage of a fiat currency on a blockchain is mapping value from the traditional world to the crypto-digital world without exposure to token price volatility. I can exchange $1 for 1 USD-Coin (`USDC`) and be assured that 1:1 mapping will hold. For business operations, valuations, and projections this is crucial. Secondary advantages come from the benefits of a crypto-native platform: low fees, fast settlement, auditability, programmability, and censorship resistance.

It is hard to ignore the growth of stablecoins. In 2021 the total value of stablecoins rose from ~$28B to $150B USD, today its about double at $300B. DeFi has been largely responsible for this demand as stablecoins are useful for liquidity provision, yield farming, lending/borrowing, and short-term settlement.

> <img width="1952" height="584" alt="image" src="https://github.com/user-attachments/assets/d5b96da0-049e-41fd-9c3f-d2292e6e3361" />
> Figure: Total stablecoin supply 2018–-2026. Growth was largely driven by DeFi demand. Source: [TheBlock](https://www.theblockcrypto.com/data/decentralized-finance/stablecoins).

There are three main mechanisms for maintaining a peg:

| Type                  | Examples                    | How Peg Is Maintained                              | Primary Risk                          |
| :-------------------- | :-------------------------- | :------------------------------------------------- | :------------------------------------ |
| Fiat-backed           | USDC, USDT                  | Issuer holds $1 in a bank for every token          | Counterparty risk; regulatory seizure |
| Crypto-collateralised | DAI                         | Smart contract holds >$1 of crypto for every token | Volatility; liquidation cascades      |
| Algorithmic           | TerraUSD *(collapsed 2022)* | Protocol mechanism; no external collateral         | Death spiral                          |

Here is a partial listing of stablecoins, the currency they are pegged to, the collateral backing the peg, and the chains they operate on:

| Stablecoin          | Currency Peg | Backing                                                                                                                | Blockchains                                                                               |
| :------------------ | :----------- | :--------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| `USDT`              | USD          | [mix of assets](https://www.bloombergquint.com/business/tether-gives-more-details-on-assets-backing-crypto-stablecoin) | Ethereum, Algorand, Tron, BSC, Solana, Fantom, etc.                                       |
| `USDC`              | USD          | USD                                                                                                                    | Bitcoin (Liquid), Ethereum, Algorand, BSC, Solana, Stellar, etc.                          |
| `AUDD`,`XAUD`       | AUD          | AUD                                                                                                                    | Ethereum, Solana, Stellar, Polygon                                                        |
| `NZDS`              | NZD          | NZD                                                                                                                    | Ethereum                                                                                  |
| `XSGD`              | SGD          | SGD                                                                                                                    | Ethereum, Solana, Polygon, Arbitrum, Hedera, etc.                                         |
| `EURA`,`EURC`       | EUR          | EUR                                                                                                                    | Ethereum, Polygon, Optimism, Arbitrum, Base, Avalanche, Gnosis, Celo, and BNB Chain, etc. |
| `DAI`,`USDS`        | USD          | crypto collateral                                                                                                      | Ethereum, Polygon, BSC, Fantom, Gnosis, Base, ZKsync, Metis, Linea, Scroll, etc.          |
| `PAXG` — Paxos Gold | 1 oz of gold | physical gold                                                                                                          | Ethereum, Polygon, Optimism, Arbitrum, Base                                               |

Fiat-backed stablecoins are the most widely used. USDC (issued by Circle) publishes monthly reserve attestations and is considered the most transparent. USDT (Tether) is the largest by volume but has historically been opaque about reserve composition.

DAI is crypto-collateralised and genuinely non-custodial: you deposit ETH into a MakerDAO vault, lock at least $1.50 of collateral per $1 of DAI minted, and the protocol liquidates your position automatically if collateral falls too far. This decentralisation has costs — DAI is vulnerable to rapid market crashes that cause collateral shortfalls before liquidations can clear.

> **See Appendix** — The Terra/Luna collapse (May 2022) is a detailed case study in algorithmic stablecoin failure and death spirals. [Jump to case study ↓](#appendix-case-study---the-terraluna-collapse-may-2022)

## Decentralised Exchanges (DEXs)
Most crypto (and all stock) exchanges are centralised and use an order book to match trades — the central limit order book (CLOB) model. This works well for a corporate structure like the NZX that can centrally manage events, but it doesn't scale to a blockchain: all bids and asks would need to be written to the chain, and the latency on price feed updates (especially during liquidations) would be unacceptable.

The decentralised way to run an exchange requires three things: a swap method for users to exchange assets, a pool of each of the assets to draw from, and a method to determine and set the price — an automated market maker. A swap is a direct exchange between two assets at one time, e.g. `ETH ↔ USDT`, although protocols can route trades through multiple hops to find the best price.

### Pools
The assets are drawn from existing pools of *same asset pairings*, e.g. `ETH-USDT` or `DAI-USDC`. There is no broker behind the scenes — if you want to swap DAI for ETH you need a pool for that specific pairing.

This creates a bootstrapping problem: you need a pool before users can swap, but why would someone deposit assets to create a pool? They are incentivised by the protocol — paid by earning a share of transaction fees, or extra tokens, or both. Ideally this is self-reinforcing: if fees are profitable, people add liquidity, which attracts users, which generates more fees.

> <p align="center"><img width="800" alt="Uniswap pool schematic" src="https://user-images.githubusercontent.com/39792005/149413404-3bc2ea73-43a7-4aff-bb23-cefdc785be14.PNG"></p>
>
> Figure: Creating a pool (from the [Uniswap docs](https://docs.uniswap.org/protocol/V2/concepts/core-concerns/pools)) — the Deposit function takes 10 of Token A and 1 of Token B in a 10:1 ratio. The provider receives LP share tokens (`A-B-LP`). On the right, a trader accesses the reserve pool to swap A for B.

To create a pool, deposit two assets into the protocol's smart contract in equivalent values. You are issued an LP token representing the combined assets — e.g. `USDC-ETH-LP-v2` — which is your receipt. You must hold this token to withdraw liquidity and claim rewards. Because you hold a single combined token, you are exposed to second-degree market effects if the ratio of the two assets changes — more on this under *impermanent loss* below.

### Automated Market Makers (AMMs)
The third piece is the automated market maker: it algorithmically ensures every bid can be matched with an ask, making a market for any token pairing. With a large enough pool the price remains stable and will match the wider market. However, if the pool runs thin it becomes difficult to place large orders without significant price movement called slippage.

### The Constant Product Formula
Uniswap, the most widely-used AMM, uses the constant product formula:

> **x × y = k**

Where `x` and `y` are the quantities of the two tokens in the pool, and `k` is a constant that the protocol maintains across every trade.

**Worked example.** Suppose a Uniswap pool holds:
- `x` = 10 ETH
- `y` = 20,000 USDC
- `k` = 10 × 20,000 = 200,000

The implied price of ETH is 20,000 ÷ 10 = $2,000.

Now suppose you want to buy 1 ETH. You're removing 1 ETH from the pool, leaving `x′ = 9`. To preserve `k`:

> y′ = k ÷ x′ = 200,000 ÷ 9 ≈ 22,222 USDC

The pool currently holds 20,000 USDC, so you must deposit 2,222 USDC to receive 1 ETH. The effective price you paid was $2,222 per ETH, not $2,000. The extra $222 is the cost of your trade moving the pool price. Larger trades in shallower pools move the price more dramatically, which is why slippage matters in DeFi. 

### Liquidity Providers and Impermanent Loss
Who supplies the tokens to the pool in the first place? LPs — users who deposit equal value of both tokens in return for LP tokens representing their ownership share of the pool. They earn a fraction of every trading fee (typically 0.3% on Uniswap v2) proportional to their share. But LPs face a risk unique to AMMs: impermanent loss. If the price of one token changes significantly, the AMM's constant rebalancing leaves the LP with less value than if they had simply held the tokens in a wallet.

[Continuing the example] Suppose ETH doubles from $2,000 to $4,000. Arbitrageurs will trade against the pool until its implied price matches the market. At the new price ratio:

- We need `y ÷ x = 4,000` (the new price) *and* `x × y = 200,000`
- Solving: `x = √(200,000 ÷ 4,000)` ≈ 7.07 ETH in the pool
- And: `y = 200,000 ÷ 7.07` ≈ 28,284 USDC in the pool
- LP portfolio value: 7.07 × $4,000 + $28,284 ≈ $56,568

If the LP had simply *held* the original 10 ETH and 20,000 USDC:
- Value: 10 × $4,000 + $20,000 = $60,000

The impermanent loss is $60,000 − $56,568 = $3,432 (~5.7%). If trading fees earned during this period exceed the loss, providing liquidity is profitable. The loss is called "impermanent" because if prices return to the original ratio, the loss disappears entirely — but if the LP exits while prices are different, the loss is realised.

### DEX Landscape
> <img width="2194" height="886" alt="image" src="https://github.com/user-attachments/assets/38b8a529-9c1a-4379-8746-327f51cdc73f" />\
> Figure: [Uniswap](https://uniswap.org/) is the leader in decentralised exchange volume. Source: [TheBlock](https://www.theblockcrypto.com/data/decentralized-finance/dex-non-custodial).

There are now four major versions of Uniswap. This version history illustrates a key constraint of decentralised development: once a smart contract is deployed it is effectively set — it cannot be edited or patched. A new version requires deploying an entirely new contract, which means liquidity must migrate and integrators must update their code.

- **v2** (2020) — the canonical AMM. Introduced direct ERC-20/ERC-20 token pairs and became the industry template for the `x × y = k` model. The [contract code](https://github.com/Uniswap/v2-core/blob/master/contracts/UniswapV2Pair.sol) is still live and used today.
- **v3** (2021) — introduced *concentrated liquidity*. LPs can specify a price range in which they provide liquidity, dramatically increasing capital efficiency for those who correctly predict the trading range — but they earn nothing if the price moves outside it. ([code](https://github.com/Uniswap/v3-periphery))
- **v4** (January 2025) — introduced a *singleton contract* architecture and a system of **hooks**: custom smart contract logic that can be attached at key points in the swap lifecycle (before/after a swap, before/after LP positions change). This allows developers to build features like dynamic fees, on-chain limit orders, or custom oracle integrations directly into a pool, without forking the protocol. The singleton design also reduces gas costs for multi-hop swaps significantly. ([code](https://github.com/Uniswap/v4-periphery))

Other notable DEXs:
- **Curve Finance** — optimised for swaps between assets that should trade near parity (e.g., USDC/USDT, stETH/ETH). Uses a hybrid bonding curve that dramatically reduces slippage between similarly-priced assets.
- **Balancer** — allows pools with more than two assets and custom weight ratios (e.g., 80% ETH / 20% USDC), enabling passive index-like portfolios.

The AMM model aligns well with a decentralised ethos — users can create their own trading pairs, self-custody their assets, and trade globally 24/7 with nothing but an internet connection. The main technical drawbacks are slippage and impermanent loss. There is also cyber risk of contract exploits, of which there have been many thus far into 2026. On the non-technical side there is the crypto problem of onramping and offramping assets to the ~~dark~~ DeFi-side.


## Lending and Borrowing
In traditional finance, lending requires a credit check, collateral, an application, and a human approval process. DeFi lending is peer-to-pool: you deposit assets into a smart contract that algorithmically determines interest rates based on supply and demand, and anyone who posts collateral can borrow instantly.

### Overcollateralisation
Because DeFi is pseudonymous the protocol doesn't know who you are and it can't rely on creditworthiness or legal recourse in case of default. So every loan must be overcollateralised meaning you deposit *more* value than you borrow. Then, if the underlying asset falls quickly in value the the position can be liquidated to (hopefully) break even.

Example. Aave requires a typical collateralisation ratio of 150% for ETH/USDC positions. If ETH is at $2,000:
- Deposit 1.5 ETH ($3,000) as collateral
- Borrow up to $2,000 USDC

Why would anyone borrow $2,000 when they already have $3,000 of collateral? Legitimate reasons include: maintaining ETH exposure while wanting liquidity (and avoiding a taxable sale), using borrowed stablecoins to lever into a yield strategy, or swapping collateral types without selling.

### Flash Loans
A flash loan is a loan with no collateral requirement, subject to one condition: it must be borrowed and repaid within the *same transaction*. If repayment fails, the entire transaction reverts as if nothing happened, so the lender has zero default risk.

Flash loans are a genuine DeFi primitive with no equivalent in traditional finance. Legitimate uses include arbitrage (borrow capital, trade across two DEXs where prices differ, repay the loan, pocket the spread — all atomically) and collateral swaps (replace one form of collateral with another without pausing your position). They have also been used as attack capital — see the Risks section.

## Governance Tokens and DAOs
Most major DeFi protocols are governed by a Decentralised Autonomous Organisation (DAO) — a structure where governance decisions are made through on-chain votes by holders of a governance token. Uniswap holders vote on fee structures. MakerDAO holders vote on collateral risk parameters for DAI. Compound holders vote on which assets can be listed.

The appeal is clear: transparent, community-driven governance instead of opaque corporate decision-making. The reality is more complicated. Token-weighted voting means one token equals one vote — which sounds democratic, but tokens concentrate quickly. Founders and venture investors receive large allocations at launch. Wealthy participants accumulate tokens over time. Research on Compound found that eight addresses controlled approximately 50% of voting power — closer to plutocracy than democracy — and typical voter turnout in DAO proposals is below 5% of eligible tokens.[^DAOpower]

[^DAOpower]: "Governance of Decentralized Autonomous Organizations" (2024). arXiv:2407.10945. [Link](https://arxiv.org/html/2407.10945v1)

On-chain vs. off-chain governance is another dimension. Some DAOs (including Uniswap) use off-chain signalling (via Snapshot) before executing decisions on-chain, reducing gas costs for votes. Research suggests on-chain voting correlates with higher capital raised — whether this reflects genuine governance quality or investor signalling remains an open question.

### Governance Attacks
Governance attacks are a real threat. In April 2023, a malicious governance proposal on a Tornado Cash DAO fork granted the attacker 1.2 million votes, giving them full control of the protocol through the legitimate governance mechanism. This is risk in building decentralised incentives. If governance can be captured by a sufficiently large token position, then "decentralised governance" is only as secure as the cost of acquiring that position.

---

# Oracles: Bridging On-Chain and Off-Chain Data
We introduced oracles briefly in [Lecture 06](06-ethereum.md#oracles), noting that smart contracts cannot fetch external data. For example, a lending protocol needs the current ETH price to decide whether a position should be liquidated; a synthetic asset needs to track a stock price; a parametric insurance contract needs weather data. All of these require a mechanism to bring *trusted* external up to date data on-chain.

The oracle problem is: how do you bring real-world data on-chain without introducing a new point of trust or failure? If a single party controls the price feed, they can manipulate it causing misdirected liquidations, incorrect settlements, or protocol insolvency.

> <p align="center"><img width="800" alt="oracles connect data to blockchains chainlink" src="https://user-images.githubusercontent.com/39792005/152075044-48db86bd-da23-4ad2-bfe0-19ddac7d5cf1.PNG"></p>
> Figure: The oracle problem — blockchains can't natively communicate with real-world data feeds. Source: [Chainlink](https://chain.link/education/blockchain-oracles)

Centralising the solution is straightforward — the NASDAQ publishes stock quotes, Binance displays bid prices — and a centralised oracle follows the same model: a single trusted data provider posts signed data on-chain. Simple to implement, but it reintroduces a single point of failure and a single point of trust.

Chainlink addresses this with a decentralised oracle network: multiple independent node operators each fetch price data from multiple sources, independently aggregate their answers, and post a signed median on-chain.[^chainlink] The network uses economic incentives — staked LINK collateral that can be slashed — to punish dishonest operators. As of April 2026, Chainlink's Total Value Locked (TVL) exceeds $100 billion across DeFi and institutional integrations.

[^chainlink]: Chainlink 2.0 whitepaper. [PDF](https://research.chain.link/whitepaper-v2.pdf)

To avoid situations where a service is unavailable or a feed has been manipulated, protocols can be designed to use multiple oracles — for example, combining Uniswap and Chainlink data, applying a custom weighting function, and publishing the result on-chain.

## Oracle Attack Vectors
Despite these protections, oracle manipulation remains a major DeFi attack vector.[^oracles] For example, AMM-based oracle manipulation: If a protocol uses the current spot price from a Uniswap pool as its price oracle, an attacker can use a flash loan to temporarily distort the pool price, trigger a protocol action (a favourable liquidation, or minting at an inflated price), and repay the flash loan — all in one transaction. The protocol sees a price that nobody actually traded at in equilibrium. Time-Weighted Average Price (TWAP) is the standard defence. Rather than using the current spot price, the protocol reads the average price over many preceding blocks. Sustaining a manipulated price across many blocks requires holding the distortion open, which is expensive and exposes the attacker to arbitrage. Uniswap v3's built-in TWAP oracle has become a widely used reference implementation.


[^oracles]: Zhou, L. et al. (2023). SoK: Decentralized Finance (DeFi) Attacks. *IEEE Symposium on Security and Privacy (S&P)*. [PDF](../papers/pdfs/2208.13035v3.pdf) | [arXiv:2208.13035](https://arxiv.org/abs/2208.13035)


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
