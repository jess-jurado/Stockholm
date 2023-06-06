
# README - File Encryption

This is a Python program for encrypting and decrypting files using the Fernet algorithm from the cryptography library. The program offers two main functions: `encrypt` and `decrypt_files`, which allow you to encrypt and decrypt files in a specified folder.

## Requirements

- Python 3.x
- cryptography (installable via pip: `pip install cryptography`)

## Usage

The program is executed from the command line and offers the following options:

'python program_name.py [-h] [-reverse <password>] [-silent] [-version]'


- `-h`, `--help`: Show the help message and exit.
- `-reverse <password>`: Insert `-reverse <password>` to decrypt the files using the provided password.
- `-silent`: Run the program silently, without printing progress.
- `-version`: Show the program version.

## File Encryption

File encryption is performed using the **`encrypt`** function. When running the program without any additional options, all files in a folder called "infection" in the user's home directory will be encrypted.

The program generates an encryption key using Fernet and prints it to the console (unless running in silent mode). Make sure to remember this password as it will be needed to decrypt the files in the future.

## File Decryption

File decryption is performed using the **`decrypt_files`** function. To decrypt the files, run the program with the **`-reverse`** option followed by the password used to encrypt the files. For example:

'python program_name.py -reverse <password>'


The program will search for files with the ".ft" extension in the "infection" folder and decrypt them using the provided password. The decrypted files will be saved in the same folder with their original names.

## Examples

- Encrypt files:

'python program_name.py'


- Decrypt files:


'python program_name.py -reverse <password>'


- Encrypt files silently:

'python program_name.py -silent'


- Decrypt files silently:

'ython program_name.py -reverse <password> -silent'


## Notes

- Ensure that you have the proper permissions to access the files in the specified folder.
- Keep in mind that this program encrypts and decrypts files in the same folder. Make appropriate backups before running the program.
- Use this program responsibly and only in your own environment or with the permission of the file owner.
- If you forget the password used to encrypt the files, it will not be possible to decrypt them.

**Make sure to fully understand how the program works and use it responsibly!**

