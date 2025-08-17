import hashlib

hash_input = input("Enter the hash to crack: ")
wordlist = input("Enter path to wordlist: ")

with open(wordlist, "r") as file:
    for line in file:
        word = line.strip()
        if hashlib.md5(word.encode()).hexdigest() == hash_input:
            print(f"[+] Password found: {word}")
            break
    else:
        print("[!] Password not found in list.")