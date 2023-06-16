from cryptography.fernet import Fernet
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Gud Baldr")
print(ascii_banner)

def generate_key():
    """Generate a new encryption key"""
    return Fernet.generate_key()

def encrypt_message(key, message):
    """Encrypt a message using the provided key"""
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    """Decrypt an encrypted message using the provided key"""
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()

def validate_key(key):
    """Validate the encryption key"""
    try:
        Fernet(key)
        return True
    except (ValueError, TypeError):
        return False

# Generate a new encryption key
key = generate_key()
print("Generated encryption key:", key.decode())

# Encrypt a message
message = input("Enter a message to encrypt: ")
encrypted_message = encrypt_message(key, message)
print("Encrypted message:", encrypted_message.decode())

# Decrypt the encrypted message
key_input = input("Enter the encryption key to decrypt the message: ")
if validate_key(key_input.encode()):
    decrypted_message = decrypt_message(key_input.encode(), encrypted_message)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid encryption key.")