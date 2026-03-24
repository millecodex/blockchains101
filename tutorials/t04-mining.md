# Tutorial 4: Simple Proof of Work Mining Simulation

## Description
This tutorial provides a simple Python script to simulate the Proof of Work (PoW) consensus mechanism used by networks like Bitcoin. The goal of PoW is to find a cryptographic hash—in this case using `SHA256`—that meets a certain difficulty target. Here, the difficulty is represented by the number of leading zeroes in the resulting hexadecimal hash. 

As the required number of leading zeroes increases by 1, the difficulty increases by a factor of 16 ($16^1$), meaning it takes exponentially more time and computational power to find a valid hash. You can run this script locally on your machine to test its processing capability!

## The Mining Script (`mining.py`)
Copy the following code into a file named `mining.py` and run it using Python. It will automatically attempt to find hashes with 1 to 5 leading zeroes.

```python
import hashlib
import time

def mine(difficulty):
    # The target prefix of leading zeroes we are looking for
    prefix = '0' * difficulty
    nonce = 0
    start_time = time.time()
    
    # We use a simple base string for our 'block' data
    base_text = "Jeff_plus_one_million_coins" 
    
    while True:
        # Combine the base text with the current nonce
        text = f"{base_text}{nonce}"
        
        # Calculate the SHA256 hash of the combined string
        hash_result = hashlib.sha256(text.encode('utf-8')).hexdigest()
        
        # Check if the hash meets the difficulty target
        if hash_result.startswith(prefix):
            elapsed_time = time.time() - start_time
            print(f"Difficulty: {difficulty}")
            print(f"Nonce: {nonce}")
            print(f"Proof-of-work: {hash_result}")
            print(f"Elapsed time: {elapsed_time}\n")
            return
            
        nonce += 1

if __name__ == "__main__":
    print("Starting mining simulation...\n")
    # Loop through difficulties 1 to 5
    for i in range(1, 6):
        mine(i)
```

## Sample Output
When you run the script, your output will look similar to this. Notice how the elapsed time increases exponentially as the difficulty goes up!

```text
Difficulty: 1
Nonce: 43
Proof-of-work: 05b7e096306a10c850cd8fe6bf55b1cc97365538cadbe3dc89e1216298275a69
Elapsed time: 0.0009968280792236328

Difficulty: 2
Nonce: 22
Proof-of-work: 002fcd61b3f3188e0f7fdff849e8dd3ee5805a34e06f4c6a8fd4fb86d4577350
Elapsed time: 0.005983591079711914

Difficulty: 3
Nonce: 12489
Proof-of-work: 0003124c9428d9a1c6f2ef0a782a044bcfde374cf6dfef414b161f8594377246
Elapsed time: 0.7731056213378906

Difficulty: 4
Nonce: 224827
Proof-of-work: 0000d66a2b464413b4af3b52ffef44a714ced1c06a4471c389755bf2eca19cef
Elapsed time: 239.61160159111023

Difficulty: 5
Nonce: 1230021
Proof-of-work: 000004ab089b08c3ceed5622dbe1ea0a3d621295379d107707cf2b8f9ffc9098
Elapsed time: 8363.934648275375
```

## Multicore Mining Script (`mining_multicore.py`)
To utilize the full processing power of your machine, you can split the search space across multiple CPU cores. This script uses the `multiprocessing` library to safely share global state and record the highest improvements found by any thread!

It removes the concept of an arbitrary target, running indefinitely. You can choose whether to log improvements every time the leading zeroes increment (`16x` argument) or when the numeric value drops at all (`any` default).

```python
import hashlib
import time
import multiprocessing as mp
import os

def mine_worker(start_nonce, step, log_mode, shared_best_zeros, shared_best_val, start_time):
    nonce = start_nonce
    salt = os.urandom(4).hex()
    base_text = f"Jeff_gets_1_million_coins_{salt}_" 
    
    # Track local bests for logging
    local_best_zeros = int(shared_best_zeros.value)
    local_best_val = float(shared_best_val.value)
    
    # Run indefinitely
    while True:
        # Periodically sync local targets with the global best to avoid stale goals
        local_best_zeros = max(local_best_zeros, int(shared_best_zeros.value))
        local_best_val = min(local_best_val, float(shared_best_val.value))

        # Inner loop runs hot without checking shared memory
        for _ in range(50000):
            text = f"{base_text}{nonce}"
            hash_result = hashlib.sha256(text.encode('utf-8')).hexdigest()
            
            # --- Pretty print logging ---
            if log_mode == '16x':
                zeros = len(hash_result) - len(hash_result.lstrip('0'))
                if zeros > local_best_zeros:
                    local_best_zeros = zeros
                    with shared_best_zeros.get_lock():
                        if zeros > shared_best_zeros.value:
                            shared_best_zeros.value = zeros
                            elapsed = time.time() - start_time
                            print(f" [Core {start_nonce:02d} | {elapsed:>8.2f}s] \U0001f680 16x Improvement (Zeros: {zeros}) | Hash: {hash_result}")
            elif log_mode == 'any':
                val = float(int(hash_result, 16))
                if val < float(local_best_val):
                    local_best_val = val
                    with shared_best_val.get_lock():
                        old_val = float(shared_best_val.value)
                        if val < old_val:
                            pct_str = "100.000" if old_val == float('inf') else f"{(old_val - val) / old_val * 100:.3f}"
                            shared_best_val.value = val
                            elapsed = time.time() - start_time
                            print(f" [Core {start_nonce:02d} | {elapsed:>8.2f}s] \U0001f4c9 {pct_str:>7}% Improvement! | Hash: {hash_result}")
            
            nonce += step

def mine_multicore(num_cores, log_mode='any'):
    start_time = time.time()
    
    shared_best_zeros = mp.Value('i', -1)
    shared_best_val = mp.Value('d', float('inf'))
        
    processes = []
    
    print("Mining indefinitely... Press Ctrl+C to stop.\n")
    print("-" * 60)
    
    try:
        # Spin up an independent process for each CPU core
        for i in range(num_cores):
            p = mp.Process(target=mine_worker, args=(i, num_cores, log_mode, shared_best_zeros, shared_best_val, start_time))
            processes.append(p)
            p.start()
            
        # Block forever until interrupted
        for p in processes:
            p.join()
            
    except KeyboardInterrupt:
        print("\n\U0001f6d1 Mining interrupted by user. Shutting down worker cores...")
        for p in processes:
            p.terminate()
            p.join()
        print("Shutdown complete.")

if __name__ == "__main__":
    import sys
    cores = mp.cpu_count()
    print(f"Starting multi-core mining simulation using {cores} parallel CPU cores...\n")
    
    mode = 'any'
    if len(sys.argv) > 1 and sys.argv[1] == '16x':
        mode = '16x'
        
    print(f"Logging mode selected: {mode} (Pass '16x' or 'any' as argument to change)\n")
    
    mine_multicore(cores, log_mode=mode)
```

### Explanation of Multicore Implementation
1. **Shared State (`mp.Value`)**: Since each core has its own isolated memory space, typical variables aren't shared. We use `mp.Value` memory locks to track the global `shared_best_zeros` and `shared_best_val`, allowing threads to continuously chase the absolute lowest hash.
2. **Infinite Runtime (`while True`)**: The main process blocks on `for p in processes: p.join()` while the individual workers loop endlessly. It relies on a `try / except KeyboardInterrupt` to gracefully cancel the operation when `Ctrl+C` is pressed.
3. **Local Caching for Speed**: To maintain high throughput and avoid excessive lock contention, each core checks the mathematical `<` threshold on its local cached copy *first*. Only if it succeeds does it fetch the costly `get_lock()` to verify if it is a true global improvement.
4. **Periodic Target Synchronization**: To prevent cores from inefficiently chasing outdated targets for too long, the local caches are synchronized with the global best every 50,000 iterations.
5. **Randomized Salts**: Each worker process generates a random 4-byte hex salt to mix into its assigned base string. This completely eliminates the microscopic chance that two cores accidentally compute the same hash due to overlapping string concatenations.

### Sample Output
When you run the script, it will continue to output new findings until interrupted:

```text
Starting multi-core mining simulation using 11 parallel CPU cores...

Logging mode selected: any (Pass '16x' or 'any' as argument to change)

Mining indefinitely... Press Ctrl+C to stop.

 [Core 01 |     0.27s] 📉  34.533% Improvement! | Hash: 21d325b6a008ac8853057fe79a623e611b1ffa720b990b37b9e272d1151bfe14
 [Core 02 |     0.27s] 📉  69.553% Improvement! | Hash: 0a4c7615e26e12d37a9bc47fa07d6baa0f712d789dd4e08bd860190d7f48b406
 [Core 02 |     0.27s] 📉  74.945% Improvement! | Hash: 029493262346e551086e465033b87d5bc25c734c1c1eee22dbc6ba306fee2285
 [Core 02 |     0.27s] 📉  64.301% Improvement! | Hash: 00ebd0ffe263ebc7f725bd88c1240d14f66dfc87f50152fa0f595fb3b2a08d47
 [Core 01 |     0.27s] 📉   0.208% Improvement! | Hash: 00eb5394dadbbf717f8d8b2bbcf496cf2912baf4ef42e278319326f472bd81a5
 [Core 01 |     0.27s] 📉  51.477% Improvement! | Hash: 00722ff53becdedeba04bebe4df01e8c3e31e8254bddbbb1aaa69ec5920b82ae
 [Core 01 |     0.27s] 📉   0.088% Improvement! | Hash: 0072165f961dc7033e0013850c82009f327b1a453cf9520b70ad6526776e4d6c
 [Core 02 |     0.27s] 📉  88.163% Improvement! | Hash: 000d812b9f37278c65e264754f8080c7f7b840db92e0cab1bb750be4dfded482
 [Core 02 |     0.27s] 📉  66.472% Improvement! | Hash: 0004871c853f917825b06c887c6741d6db123ffaf97a9ae060b453da7d4b161c
 [Core 01 |     0.27s] 📉  58.750% Improvement! | Hash: 0001de211f3b68894fca3404d562eb756dd0e90ac07600555fb5a09c8ecd3bd2
 [Core 00 |     0.28s] 📉  55.929% Improvement! | Hash: 0000d2b7d3b17dc71d31570979f3aa801ceac9ea82a5f5f260352fc6fa2db722
 [Core 01 |     0.28s] 📉   7.649% Improvement! | Hash: 0000c299dcd505f0fd6f347d0046de16a2c864a549d2bb5a435d97e059529147
 [Core 02 |     0.30s] 📉  42.090% Improvement! | Hash: 000070b15da6488d06cfc26f4c4e1ae4b46c74472a30e43a36bf0fda9f894146
 [Core 02 |     0.30s] 📉  63.639% Improvement! | Hash: 000028f9c6667a3276511521cf09af4e07444c36a31c743f74473bec743643da
 [Core 07 |     0.49s] 📉  74.139% Improvement! | Hash: 00000a98b7b1fdcfd63422b58e7caa9dc35a4b2ff0f688167220c0e86ea7c147
 [Core 10 |     1.00s] 📉  28.644% Improvement! | Hash: 0000078fadca990a6a59de17280b2259b7efb8d0102faec5b0b3a28ca7e132eb
 [Core 10 |     1.75s] 📉  61.386% Improvement! | Hash: 000002eb712574738b200965545bf432235c02d725ed04a93a65c39a5d539e17
 [Core 06 |     2.05s] 📉  22.120% Improvement! | Hash: 000002461b728c9daf9cd915f1cc7f60e55b0e587c86681d5e3f3fbca8ee661e
 [Core 04 |     2.85s] 📉  47.851% Improvement! | Hash: 0000012f8faad9fb76de446b4921d57a512c2344e194cb533bf2560b8220ac69
 [Core 10 |     4.68s] 📉  85.815% Improvement! | Hash: 0000002b0f6c34ed55d53594e4252de5c016c11f0e7fafd45a16e29fef7e3d3c
 [Core 00 |    56.00s] 📉  38.236% Improvement! | Hash: 0000001a9887dbef895bd5f43532ed0d6404e353f9b35b95280217f538c3436f
 [Core 01 |    75.45s] 📉  15.167% Improvement! | Hash: 000000168fe9f73ea3516a79ae178e2ae72d3b09d7a4673c1c34c3edb018eba8
 [Core 07 |    99.77s] 📉  84.571% Improvement! | Hash: 000000037b24d08e8dcf3185753e76f25c743f7bab27faf19faffaa022e257db
 [Core 06 |   314.73s] 📉  87.334% Improvement! | Hash: 0000000070de4c8f096e8c1c688cacda5dfa023ecaf6a5d868ece0cbb55836b2
 [Core 01 |   755.95s] 📉  23.127% Improvement! | Hash: 0000000056c3cfc49310cd4ad2354da538f6e29aeadb7ea09aa00dde9baa2b09
 [Core 06 |  1861.90s] 📉  65.443% Improvement! | Hash: 000000001dfbb8492152054fd4bba22f0a44a263372dcbde9917d567cd458af7
 [Core 01 |  2227.18s] 📉   9.911% Improvement! | Hash: 000000001b02f61f37c0c98f4fe9fe74414d2e3780046736f7ec431a3412ae48
 [Core 01 |  7341.18s] 📉  50.123% Improvement! | Hash: 000000000d78f15b56e5e792c37a67ae0aab4d43445f78fb1f9863a46da5d4da
 [Core 02 | 10014.35s] 📉  68.873% Improvement! | Hash: 0000000004319071c0f5843087abd17ee3ea8b623d0a5a5c981c449ff26995a3

\U0001f6d1 Mining interrupted by user. Shutting down worker cores...
Shutdown complete.
```
