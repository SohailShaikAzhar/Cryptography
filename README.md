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

### Installation
Clone this repository

Ensure Python 3.10 is installed on your system

No additional dependencies required

### Usage
Run the encryption script:

### bash
python message.py
Follow the prompts to enter text for encryption. The program will output:

Encryption mapping (keys to characters)

Individual encryption details for each character

Final encrypted message in hexadecimal format

Binary representation of the encrypted message

### Project Structure
text
cryptography-project/
├── encryption.py      # Main encryption implementation
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies (none currently)
Technical Details
The encryption process:

Generates unique 16-byte cryptographic keys for each character

Uses the XOR operation with the last byte of each key for encryption

Outputs results in both hexadecimal and binary formats

Maintains a mapping dictionary for potential decryption

### Future Plans
Implement decryption functionality

Fix existing bugs in the encryption logic

Add support for different encryption algorithms

Create a graphical user interface

Add file encryption capabilities

Implement proper key management and exchange

### Contributing
This is a learning project. Feel free to fork and experiment with different encryption approaches.

### License
This project is open source.

### Note: This is a educational project and should not be used for securing sensitive information in production environments.
