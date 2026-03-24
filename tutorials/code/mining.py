import hashlib
import time

def mine(difficulty):
    # The target prefix of leading zeroes we are looking for
    prefix = '0' * difficulty
    nonce = 0
    start_time = time.time()
    
    # We use a simple base string for our 'block' data
    base_text = "COMP842_Mining_Simulation_" 
    
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
    # Loop through difficulties 1 to 15
    for i in range(1, 15):
        mine(i)
