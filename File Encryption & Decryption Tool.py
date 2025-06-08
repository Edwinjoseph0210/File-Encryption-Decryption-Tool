"""
File Encryptor/Decryptor using Fernet symmetric encryption.

Requirements:
pip install cryptography

Usage:
- Run script.
- Choose encrypt/decrypt.
- Provide file path and key (generate key once).

"""

from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    print("Generated Key:", key.decode())
    return key

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", 'wb') as file:
        file.write(encrypted)
    print(f"File encrypted as {filename}.enc")

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        data = file.read()
    decrypted = f.decrypt(data)
    output_file = filename.replace(".enc", ".dec")
    with open(output_file, 'wb') as file:
        file.write(decrypted)
    print(f"File decrypted as {output_file}")

def main():
    print("File Encryptor/Decryptor")
    print("1. Generate Key\n2. Encrypt File\n3. Decrypt File")
    choice = input("Choose option: ")

    if choice == '1':
        generate_key()
    elif choice == '2':
        filename = input("File to encrypt: ")
        key = input("Enter key: ").encode()
        encrypt_file(filename, key)
    elif choice == '3':
        filename = input("File to decrypt: ")
        key = input("Enter key: ").encode()
        decrypt_file(filename, key)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
