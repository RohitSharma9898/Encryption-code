from cryptography.fernet import Fernet

# Generate secret key
key = Fernet.generate_key()

print("Secret Key:", key)

# Create encryption object
cipher = Fernet(key)

# Original message
message = b"Hello Students"

print("Original:", message)

# Encrypt
encrypted = cipher.encrypt(message)

print("Encrypted:", encrypted)

# Decrypt
decrypted = cipher.decrypt(encrypted)

print("Decrypted:", decrypted.decode())