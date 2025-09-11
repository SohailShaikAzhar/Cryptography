import os

def decrypt_message(binary_block, final_key):
    """
    Decrypts a binary block using the provided final key.
    
    Args:
        binary_block (str): The encrypted binary data
        final_key (str): The key used for encryption
    
    Returns:
        str: The decrypted original message
    """
    # DECRYPTION PROCESS
    print("Starting decryption process...")
    
    # First, we need to determine the original binary chunk size
    # Since we don't know it, we'll try to find a divisor that makes sense
    # For this specific encryption, chunks are likely to be consistent in size
    
    # Find a reasonable chunk size (this is a workaround since we don't store the original size)
    possible_chunk_sizes = []
    for n in range(16, 65):  # Try chunk sizes from 16 to 64 bits
        if len(binary_block) % n == 0:
            possible_chunk_sizes.append(n)
    
    if not possible_chunk_sizes:
        raise ValueError("Cannot determine binary chunk size from the encrypted data")
    
    # Use the smallest possible chunk size (most likely correct)
    n = min(possible_chunk_sizes)
    print(f"Using binary chunk size: {n} bits")
    
    # Recover binary chunks
    recovered_list = [binary_block[i:i+n] for i in range(0, len(binary_block), n)]

    # Prepare the decryption key (split into two halves)
    final_key_str = str(final_key)
    length_of_key = len(final_key_str)
    half = (length_of_key // 2) + (length_of_key % 2)  # integer division, add 1 if odd length

    first_half_decryption = final_key_str[:half]            # up to but excluding half index
    second_half_decryption = final_key_str[half:]           # from half index to end

    # Convert binary back to integers
    int_list = [int(b, 2) for b in recovered_list]

    # Reverse the encryption process
    decrypted_values = []
    midpoint = len(int_list) / 2
    for i in range(len(int_list)):
        if i <= midpoint:
            decrypted_values.append(int_list[i] - int(first_half_decryption))
        else:
            decrypted_values.append(int_list[i] - int(second_half_decryption))

    # Convert back to hexadecimal
    hex_values = []
    for value in decrypted_values:
        # Convert to hex and ensure proper formatting
        hex_str = hex(value)[2:]
        # Pad with leading zeros if necessary to maintain structure
        while len(hex_str) < 12:  # 8 chars for key + at least 1 char for value
            hex_str = '0' + hex_str
        hex_values.append(hex_str)

    # Extract original keys and values from the hexadecimal strings
    original_values = []

    for s in hex_values:
        # First 8 characters are the key (4 bytes in hex), remaining are ASCII value
        if len(s) >= 9:  # Ensure we have at least key + 1 digit value
            original_values.append(s[8:])    # Extract the ASCII value part

    # Reconstruct and return the original message
    decrypted_message = ""
    for value in original_values:
        try:
            # Convert hex value to character
            decrypted_message += chr(int(value))
        except (ValueError, TypeError):
            # Handle potential conversion errors
            print(f"Warning: Could not convert value '{value}' to character")
    
    return decrypted_message

def main():
    """
    Main decryption function that takes encrypted binary data and key to recover original message.
    """
    print("=== DECRYPTION TOOL ===")
    
    # Get encrypted binary data
    binary_block = input("Enter the encrypted binary data: ")
    
    # Get the final key used for encryption
    final_key = input("Enter the final key used for encryption: ")
    
    try:
        # Decrypt the message
        decrypted_message = decrypt_message(binary_block, final_key)
        
        # Output the result
        print(f"\nDecryption successful!")
        print(f"Your decrypted message is: {decrypted_message}")
        
    except Exception as e:
        print(f"\nDecryption failed: {str(e)}")
        print("Please verify that:")
        print("1. The binary data is correct and complete")
        print("2. The key is exactly the same as used for encryption")
        print("3. The data wasn't corrupted or modified")

if __name__ == "__main__":
    main()
