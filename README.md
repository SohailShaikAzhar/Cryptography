# Cryptography Project
## Text Encryption/Decryption Tool
A simple Python-based encryption and decryption tool that converts text into encrypted ciphertext and back again.

### Overview
This project implements a basic cryptographic system following the process:

text
Text → Encrypt → Cipher Text → Decrypt → Text
### Current Status - Day 1
✅ Implemented initial encryption logic

🔄 Working on fixing some bugs in the implementation

⚠️ Basic functionality is working but needs refinement

### Features
Text encryption using XOR operations with cryptographic keys

Hexadecimal and binary output formats

Unique key generation for each character

Simple command-line interface

### Project Structure
text
cryptography-project/
-- message.py     
-- README.md      

### Technical Details
The encryption process:

Generates unique 16-byte cryptographic keys for each character

Uses the XOR operation with the last byte of each key for encryption

Outputs results in both hexadecimal and binary formats

Maintains a mapping dictionary for potential decryption


### Contributing
This is a learning project. Feel free to fork and experiment with different encryption approaches.

### License
This project is open source.

### Note: This is an educational project and should not be used for securing sensitive information in production environments.
