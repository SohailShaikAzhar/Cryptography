# Cryptography Project
Text Encryption/Decryption Tool
A Python-based encryption and decryption tool that converts text into encrypted binary ciphertext and back again using a custom cryptographic algorithm.

## Overview
This project implements a custom cryptographic system with the following process:

Plain Text → Encrypt → Binary Cipher Text → Decrypt → Plain Text
## 📋 Project Status
### Day 1 - Foundation
✅ Initial Encryption Logic - Basic encryption implementation.

✅ Initial Structure - Core framework established (with some bugs and incomplete features).

### Day 2 - Core Implementation
✅ Complete Encryption System - Fully functional encryption module.

✅ Complete Decryption System - Fully functional decryption module.

✅ Cryptographic Security - Uses cryptographically secure random number generation (CSPRNG).

✅ Key Management - Proper key generation, handling, and storage mechanisms.

✅ Binary Encoding - Fixed binary encoding/decoding issues for reliable data processing.

✅ Standalone Modules - Separate, well-organized files for encryption and decryption.

### Day 3 - Security Enhancements
✅ Zero-Prefix Prevention - Implemented protection against zero-byte prefixes in generated values.

✅ Robust Key Validation - Added while-loop validation to ensure generated keys never start with zero.

✅ Byte-Level Security - Direct byte manipulation for efficient zero-byte detection.

✅ Deterministic Output - Guaranteed non-zero starting bytes for all cryptographic values.


## Features
Text encryption using dual-phase key encryption

Binary output format for ciphertext

Unique key generation for each character

Cryptographically secure random number generation

Simple command-line interface

Standalone encryption and decryption modules

## Technical Details
The encryption process:

Generates a 16-byte cryptographic master key

Splits the key into two halves for dual-phase encryption

Creates unique 4-byte keys for each character

Maps characters to their ASCII values with unique keys

Applies dual-phase encryption using split key halves

Converts results to binary format

The decryption process:

Recovers binary chunks from the ciphertext

Splits the master key into two halves

Reverses the encryption process

Extracts original character values

Reconstructs the original message

## Project Structure
text
cryptography-project/
│
├── encrypt.py          # Encryption module
├── decrypt.py          # Decryption module
└── README.md           # Project documentation
## Usage
Encryption:
python encrypt.py
Enter text when prompted, receive binary ciphertext and encryption key.

## Decryption:
python decrypt.py
Provide binary ciphertext and encryption key when prompted.

## Contributing
This is a learning project. Feel free to fork and experiment with different encryption approaches.

## License
This project is open source.

## Note
This is an educational project and should not be used for securing sensitive information in production environments.
