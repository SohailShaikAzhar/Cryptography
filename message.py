import os

def token_bytes(nbytes=None):    # Generates nbytes cryptographic random bytes[1]
    if nbytes is None:
        nbytes = 32
    return os.urandom(nbytes)


#Sender side message
message = input("Enter the text you want to send")    
# Generating an secrect key from user side
user_key = token_bytes(64)


# Encryption

# Generating a unique Key for each character
encryption_map = {}  
for i in message:
    # Generate a random 16-byte key for this character
    char_key = token_bytes(16).hex()
    # Stores the character with its key
    encryption_map[char_key] = i

# Extract the keys
keys = list(encryption_map.keys())

# Converting hexa decimal keys to decimal number
num_keys = []
for i in keys:
    num_keys.append(int(i, 16))

# Encrypt each character using its key
encrypted_message = []
for char in message:
    # Find the key for this character
    char_key = None
    for key, value in encryption_map.items():
        if value == char:
            char_key = key
            break
    
    if char_key:
        # Convert to numeric value
        key_num = int(char_key, 16)
        # Use the last byte as XOR key
        key_byte = key_num & 0xFF
        # Encrypt the character
        encrypted_val = ord(char) ^ key_byte
        encrypted_hex = hex(encrypted_val)[2:] #Remove '0x' prefix
        encrypted_message.append(encrypted_hex)
    
#       print(f"Encrypted '{char}' (ASCII {ord(char)}) with key byte {key_byte} to: {encrypted_hex}")

# print("\nFinal Encrypted Message (hex):", " ".join(encrypted_message))

# Format the encrypted message as a space-separated hexadecimal string
sending_cipher_txt = ' '.join(encrypted_message)

# print("\nFinal Encrypted Message:")
# print(sending_cipher_txt)

# Converting hex to binary 
binary_string = ' '.join(format(ord(char), '08b') for char in sending_cipher_txt)
print(binary_string)
