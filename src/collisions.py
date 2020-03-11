import random

def how_many_before_collsion(buckets, loops=1): 
    """
    roll random hash indexes into buckets and print how many rolls before a collision 
    """

    for i in range(loops):
        tries = 0
        tried = set()
    
        tried_list = []

        while True: 
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried: 
                tried.add(hash_index)
                tries += 1
            
            else: 
                break
        print(f"{buckets} buckets, {tries} hashes before collision. {tries/buckets * 100:.1f}%")

how_many_before_collsion(100,10)