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

It removes the concept of an arbitrary target, running indefinitely. You can choose whether to log improvements every time the leading zeroes increment (`16x` argument) or when the numeric value drops at least 1% (`1%` default).

```python
import hashlib
import time
import multiprocessing as mp

def mine_worker(start_nonce, step, log_mode, shared_best_zeros, shared_best_val, start_time):
    nonce = start_nonce
    base_text = "COMP842_Mining_Simulation_" 
    
    # Track local bests for logging
    local_best_zeros = shared_best_zeros.value
    local_best_val = shared_best_val.value
    
    # Run indefinitely
    while True:
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
                            print(f" [Core {start_nonce:02d} | {elapsed:.2f}s] \U0001f680 16x Improvement (Zeros: {zeros}) | Hash: {hash_result}")
            elif log_mode == '1%':
                val = int(hash_result, 16)
                if val < 0.99 * local_best_val:
                    local_best_val = val
                    with shared_best_val.get_lock():
                        if val < 0.99 * shared_best_val.value:
                            shared_best_val.value = float(val)
                            elapsed = time.time() - start_time
                            print(f" [Core {start_nonce:02d} | {elapsed:.2f}s] \U0001f4c9 1% Improvement! | Hash: {hash_result}")
            
            nonce += step

def mine_multicore(num_cores, log_mode='1%'):
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
    
    mode = '1%'
    if len(sys.argv) > 1 and sys.argv[1] == '16x':
        mode = '16x'
        
    print(f"Logging mode selected: {mode} (Pass '16x' or '1%' as argument to change)\n")
    
    mine_multicore(cores, log_mode=mode)
```

### Explanation of Multicore Implementation
1. **Shared State (`mp.Value`)**: Since each core has its own isolated memory space, typical variables aren't shared. We use `mp.Value` memory locks to track the global `shared_best_zeros` and `shared_best_val`, allowing threads to continuously chase the absolute lowest hash.
2. **Infinite Runtime (`while True`)**: The main process blocks on `for p in processes: p.join()` while the individual workers loop endlessly. It relies on a `try / except KeyboardInterrupt` to gracefully cancel the operation when `Ctrl+C` is pressed.
3. **Local Caching for Speed**: To maintain high throughput and avoid excessive lock contention, each core checks the mathematical `< 0.99` threshold on its local cached copy *first*. Only if it succeeds does it fetch the costly `get_lock()` to verify if it is a true global improvement.

### Sample Output
When you run the script, it will continue to output new findings until interrupted:

```text
Starting multi-core mining simulation using 11 parallel CPU cores...

Logging mode selected: 1% (Pass '16x' or '1%' as argument to change)

Mining indefinitely... Press Ctrl+C to stop.

------------------------------------------------------------
 [Core 00 | 000.13s] 📉 1% Improvement! | Hash: 9fa5fe0c87706be9d7a7e3e2649d336e14eea5b703f04d272c009e7b51990bf8
 [Core 00 | 000.13s] 📉 1% Improvement! | Hash: 23a148f1512a1e7221d92db32b6e8f5267e38689c38ae164181cfa359a3bc8e4
 [Core 00 | 000.13s] 📉 1% Improvement! | Hash: 09222c810be99f89e2e7c1aa7c5600182a037758f97a7556a35e7559d6c4e916
 [Core 00 | 000.13s] 📉 1% Improvement! | Hash: 07a947b62b0570d8d087fb8432aef379797cc8e07061c0a2598ac1a6fac5dcb5
 [Core 00 | 000.13s] 📉 1% Improvement! | Hash: 0535c9ed92f607b33f136780dddb6e7d1b155a5fdb03921742f838afd87e30be
 [Core 00 | 000.13s] 📉 1% Improvement! | Hash: 00608a854b251e2b19aa6d9b3273618a5e49b7711241ec47cfaadf7dc0b9e0ba
 [Core 01 | 000.13s] 📉 1% Improvement! | Hash: 001428f2fb657f89f2122ab2b7aa546588a6b262d3a2df51f3703c5eff6638fb
 [Core 01 | 000.13s] 📉 1% Improvement! | Hash: 0006da180b134e8a9248a231d1271bdf34f8ab9fabe34bc3a3399b28986f1399
 [Core 01 | 000.14s] 📉 1% Improvement! | Hash: 00067ef0abe68da15586b3a47d9823db777713db32bececa1729ba48bb8f910c
 [Core 01 | 000.14s] 📉 1% Improvement! | Hash: 000439537bc6d4be4fae97428d43fe4fa5e685e6c632542caffc7fc40bf90837
 [Core 02 | 000.15s] 📉 1% Improvement! | Hash: 000055d2aed2376f959c0468721915b100b47948c0bcd93efe34f8b2fc079287
 [Core 03 | 000.15s] 📉 1% Improvement! | Hash: 00002461e4a3dcd7cf3ab2d185fcf1fc9232fc712eefaf2c62b8f420e8284ced
 [Core 05 | 000.21s] 📉 1% Improvement! | Hash: 000018e806ce3cee449f6fc0a0f02708646efdebef4284604147ce533f443e58
 [Core 00 | 000.29s] 📉 1% Improvement! | Hash: 00000ab96ef29be2104d64a765fe53ba2af67aece6fef6e363a44dc0436cf39e
 [Core 02 | 000.42s] 📉 1% Improvement! | Hash: 00000a1b3b9662ca5f2461da649305a70318ea5b7bf8e4460d03df1ffdfdda2e
 [Core 03 | 000.73s] 📉 1% Improvement! | Hash: 00000916584e7e12a1dbd848d3bd00dcee9497aa2fb95cd80bc794a28182a7f0
 [Core 05 | 001.09s] 📉 1% Improvement! | Hash: 000004a547252cb6335a216eb068cce6b49bdaebb724acc555bc2db284935551
 [Core 02 | 001.16s] 📉 1% Improvement! | Hash: 000000d87d1bbac7e3f832a42a3854d4ee55f459401f63c85fcf8b652e9e8f88
 [Core 09 | 006.18s] 📉 1% Improvement! | Hash: 000000c13fb53de0d57646812075e147351f29b32f83a5185ce266267ad8f685
 [Core 08 | 006.67s] 📉 1% Improvement! | Hash: 0000007a05761cc59cedd225f69bc070de42705ffcb93c049af71c26ac81d28d
 [Core 10 | 007.89s] 📉 1% Improvement! | Hash: 0000000859bafc5c25544d7b75495a26ec4846702f9146793689745b17f91340
 [Core 04 | 070.70s] 📉 1% Improvement! | Hash: 0000000717f1764f7aaace41f438f74caeeafb304bc178da603383c5f9d85250
 [Core 06 | 100.39s] 📉 1% Improvement! | Hash: 0000000403bccf9ca99bd80fcd1a0c8d7ee1a0b969f5e0e64d5832a073b4c17b
 [Core 06 | 120.59s] 📉 1% Improvement! | Hash: 00000001080f435982aa037ae9b0a03e33e2217c92429af832f2f204a9deb682

\U0001f6d1 Mining interrupted by user. Shutting down worker cores...
Shutdown complete.
```
