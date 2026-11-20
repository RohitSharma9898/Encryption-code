from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# 1. Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 2. Generate the public key
public_key = private_key.public_key()


# 3. Create the original message
message = b"Hello Students"

print("Original Message:", message)


# 4. Encrypt the message using the PUBLIC key
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nEncrypted Message:")
print(encrypted_message)


# 5. Decrypt the message using the PRIVATE key
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nDecrypted Message:")
print(decrypted_message.decode())