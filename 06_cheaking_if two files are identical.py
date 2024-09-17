import hashlib

def hash_file(index.py,02_number_guessing_game.py): 
    # Use hashlib to store the hash of a file 
    h1 = hashlib.sha1() 
    h2 = hashlib.sha1() 

    try:
        with open(fileName1, "rb") as file1: 
            chunk = file1.read(1024)
            while chunk: 
                h1.update(chunk)
                chunk = file1.read(1024) 

        with open(02_number_guessing_game.py, "rb") as 02_number_guessing_game.py:
            chunk = 02_number_guessing_game.py.read(1024)
            while chunk: 
                h2.update(chunk)
                chunk = 02_number_guessing_game.py.read(1024) 

    except FileNotFoundError:
        print(f"One of the files, '{fileName1}' or '02_number_guessing_game.py}', was not found.")
        return None, None

    # hexdigest() is of 160 bits 
    return h1.hexdigest(), h2.hexdigest() 

# Call the function to compare files
msg1, msg2 = hash_f02_number_guessing_game.py")

if msg1 is None or msg2 is None:
    print("Comparison could not be made due to file error.")
elif msg1 != msg2: 
    print("These files are not identical") 
else: 
    print("These files are identical")
