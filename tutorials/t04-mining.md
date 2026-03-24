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
            elif log_mode == '1%':
                val = float(int(hash_result, 16))
                if val < 0.99 * float(local_best_val):
                    local_best_val = val
                    with shared_best_val.get_lock():
                        old_val = float(shared_best_val.value)
                        if val < 0.99 * old_val:
                            pct_str = "100.000" if old_val == float('inf') else f"{(old_val - val) / old_val * 100:.3f}"
                            shared_best_val.value = val
                            elapsed = time.time() - start_time
                            print(f" [Core {start_nonce:02d} | {elapsed:>8.2f}s] \U0001f4c9 {pct_str:>7}% Improvement! | Hash: {hash_result}")
            
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
4. **Periodic Target Synchronization**: To prevent cores from inefficiently chasing outdated targets for too long, the local caches are synchronized with the global best every 50,000 iterations.
5. **Randomized Salts**: Each worker process generates a random 4-byte hex salt to mix into its assigned base string. This completely eliminates the microscopic chance that two cores accidentally compute the same hash due to overlapping string concatenations.

### Sample Output
When you run the script, it will continue to output new findings until interrupted:

```text
Starting multi-core mining simulation using 11 parallel CPU cores...

Logging mode selected: 1% (Pass '16x' or '1%' as argument to change)

Mining indefinitely... Press Ctrl+C to stop.

------------------------------------------------------------
 [Core 00 |     0.14s] 📉 100.000% Improvement! | Hash: 2ac1c88ad27f2a386e76516b5f78532fa14a9db0a1e2f15f24e9be980e60e0d3
 [Core 00 |     0.14s] 📉   9.437% Improvement! | Hash: 26b8d5964145241848e6e33d33751c71acc7b6c749bce778fd0f3f37add076ab
 [Core 00 |     0.14s] 📉  45.260% Improvement! | Hash: 153251a9742d741fb3844b7b77d8d4772c53ee9b0fd341244014e387c4551888
 [Core 00 |     0.14s] 📉  13.521% Improvement! | Hash: 1254a06ad4756375a1f4087f61335a13b01c12c95e6c3bf61eb9c19d4be9635b
 [Core 00 |     0.14s] 📉  70.744% Improvement! | Hash: 055ce4d5f2e0bce6c933e1d1e9646c8588527c9f39bfc4c7f400a95cbfe09bd0
 [Core 00 |     0.14s] 📉  44.475% Improvement! | Hash: 02fa4e15dd27c44a9f68be85355adbda5406cdec501e5cb2e46ef4a9215f6e18
 [Core 00 |     0.14s] 📉  17.598% Improvement! | Hash: 0274271569127135cb5ea5f4154fda91342961fb0eeedae8041436541ec14e13
 [Core 00 |     0.14s] 📉  53.698% Improvement! | Hash: 0122d9634e899fd70efe7f77cb343ae09bf8f0512336d5e82b26b12e647c9ab5
 [Core 00 |     0.14s] 📉  94.234% Improvement! | Hash: 0010c54315ac8d984d667a9593357ba3ecc548dffef87885b80e4ec322b54e57
 [Core 00 |     0.14s] 📉  26.363% Improvement! | Hash: 000c59687d5d47f2f812c30c8f1c355784bea7eb76c3b764d72a1ebac5de11c1
 [Core 00 |     0.14s] 📉   3.772% Improvement! | Hash: 000be22a1db8cdcfd003f2118a83aa16fb0b7194d92b73cc90f1ae8cdf09e8da
 [Core 02 |     0.14s] 📉  17.315% Improvement! | Hash: 0009d367b0f7b102e095d1cc16c789977f0715884d1b7ba02a70dad0ace6578b
 [Core 04 |     0.15s] 📉  85.914% Improvement! | Hash: 00016252ddf592fbfd5b5fff95995755a2a3aa366ba076faca03c533f88a203d
 [Core 02 |     0.15s] 📉   2.213% Improvement! | Hash: 00015a7b594baf68d1a4c8019ed0a6f0d28b6bf87bc75d164950bfca173e952a
 [Core 09 |     0.16s] 📉  15.485% Improvement! | Hash: 000124d48105e175e436cc999f9f1f42c557c602f56c4aebc0c206bc95fc8560
 [Core 04 |     0.16s] 📉  65.002% Improvement! | Hash: 0000667c6dba22ccac760b5f98bdc78b4eded6dda3eebedaa65279487412dcee
 [Core 03 |     0.17s] 📉  76.050% Improvement! | Hash: 0000188b85f21241abd6c9141cc5370d54fc04d17450b362a6901e6b80d0473d
 [Core 10 |     0.22s] 📉  37.229% Improvement! | Hash: 00000f684201ff81f43bd32c40f03c07e0a44c2a654d583fbd0e143ecd56a026
 [Core 02 |     0.22s] 📉  87.938% Improvement! | Hash: 000001dbc386de80b64046005e4f2c8e7587f5b7be6972c7ff0496c2c6e4930d
 [Core 04 |     0.99s] 📉  27.367% Improvement! | Hash: 000001598fc2944c647a9041d03f4362bf1a806e6f8c23fe76f68a9ea649b60e
 [Core 10 |     1.65s] 📉  41.186% Improvement! | Hash: 000000cb3d512c799c8db0d2d41eebb1caef388c4b5b5c64622a5e3364912efa
 [Core 03 |     1.79s] 📉  50.663% Improvement! | Hash: 000000644578b104d96513b2ee60ceeee7bf791839ae12bcebd6ae8799d40be3
 [Core 06 |     6.02s] 📉  15.144% Improvement! | Hash: 000000551636f895f245e3ba2a20e5cb5bfe31a6d8cb802a94b9ae35a3bc0c90
 [Core 01 |     8.43s] 📉   7.789% Improvement! | Hash: 0000004e758331237fd6614cb7e1e8701a2425041bf2fb7346bf178158dd4df8
 [Core 09 |     9.75s] 📉  54.585% Improvement! | Hash: 00000023a1dc8a47e2c315120fe7274bd5c57457832e9b7c1a032d34f68373bf
 [Core 05 |    12.26s] 📉  98.179% Improvement! | Hash: 00000000a61d1c8a042885906e0d4ebd4bf0068c5dfc51bcaa6b3d90f522a70e

\U0001f6d1 Mining interrupted by user. Shutting down worker cores...
Shutdown complete.
```
