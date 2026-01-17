"""
Brute Force Password Cracking Demo
Author: Your Name
Purpose: Educational cybersecurity project

This script demonstrates how brute-force attacks work
against a hashed password in a controlled environment.
"""

import hashlib

# Target password hash (SHA-256 of 'password123')
TARGET_HASH = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force(wordlist_path):
    try:
        with open(wordlist_path, "r") as file:
            for password in file:
                password = password.strip()
                hashed = hash_password(password)

                print(f"Trying: {password}")

                if hashed == TARGET_HASH:
                    print("\n[✔] Password Found:", password)
                    return
        print("\n[✘] Password not found in wordlist.")
    except FileNotFoundError:
        print("Wordlist not found.")

if __name__ == "__main__":
    brute_force("passwords.txt")
