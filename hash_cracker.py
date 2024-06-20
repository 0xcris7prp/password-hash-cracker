import hashlib
import pyfiglet

banner = pyfiglet.figlet_format("Falcon's \n MD5 Hash Cracker")
print(banner)

wordlist_location = str(input("Give path of wordlist: "))
hash_input = str(input("Enter hash value to crack: "))

with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hashlib.sha256(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print("Found cleartext password: " + line.strip())
            exit(0)

