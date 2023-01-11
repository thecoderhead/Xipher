# Xipher
[XipherLogo](https://user-images.githubusercontent.com/46077685/211902267-981b05f5-0df0-48c8-a83e-da17d1b4f2df.png)

Xipher is a simple GUI for encrypting/decrypting files using PyQt5 and AES. User can select a file, enter a password and encrypt or decrypt it. The encryption/decryption uses a password-based key generated using PBKDF2. Good for demonstration, but use a vetted library in real-world scenarios.
File Crypto GUI
This script is a python script that provides a Graphical User Interface (GUI) for encrypting and decrypting a file.

# Requirements
python3

PyQt5

Crypto

struct
# Usage
Run the script by python3 filecrypto.py
In the GUI, you'll be prompted to enter a password, browse for a file and select whether to encrypt or decrypt the file.
After the selection the process of encryption or decryption will take place.
# Dependencies
PBKDF2 is missing in the crypto library, you should add it.
import struct is also missing in the script.
# Note
The encryption is using AES CBC encryption mode and the key is created using PBKDF2.
The key is derived from the password entered by the user.
The file encryption and decryption functions have a chunksize parameter that can be adjusted for optimal performance.
This script is for educational purposes only, always make sure to use industry-standard encryption and authentication methods when working with sensitive data.

# Limitations
This script is not suitable for large files, as the encryption and decryption process is done in memory.
There is no exception handling in case of wrong file path, missing dependencies or wrong password.
There is no authentication mechanism to check the access level of the user.
There is no limit of password length.
# Changelog
PBKDF2 is added.
struct import is added.
# Future Work
Add exception handling mechanism.
Add authentication mechanism.
Add limit of password length.
Make it suitable for large files encryption and decryption.
# Contribution
Any contribution is welcomed, whether it is a bug fix, new feature or simply feedback.
For any issues or bugs, please open a new issue in the GitHub repository.
# License
The script is open-source and available under the MIT License.
# Author
the script is written by me .
# Acknowledgments
This script is inspired by the encrypt and decrypt functions from the pycrypto library.
