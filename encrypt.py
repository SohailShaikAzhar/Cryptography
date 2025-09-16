import os

def token_bytes(nbytes=None):
    """
    Generates cryptographically secure random bytes.
    
    Args:
        nbytes (int, optional): Number of bytes to generate. Defaults to 32.
    
    Returns:
        bytes: Random bytes of specified length
    """
    if nbytes is None:
        nbytes = 32
    return os.urandom(nbytes)

def main():
    """
    Main encryption function that processes user input through a custom encryption algorithm.
    """
    # Get input message from user
    message = input("Enter the text you want to send: ")    
    
    # Generate a cryptographic secret key
    user_key = token_bytes(16)
    key_hex = user_key.hex()
    key_num = int(key_hex, 16)
    key_num = str(key_num)

    # Split the key into two halves for dual-phase encryption
    first_half_encryption = ''
    second_half_encryption = ''

    for i, val in enumerate(key_num):
        # Divide digits into odd and even positions
        if i % 2 == 0:
            first_half_encryption += str(val)
        elif i % 2 == 1:
            second_half_encryption += str(val)

    # Combine both halves to form the final key
    final_key = str(first_half_encryption) + str(second_half_encryption)

    # Encryption Process
    
    # Create a unique mapping for each character to a random key
    encryption_map = {}  
    for char in message:
        # Generate a random 4-byte key for this character
        char_key = token_bytes(4).hex()
        # Store the character's ASCII value with its unique key
        encryption_map[char_key] = str(ord(char))

    # Prepare for encryption processing
    map_keys = list(encryption_map.keys())
    map_values = list(encryption_map.values())

    ''' To remove the ambiguity from the code when a key generates 0 in the start
        I have removed the value starts with 0 and then creates a new key until it dosen't starts with 0
    '''
    map_key = []

    for i in map_keys:
        if str(i[0]) == "0":
            new_value = str(token_bytes(4).hex())
            while new_value[0] == "0":
                new_value = str(token_bytes(4).hex())
            map_key.append(new_value)
        else:
            map_key.append(i)

    map_keys = map_key

    # Combine keys and values for each character
    encrypted_text = []
    for i in range(len(map_keys)):
        encrypted_text.append(str(map_keys[i]) + str(map_values[i]))

    # Convert combined values to integers
    for i in range(len(encrypted_text)):
        encrypted_text[i] = int(encrypted_text[i], 16)

    # Apply dual-phase encryption using the split key
    cipher_text = []
    midpoint = len(encrypted_text) / 2
    for i in range(len(encrypted_text)):
        if i <= midpoint:
            cipher_text.append(int(first_half_encryption) + int(encrypted_text[i]))
        else:
            cipher_text.append(int(second_half_encryption) + int(encrypted_text[i]))

    # Convert encrypted values to binary representation
    binary_list = [bin(x)[2:] for x in cipher_text]
    binary_block = ''.join(binary_list)
    
    # Output the final encrypted data
    print(f"Your final encrypted data is: {binary_block}\nYour key is {final_key}")

if __name__ == "__main__":
    main()
