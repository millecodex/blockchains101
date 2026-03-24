import hashlib
import time
import multiprocessing as mp

def mine_worker(start_nonce, step, log_mode, shared_best_zeros, shared_best_val, start_time):
    nonce = start_nonce
    base_text = "COMP842_Mining_Simulation_" 
    
    # Track local bests for logging
    local_best_zeros = int(shared_best_zeros.value)
    local_best_val = float(shared_best_val.value)
    
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
                            print(f" [Core {start_nonce:02d} | {elapsed:.2f}s] 🚀 16x Improvement (Zeros: {zeros}) | Hash: {hash_result}")
            elif log_mode == '1%':
                val = float(int(hash_result, 16))
                if val < 0.99 * float(local_best_val):
                    local_best_val = val
                    with shared_best_val.get_lock():
                        if val < 0.99 * float(shared_best_val.value):
                            shared_best_val.value = val
                            elapsed = time.time() - start_time
                            print(f" [Core {start_nonce:02d} | {elapsed:.2f}s] 📉 1% Improvement! | Hash: {hash_result}")
            
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
        print("\n🛑 Mining interrupted by user. Shutting down worker cores...")
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
