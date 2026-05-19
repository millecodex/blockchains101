[↰ back](../../..)
# Week 12: Money (Revisited) & Future Trends
(Still under constrution 🚧 as of May 2026 ⚠️)
## Contents
- [The Evolution of Money (Revisited)](#the-evolution-of-money-revisited)
- [Central Bank Digital Currencies (CBDCs)](#central-bank-digital-currencies-cbdcs)
- [Tokenization of Real-World Assets](#tokenization-of-real-world-assets)
- [AI and the Blockchain](#ai-and-the-blockchain)
- [Quantum Computing](#quantum-computing)
- [What did we miss?](#what-did-we-miss)
- [Exercises](#exercises)
- [Further Reading](#further-reading)
- [References](#references)


# The Evolution of Money (Revisited)

In [Lecture 1](01-money-bitcoin.md) we traced the long arc from cowrie shells and Medici ledgers to Bitcoin's genesis block. So, after twelve weeks of studying cryptographic protocols, consensus mechanisms, smart contracts, scaling solutions, privacy, and security, we can evaluate the question: have we made any progress?

## Some Recent Monetary History

### The Gold Standard
The gold standard is a monetary system where a country's currency has a value directly linked to gold — governments held gold in reserve and allowed conversion upon request. Adopted by the UK in 1821, it spread globally and survived, in various forms, until the Great Depression. Its appeal was discipline: governments could not print money faster than they could mine gold.

It was abandoned because that discipline was also its fatal flaw. Fixed exchange rates prevented countries from adjusting their currencies in response to economic shocks. Scarcity of gold constrained economic growth. When economies needed to expand money supply to fight unemployment and depression, the gold standard wouldn't allow it.

### Bretton Woods (1944–1971): The Pseudo-Gold Standard
After World War II, the allied nations met at Bretton Woods, New Hampshire to design a new monetary order. The agreement fixed all major post-war currencies to the U.S. dollar at stable exchange rates, and the U.S. dollar was itself fixed to gold at $35 USD per troy ounce. Every other currency was therefore indirectly backed by gold, via the dollar. This system also created the IMF and the World Bank.

### WTF Happened in 1971?
On August 15, 1971, President Nixon announced that the U.S. would suspend the convertibility of the dollar to gold — effectively ending Bretton Woods unilaterally. The U.S. had been running balance-of-payments deficits and financing the Vietnam War, and foreign governments were redeeming dollars for gold faster than the U.S. could manage. The "Nixon Shock" decoupled global money from any commodity anchor permanently.

> <img width="700" alt="WTF Happened in 1971 — Tomato Soup price" src="https://github.com/millecodex/COMP842/assets/39792005/5bd525fb-c642-4984-a13c-8f396493e54b">\
> Figure: Inflation on a can of Campbell's Tomato Soup — a common domestic good tracked by inflation researchers. Before 1971, prices were comparatively stable; after the dollar was unmoored from gold, purchasing power eroded steadily. Source: [wtfhappenedin1971.com](https://wtfhappenedin1971.com/)

The year 1971 is not just a historical curiosity. It is the point at which money became, for the first time in modern history, purely political as its supply is now determined entirely by the decisions of central banks and governments, with no external anchor.

## The Properties of Money, Revisited

Recall the classical requirements for money: it must function as a *medium of exchange*, a *unit of account*, and a *store of value*. In [Lecture 1](01-money-bitcoin.md), we added affordability, availability, durability, fungibility, portability, and reliability to that list. After studying cryptographic systems, we can add further properties that become newly salient — particularly around censorship resistance, privacy, and programmability.

The table below expands this framework across five monetary forms. The notation follows Nijsse (2020): **✓!** = hyper / exceeds; **✓** = yes / full; **(✓)** = partial; **±** = yes for some variants, no for others; **–** = does not apply or absent.

| Property          | Fiat (cash) | Digital Fiat / CBDC | Gold  | Bitcoin | Cryptocurrency |
| ----------------- | :---------: | :-----------------: | :---: | :-----: | :------------: |
| **Fungible**      |      ✓      |          ✓          |  ✓!   |   (✓)   |       ±        |
| **Divisible**     |      ✓      |         ✓!          |   –   |   ✓!    |       ✓!       |
| **Reliable**      |      ✓      |         (✓)         |  ✓!   |    ✓    |       ±        |
| **Affordable**    |      ✓      |         ✓!          |   –   |   (✓)   |       ✓        |
| **Physical**      |      ✓      |          –          |   ✓   |    –    |       –        |
| **Portable**      |      ✓      |          –          |  (✓)  |    –    |       –        |
| **Durable**       |      ✓      |          –          |   ✓   |    –    |       –        |
| **Asset-backed**  |     (✓)     |          –          |   –   |    ✓    |      (✓)       |
| **Private**       |      ✓      |          –          |   ✓   |   (✓)   |       ±        |
| **Anonymous**     |      ✓      |          –          |   ✓   |   (✓)   |       ±        |
| **Censorable**    |      –      |         ✓!          |   –   |   (✓)   |      (✓)       |
| **Confiscatable** |     (✓)     |          ✓          |   ✓   |    –    |       –        |
| **Auditable**     |      –      |          ✓          |   –   |    ✓    |       ✓        |
| **Transparent**   |      –      |          –          |   –   |    ✓    |       ±        |
| **Programmable**  |      –      |          ✓          |   –   |    ✓    |       ✓        |
| **Decentralized** |      –      |          –          |   –   |    ✓    |       –        |
| **Anti-fragile**  |      –      |          –          |   –   |    ✓    |       –        |

> Table: Monetary characteristics applied to five monetary forms. Notation: **✓!** hyper/exceeds; **✓** yes; **(✓)** partial; **±** yes/no depending on implementation; **–** absent or not applicable. Source: adapted from Nijsse (2020).

No instrument scores perfectly across all rows — and critically, different stakeholders weight the rows differently. A central bank cares most about *reliable*, *auditable*, and *programmable*; a citizen under capital controls cares most about *private*, *confiscatable*, and *censorable*; a long-term saver cares about *asset-backed*, *durable*, and *anti-fragile*. Understanding who holds the power to design a monetary system tells you which rows will be optimised.

*See [Appendix: Property Glossary](#appendix-property-glossary) for definitions of all 17 properties.*

## Macro Analysis: Inflation and the Money Printer

The Bitcoin whitepaper appeared on October 31, 2008 — six weeks after Lehman Brothers collapsed and the U.S. Federal Reserve began the first of several rounds of quantitative easing (QE). QE involves a central bank purchasing financial assets (typically government bonds) with newly created money, expanding the monetary base. Between 2008 and 2022, the U.S. M2 money supply grew from approximately $7.5 trillion to $21.7 trillion — nearly tripling in fourteen years (Federal Reserve, 2023).

> <img width="1920" height="979" alt="image" src="https://github.com/user-attachments/assets/84f4ed1e-84f7-4cd6-80f1-bf84869be85d" />\
> Figure: The price of gold in US dollars remained stable until 1971. The inverse is also true: the value of a dollar has decreased against the value of gold. Source: Wikipedia.

M2 Chart Broken, needs attention.

> Figure: U.S. M2 money supply components, 2006–2024. The sharp vertical rise in 2020 corresponds to COVID-era stimulus spending. Source: Federal Reserve / Wikimedia Commons.

> Q: If the supply of money doubles but the supply of goods and services does not, what happens to prices?

The consequence is purchasing power erosion: a dollar in 2008 purchased what required approximately $1.55 by 2024 (U.S. Bureau of Labor Statistics CPI data). This is not a bug in the eyes of central banks — a target inflation rate of ~2% per year is considered optimal for encouraging spending and investment over hoarding. Critics, particularly in the Austrian economic tradition, argue that any inflation is a form of taxation on savings, and that monetary expansion disproportionately benefits asset owners (the Cantillon effect: those closest to the money printer see prices rise last).

> <img width="1126" height="1501" alt="image" src="https://github.com/user-attachments/assets/bd2575e7-3fd6-4bce-819a-d702197e10c3" />
> Figure: Cost of consumer good and services tracked shows a clear trend of inflationary services provisioned by centralised institutions (governments) and deflationary electronics.

## What Can Governments Do? Three Uncomfortable Options

Governments that have accumulated large debts guaranteed by the voters whose savings are silently eroded by inflation face a narrow set of structural options. None of them are popular:

1. *Raise Taxes* — Increase government revenue to service debt without printing money. This is politically difficult: voters punish governments that raise taxes, and high-income earners and corporations have the mobility and resources to reduce their exposure. The revenue gain is often smaller than expected, and the political cost is immediate.

2. *Austerity* — Cut government spending to reduce deficits. Also politically difficult: cutting pensions, health services, or infrastructure is immediately felt by constituents. The eurozone debt crisis of 2010–2015 demonstrated that imposed austerity can trigger social instability and democratic backsliding without reliably restoring growth.

3. *Grow Your Way Out* — Increase GDP faster than debt accumulates, so the debt-to-GDP ratio falls even if the nominal debt does not. This is the most desirable outcome and the one that actually worked for post-WWII economies. It requires genuine productivity gains — technological innovation, labour force participation, capital investment. It cannot be manufactured by policy alone, and it is becoming harder in ageing, high-debt economies. One bright spot in this regard is the innovation brought about by LLMs, AI research and infrastructure, and the potential for future artificial intelligence applications.

The implicit fourth option — the one governments have most consistently chosen since 2008 — is

4. *Print Money*: - Pay the deb with freshly printed money, keep interest rates low, and transfer the cost of debt onto savers through purchasing power erosion. It is politically the easiest option in the short run because the mechanism is opaque. Voters do not directly vote against quantitative easing.

> Q: If inflation is effectively a tax on savings, who pays it and who collects it? How does this compare to a conventional income or wealth tax in terms of visibility, fairness, and political accountability?

## Case Studies: When Inflation Becomes a Crisis

For most people in wealthy countries, inflation is a nagging inconvenience — grocery bills up 20%, real wages flat. In other economies, inflation has crossed into territory that destroys livelihoods and forces mass emigration.

### Venezuela
Venezuela's economy depended heavily on oil revenues. When oil prices collapsed in 2014, the government of Nicolás Maduro chose to print money to fund both imports and domestic social programs rather than cut spending. With no productive base to support the expanding money supply, the bolivar collapsed. Inflation ran at six-digit rates for several years — at one point the IMF estimated 1,000,000% annually. An estimated 7.7 million Venezuelans emigrated between 2012 and 2022, one of the largest forced displacement events in Latin American history (UNHCR, 2023). Cryptocurrency, particularly USD stablecoins, became a practical lifeline for many Venezuelans trying to preserve savings or receive remittances from family abroad.

### El Salvador
El Salvador dollarized in 2001, abandoning its previous currency, the colón, in favour of the U.S. dollar. In June 2021, under President Nayib Bukele, it became the first country to adopt Bitcoin as legal tender (alongside the USD). By law, businesses including McDonald's and Starbucks were required to accept it. The government holds Bitcoin on its national balance sheet (~7,655 BTC as of 2026, tracked publicly at [bitcoin.gov.sv](https://bitcoin.gob.sv/)).

The experiment has been controversial:
- The IMF threatened to withhold a \$1B loan over what it called reckless financial behaviour
- Citizen uptake of the government's Chivo wallet was low and primarily driven by a \$30 sign-up bonus
- El Salvador also launched geothermal Bitcoin mining using volcano energy and created special economic zones with no capital gains tax on tech investment (Google has established a regional presence)

In 2024, El Salvador reached an agreement with the IMF that effectively made Bitcoin acceptance *optional* rather than mandatory for businesses — a significant walk-back of the original legal tender mandate. The experiment is neither a clear success nor a clear failure; it is a live field trial of what it looks like when a state formally adopts a fixed-supply digital asset.

## Crypto Adoption: A Global Snapshot

Bitcoin and cryptocurrencies are, at their core, about the choice to participate in a different financial system. The adoption data below suggests this choice is most compelling where the existing system is failing people most visibly.

The table shows the percentage of internet users who report owning or having owned cryptocurrency, surveyed across countries 2019–2023. Note the correlation with the inflation column.

| Country          | 2019 | 2020 | 2021 | 2022 | 2023 | Inflation (2024 %) |
| ---------------- | ---- | ---- | ---- | ---- | ---- | ------------------ |
| 🇳🇬 Nigeria        | 28%  | 32%  | 42%  | 45%  | 47%  | **33.9**           |
| Turkey           | 20%  | 16%  | 25%  | 40%  | 47%  | **58.5**           |
| 🇦🇷 Argentina      | 16%  | 14%  | 21%  | 35%  | 26%  | **117**            |
| 🇮🇩 Indonesia      | 11%  | 13%  | 12%  | 19%  | 29%  | 2.8                |
| 🇧🇷 Brazil         | 18%  | 12%  | 12%  | 22%  | 28%  | 4.8                |
| 🇮🇳 India          | 8%   | 8%   | 10%  | 22%  | 27%  | 4.9                |
| 🇵🇭 Philippines    | —    | 20%  | 28%  | 29%  | —    | 3.2                |
| 🇻🇳 Vietnam        | 22%  | 21%  | 27%  | 27%  | —    | 3.6                |
| 🇲🇾 Malaysia       | —    | 12%  | 16%  | 20%  | 23%  | 1.8                |
| 🇵🇰 Pakistan       | 6%   | 6%   | 14%  | 19%  | 18%  | **23.4**           |
| 🇿🇦 South Africa   | 16%  | 17%  | 18%  | 23%  | 22%  | 4.4                |
| 🇦🇺 Australia      | 7%   | 8%   | 9%   | 16%  | 17%  | 3.8                |
| 🇺🇸 United States  | 5%   | 7%   | 8%   | 15%  | 16%  | 2.9                |
| 🇸🇬 Singapore      | —    | 10%  | 11%  | 25%  | —    | 2.4                |
| 🇳🇿 New Zealand    | 6%   | 5%   | 11%  | 15%  | 14%  | 2.2                |
| 🇬🇧 United Kingdom | 6%   | 5%   | 5%   | 10%  | 12%  | 2.6                |

> Table: Global crypto ownership rates, percentage of internet users, 2019–2023. Source: Statista / Triple-A. Inflation figures: IMF World Economic Outlook 2024. **Bold** indicates above-average inflation.

The pattern is consistent: high adoption correlates with high inflation and currency instability. This does not mean cryptocurrency *solves* inflation for individuals — volatility remains a barrier to everyday use — but it suggests that people reach for alternative stores of value when their national currency is demonstrably failing them.

---

# Central Bank Digital Currencies

A **Central Bank Digital Currency (CBDC)** is a digital form of a country's sovereign currency, issued and backed directly by the central bank. Unlike cryptocurrency, a CBDC is not decentralized — it is the most centralized form of digital money possible. Unlike commercial bank deposits, a CBDC represents a direct liability of the central bank itself, not of a private institution.

As of 2025, over 130 countries representing 98% of global GDP are exploring CBDCs, with 66 in advanced development, pilot, or launch phases (Atlantic Council CBDC Tracker, 2025).

## CBDC Architectures

There are two primary architectural models:

| Model                      | Description                                                | Example                   |
| -------------------------- | ---------------------------------------------------------- | ------------------------- |
| **Retail (Direct)**        | Central bank issues CBDC directly to citizens              | China's e-CNY (partial)   |
| **Retail (Intermediated)** | Commercial banks distribute CBDC on behalf of central bank | ECB Digital Euro proposal |
| **Wholesale**              | CBDC used only for interbank settlement, not retail        | Project mBridge (BIS)     |

The intermediated model preserves the existing role of commercial banks while upgrading the settlement layer. The direct model raises the prospect of every citizen holding an account at the central bank — which would disintermediate commercial banks and give the state unprecedented visibility into individual transactions.

## The Decentralization Question

How decentralized is a CBDC? The short answer is: **not at all by design**. Unlike a permissionless blockchain where no party controls the ledger, a CBDC ledger is controlled entirely by the issuing central bank. The key policy questions are:

- **Programmability**: Can spending be restricted to certain categories (e.g. no gambling, no foreign purchases)?
- **Expiry**: Can the CBDC be time-limited to encourage spending (as China piloted with e-CNY red packets)?
- **Surveillance**: Are all transactions visible to the state?
- **Anonymity**: Can any form of privacy be preserved for small transactions?

These features represent a spectrum from "digital cash equivalent" (anonymous, unrestricted) to "programmable panopticon" (fully tracked and controlled). Most CBDC proposals sit closer to the latter in their technical architecture, even when their marketing claims otherwise.

> Q: A CBDC with programmable spending restrictions — is this a monetary policy tool, a surveillance tool, or both? Where is the line?

## Citizen Resistance and Civil Liberties Concerns

Public reaction to CBDC proposals has been markedly skeptical in several jurisdictions:

- **United States**: Congressional bills have explicitly proposed banning a U.S. retail CBDC (CBDC Anti-Surveillance State Act, 2023). Concerns centre on financial privacy and government overreach.
- **European Union**: The ECB's digital euro proposal drew over 8,000 public consultation responses, the majority raising privacy concerns. The ECB subsequently committed to "cash-like" privacy for small transactions, though critics note the architecture does not technically guarantee this.
- **United Kingdom**: The Bank of England's consultation on the "digital pound" received 50,000+ responses, many negative. The governor stated the Bank had "no intention" of monitoring transactions, but could not make this a technical guarantee.

The core tension is structural: a CBDC that provides genuine financial privacy is almost indistinguishable from cash or private cryptocurrency — making it less useful as a monetary policy tool. A CBDC that is useful as a policy tool requires transaction visibility.

## Implementation Struggles: The Technology Hasn't Kept Up

Central banks have struggled to ship CBDC technology that performs at national scale, preserves any privacy, and integrates with existing financial infrastructure:

**Nigeria — eNaira (2021)**: The world's first major retail CBDC launch. Two years after launch, adoption was under 0.5% of the population. Nigerians preferred mobile money (which works offline), USD stablecoins, and cash. The government's attempt to force adoption by demonetizing large-denomination naira notes in 2023 caused a cash crisis and street protests, without meaningfully improving eNaira uptake (Auer et al., 2023).

**China — e-CNY**: The most technically advanced CBDC in deployment, with hundreds of millions of digital wallets opened. However, active usage remains low relative to WeChat Pay and Alipay. Pilot features including expiring money and geo-restricted spending have raised international concern about the template being exported via Belt and Road infrastructure.

**Eurozone — Digital Euro**: Formally entered "preparation phase" in November 2023. Legislative framework remains incomplete. A full launch is not expected before 2028 at the earliest.

**United States**: No retail CBDC development. The Fed has stated it would only proceed with explicit authorisation from Congress. The political environment remains hostile.

> Q: Nigeria's eNaira failed despite government backing. What does this tell us about the relationship between legal tender status and actual adoption?

---

# Tokenization of Real-World Assets

**Real-World Asset (RWA) tokenization** refers to representing ownership rights in a traditional off-chain asset — a bond, share of stock, property title, or commodity — as a digital token on a blockchain. If CBDCs represent governments trying to capture blockchain infrastructure, RWA tokenization represents traditional finance doing the same.

This is widely regarded as one of the most credible near-term applications of blockchain technology, not because it is decentralized, but because it delivers genuine efficiency gains: faster settlement, fractional ownership, 24/7 markets, and programmable compliance — without requiring the wholesale replacement of existing financial institutions.

| Institution        | Product         | Asset Class                    | Scale (2025)   |
| ------------------ | --------------- | ------------------------------ | -------------- |
| BlackRock          | BUIDL Fund      | U.S. Treasury Bills            | ~\$500M AUM    |
| Franklin Templeton | BENJI           | Government Money Market        | ~\$400M AUM    |
| Ondo Finance       | OUSG            | Short-duration U.S. Treasuries | ~\$200M AUM    |
| JPMorgan           | Onyx / JPM Coin | Repo / Wholesale settlements   | Billions daily |

> Table: McKinsey (2024) estimated \$2 trillion in liquid tokenized assets by 2030. The bottleneck is not technology — it is regulatory clarity.

## How Tokenization Works

A tokenized asset typically involves three layers:

1. **Legal wrapper**: A special-purpose vehicle (SPV) holds the underlying asset off-chain. Token holders have a legal claim on the SPV.
2. **Token standard**: On-chain representation uses compliance-enabled token standards such as ERC-3643 (T-REX), which embeds KYC/AML checks directly into the transfer function.
3. **Oracle/Custodian**: A trusted third party attests that the off-chain asset exists and matches on-chain supply.

This architecture is deliberately *permissioned*: transfers are restricted to KYC-whitelisted addresses. Tokenized securities are the opposite of DeFi — they rely on centralized legal and custodial trust, while using blockchain for settlement efficiency.

> Q: If tokenized assets require trusted custodians and KYC-whitelisted transfers, what does the blockchain actually add over a conventional database?

## Case Study: Anthropic Secondary Market Equity

On 12 May 2026, Anthropic updated its public support page to warn investors against a wave of secondary platforms claiming to offer access to its shares. The company named eight firms explicitly — Open Doors Partners, Unicorns Exchange, Pachamama Capital, Lionheart Ventures, Hiive, Forge Global, Sydecar, and Upmarket — and issued an unambiguous statement:

> *"Any sale or transfer of Anthropic stock, or any interest in Anthropic stock, offered by these firms is void and will not be recognized on our books and records."*
> — [Anthropic support page](https://support.claude.com/en/articles/13704655-unauthorized-anthropic-stock-sales-and-investment-scams), May 2026

The context matters: Anthropic was rumoured to be raising fresh funding at a $900 billion valuation, making it one of the most sought-after private assets in the world. Unicorns Exchange reported receiving over 50 institutional inquiries in three months representing more than $1 trillion in aggregate demand — none of which resulted in completed deals, because sellers could not provide proof of Anthropic's consent.

The mechanism behind the platforms varied: some offered shares in SPVs (special-purpose vehicles) holding Anthropic stock; others offered derivative instruments such as pre-IPO perpetual futures contracts tracking the company's secondary market value without conveying actual ownership. Anthropic's statement applies clearly to SPVs: *"We do not permit special purpose vehicles to acquire Anthropic stock and any transfer of shares to an SPV are void under our transfer restrictions."*

Forge Global disputed being included, claiming it was listed erroneously and that it does not facilitate transactions without explicit company approval. Hiive similarly asserted that all transfers it facilitates are issuer-approved. Sydecar stated it acts only in an administrative capacity and requires sponsors to attest they have the required consents.

Sources: [TechCrunch, 12 May 2026](https://techcrunch.com/2026/05/12/anthropic-warns-investors-against-secondary-platforms-offering-access-to-its-shares/) | [Bloomberg, 12 May 2026](https://www.bloomberg.com/news/articles/2026-05-12/anthropic-warns-investors-to-avoid-certain-secondary-market-sellers)



# AI and the Blockchain

Artificial intelligence and blockchain have developed largely in parallel and are increasingly positioned as complementary. Two directions are worth examining: AI using blockchain infrastructure, and blockchain infrastructure for AI systems.

## AI Using Blockchain

Decentralized compute markets: Training large AI models requires significant GPU compute dominated by AWS, Google Cloud, and Azure. Projects like *Akash Network* and *io.net* aggregate idle GPU capacity from distributed providers, paying in cryptocurrency and settling on-chain. The value proposition: lower cost and censorship-resistant access to compute.

Verifiable AI inference (zkML): Zero-knowledge proofs (see [Lecture 10](10-privacy.md)) can prove that a computation was performed correctly without revealing inputs. Applied to AI, this is *zero-knowledge machine learning* (zkML). A user could prove an AI model produced a specific output from a specific input — useful for auditing AI decisions in regulated contexts — without revealing the model weights.

Content provenance: As AI-generated content becomes indistinguishable from human-created content, blockchain-based attestation — where a creator signs and timestamps work on-chain — offers a mechanism for provenance. The C2PA standard (Coalition for Content Authenticity and Provenance), backed by Adobe and Microsoft, is the leading industry effort.

Prediction markets: Platforms like *Polymarket* use blockchain-settled markets to aggregate crowd intelligence (not AI) on real-world outcomes, functioning as decentralized forecasting engines with accuracy benchmarks that sometimes exceed expert panels.

## Blockchain Infrastructure for AI Agents

A more speculative area involves *autonomous AI agents* — software systems that act in the world without continuous human oversight — using cryptocurrency rails for economic activity:

- **Micro-payments**: An agent paying per-API-call in stablecoin micropayments, without needing a credit card.
- **On-chain identity**: Agents with verifiable cryptographic identities, enabling authentication of interactions.
- **Bittensor**: A marketplace for AI model outputs where models compete to provide the best responses, rewarded in the network's native token (TAO) based on peer evaluation.

> Q: If an AI agent can autonomously hold and spend cryptocurrency, who is legally responsible for its transactions?

## Key Tensions

| Tension                  | Description                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Centralization vs. ethos | AI development is dominated by a handful of corporations — the opposite of crypto's decentralization ideal       |
| Energy consumption       | Both PoW mining and large AI training runs compete for the same GPU and power infrastructure                     |
| Verification cost        | zkML proofs are computationally expensive; practical verifiable AI inference remains an open engineering problem |
| Hype vs. reality         | Many "AI + blockchain" projects in 2023–2025 are marketing exercises, not genuine technical integrations         |

---

# Quantum Computing

Quantum computing represents the most significant long-term technical threat to the cryptographic foundations of every blockchain in existence.

## Why Blockchains Are Vulnerable

Bitcoin and Ethereum use **Elliptic Curve Digital Signature Algorithm (ECDSA)** to authorize transactions. The security assumption is that recovering a private key from a public key is computationally infeasible for classical computers. **Shor's algorithm** (1994) is a quantum algorithm that can solve the discrete logarithm problem — the mathematical foundation of ECDSA — in polynomial time.

A sufficiently powerful quantum computer running Shor's algorithm could:
1. Observe a Bitcoin address's public key (revealed when you *spend* from that address)
2. Derive the corresponding private key
3. Sign fraudulent transactions from that address

This is a concrete, well-defined threat — even if the timeline for a cryptographically capable quantum computer remains uncertain.

> Q: Not all Bitcoin addresses are equally vulnerable. A P2PK address exposes the public key permanently; a P2PKH address only exposes it on spend. Which is more quantum-resistant, and why?

## Where Quantum Computing Stands (2025)

The current era is **NISQ** — *Noisy Intermediate-Scale Quantum* — meaning quantum computers exist but are too error-prone and limited in qubit count for cryptographically relevant attacks.

**Google's Willow chip (December 2024)**: Google announced Willow solved a specific benchmark in under five minutes that would take the fastest classical supercomputer 10 septillion years. This is a milestone in *error correction* — a key barrier to fault-tolerant quantum computing (Google Quantum AI, 2024).

A subsequent 2026 paper by Google researchers (Babbush et al., 2026) provided updated resource estimates specifically targeting ECDSA-256 — the signature scheme used by Bitcoin and Ethereum. Their result is more concerning than earlier estimates: Shor's algorithm for this problem can be executed with fewer than 500,000 physical qubits on superconducting hardware, running in minutes. This is significantly tighter than the ~317 million physical qubit estimate from Webber et al. (2022), reflecting algorithmic improvements in circuit compilation. The paper also uses a zero-knowledge proof to validate results without disclosing the specific attack implementation — a responsible disclosure approach. Willow has ~105 qubits; 500,000 is still a large gap, but it has narrowed substantially.

Scientific consensus: a quantum computer capable of breaking Bitcoin's ECDSA is 10–20+ years away at minimum. The "harvest now, decrypt later" threat is more relevant to encrypted communications than to blockchain signatures, since blockchain signatures are single-use and already public.

## NIST Post-Quantum Cryptography Standards (2024)

NIST finalized three post-quantum cryptographic standards in August 2024:

| Standard               | Based On                        | Use Case                          |
| ---------------------- | ------------------------------- | --------------------------------- |
| **ML-KEM** (FIPS 203)  | Module Lattice (Kyber)          | Key encapsulation                 |
| **ML-DSA** (FIPS 204)  | Module Lattice (Dilithium)      | Digital signatures                |
| **SLH-DSA** (FIPS 205) | Stateless Hash-Based (SPHINCS+) | Digital signatures (conservative) |

These are designed to resist attacks from both classical and quantum computers. The challenge for blockchains is that signature schemes are embedded in data structures, address formats, and consensus protocols — migrating is a protocol-level upgrade, not a patch.

## What Needs to Change

Bitcoin is the most conservative case. Active proposals include:

- BIP-360 (P2QRH — Pay to Quantum Resistant Hash): A proposed new address type using hash-based signatures. Still in draft PR as of mid-2025; requires broad community consensus to activate.
- An estimated 4 million Bitcoin (in ~1.7 million addresses) sit in bare P2PK outputs — including Satoshi's coins. If quantum computers arrive before these migrate, those coins are at risk.

Ethereum has a more upgrade-agile governance model. Vitalik Buterin has proposed an emergency quantum-fork mechanism and Ethereum's account abstraction roadmap (EIP-7702) creates a cleaner migration path toward quantum-resistant signature schemes.

**No major blockchain has completed a migration to post-quantum cryptography as of 2025.**

> Q: Bitcoin's conservatism resists malicious changes — but also necessary upgrades. How should the community weigh this tradeoff for a quantum-resistance migration that must happen *before* the threat arrives?

---

# What did we miss?

* **Stablecoins in depth**: The mechanics of USDC (fiat-backed), DAI (crypto-collateralized), and failed algorithmic stablecoins like Terra/UST deserve a full lecture. They are the largest practical use of blockchain for money today.
* **DeFi regulation**: The SEC's enforcement actions against Uniswap, Coinbase, and others form a rapidly evolving legal landscape that will determine which parts of the DeFi ecosystem survive in regulated jurisdictions.
* **Bitcoin ETFs**: The approval of spot Bitcoin ETFs in the U.S. in January 2024 marked a watershed for institutional capital. The implications for price discovery and network ownership concentration are not yet fully understood.
* **Hash-based signatures**: SPHINCS+ and XMSS are quantum-resistant signature schemes that don't rely on lattice assumptions — a more conservative option for systems requiring long-term security.
* **Historical hyperinflation**: Two of the most studied cases of catastrophic monetary failure are the German Weimar Republic (1921–1923), where monthly inflation peaked at 29,500% — workers were paid twice daily so they could spend wages before prices rose — and Zimbabwe (2007–2009), where the government issued a 100 trillion dollar note before abandoning its currency entirely. Both cases have been used, correctly or not, as arguments for commodity-backed or fixed-supply money. See: [Weimar hyperinflation (Wikipedia)](https://en.wikipedia.org/wiki/Hyperinflation_in_the_Weimar_Republic) and [Zimbabwe hyperinflation (Wikipedia)](https://en.wikipedia.org/wiki/Hyperinflation_in_Zimbabwe).

# Exercises

1. 

# Further Reading

* [NIST Post-Quantum Cryptography Standards](https://csrc.nist.gov/projects/post-quantum-cryptography) — FIPS 203/204/205 documentation
* [BIP-360: Pay to Quantum Resistant Hash](https://github.com/cryptoquick/bips/blob/p2qrh/bip-0360.mediawiki) — Bitcoin's draft quantum-resistance proposal (draft PR, not yet merged to main bips repo)
* [Project Guardian](https://www.mas.gov.sg/schemes-and-initiatives/project-guardian) — MAS Singapore RWA tokenization pilot

## Supplementary

* [*How Quantum Computers Break Encryption* — 3Blue1Brown (YouTube)](https://www.youtube.com/watch?v=-UrdExQW0cs) — visual explanation of Shor's algorithm


# References

1. Babbush, R. et al. 2026. *Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations*. arXiv:2603.28846. [arXiv](https://arxiv.org/abs/2603.28846)
2. Atlantic Council. 2025. *CBDC Tracker*. [Web](https://www.atlanticcouncil.org/cbdctracker/)
3. Auer, R., Cornelli, G. & Frost, J. 2023. *Rise of the central bank digital currencies: drivers, approaches and technologies*. BIS Working Paper No. 880. [(pdf)](https://www.bis.org/publ/work880.pdf)
3. Federal Reserve. 2023. *Money Stock Measures — H.6 Release*. [Web](https://www.federalreserve.gov/releases/h6/)
4. Garratt, R. & van Oordt, M. 2021. *Privacy as a Public Good: A Case for Electronic Cash*. BIS Working Paper No. 905. [(pdf)](https://www.bis.org/publ/work905.pdf)
5. McKinsey & Company. 2024. *From ripples to waves: The transformational power of tokenizing assets*. [Web](https://www.mckinsey.com/industries/financial-services/our-insights/from-ripples-to-waves-the-transformational-power-of-tokenizing-assets)
6. NIST. 2024. *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*. [(pdf)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
7. NIST. 2024. *FIPS 204: Module-Lattice-Based Digital Signature Standard*. [(pdf)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
8. NIST. 2024. *FIPS 205: Stateless Hash-Based Digital Signature Standard*. [(pdf)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
9. Google Quantum AI. 2024. *Quantum error correction below the surface code threshold*. Nature, 638, 920–926. [DOI](https://doi.org/10.1038/s41586-024-08449-y)
10. Shor, P. W. 1994. *Algorithms for quantum computation: discrete logarithms and factoring*. FOCS 1994. [DOI](https://doi.org/10.1109/SFCS.1994.365700)
11. Webber, M. et al. 2022. *The impact of hardware specifications on reaching quantum advantage over classical simulation*. AVS Quantum Science, 4(1). [DOI](https://doi.org/10.1116/5.0073075)
12. World Economic Forum. 2024. *Tokenization of Real-World Assets: A Framework for Policymakers*. [Web](https://www.weforum.org/reports/tokenization-of-real-world-assets/)

# Video Lecture
* TBC

---

# Appendix: Property Glossary

Referenced from [above](#the-properties-of-money-revisited).

**Fungibility** — One unit is interchangeable with any other. A \$20 note has the same value as any other \$20 note. Gold is atomically indistinguishable. Bitcoin's fungibility is partial: early coinbase coins and coins from sanctioned addresses carry history that some exchanges refuse.

**Divisibility** — The ability to transact for goods of variable value. Fiat uses coins for small denominations. Bitcoin divides to 8 decimal places (1 satoshi = 0.00000001 BTC), enabling microtransactions impractical with physical money.

**Reliability** — The currency is available when needed. Digital fiat introduces outage risk dependent on state infrastructure. Decentralised networks are statistically reliable if nodes remain online; centralised systems can be destabilised by governance failure, attacks, or software bugs.

**Affordability** — Must be cheap enough to produce at scale but not so cheap that counterfeiting becomes attractive. Gold fails this: it is expensive to produce and physically impractical. Bitcoin's marginal cost of creating a *token* is zero; producing *a bitcoin* requires real computational expenditure (PoW).

**Physical** — Physical cash offers true bearer anonymity. All digital money sacrifices some form of this by design.

**Portability** — Digital assets are hyper-portable: the infrastructure to transmit \$1 is identical to that for \$1 billion. However, digital transfer requires network connectivity; in practice, physical cash is more portable in low-connectivity environments.

**Durability** — Value persists across time. Gold is chemically indestructible. Digital objects do not degrade, but their value depends on network survival — a dimension to which physical durability does not apply.

**Asset-backed** — Long-term stability requires something backing the currency if confidence fails. Gold and Bitcoin represent finite resources. The New Zealand dollar is backed only by a government promise. Bitcoin is also backed by the hardware, energy, and network infrastructure accumulated since 2009.

**Private / Anonymous** — Both cash and gold allow untracked transactions. Bitcoin is *pseudo-anonymous*: transactions are permanently linked by address. Anonymous cryptocurrencies (Monero via ring signatures; Zcash via zk-SNARKs) sacrifice efficiency for privacy.

**Censorable** — Whether a third party can block a specific transaction. Digital fiat is highly censorable by design. Bitcoin offers partial censorship resistance: miners or validators can technically exclude transactions, but doing so is economically costly and observable.

**Confiscatable** — The legal ability of a state to seize assets. Gold and bank deposits must comply with jurisdiction law. Cryptocurrency is a bearer asset: without the private key, it cannot be taken — absent coercion.

**Auditable / Transparent** — Bitcoin's open ledger allows any node to audit every transaction in history. Enterprise blockchains are typically not open. Fiat's ledger is opaque outside regulated reporting.

**Programmable** — Digital money can encode monetary policy at the protocol level: supply schedules, spending conditions, expiry. This is Bitcoin's block reward halving — and the CBDC spending restriction — as a feature rather than a bug.

**Decentralized** — True decentralization is difficult to achieve and maintain. Bitcoin and Ethereum are the primary candidates. All fiat systems are centralised by design.

**Anti-fragile** — Coined by Nassim Taleb: a system that gets stronger under attack. Since 2009, Bitcoin has been more reliably available than platforms maintained by the world's largest technology companies. Whether other blockchain projects share this property remains to be seen.
