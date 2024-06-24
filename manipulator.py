import argparse
from modules import encrypt_decrypt, logo
# encrypt_decrypt.encrypt_decrypt()
def main():
    # Define the argument parser
    parser = argparse.ArgumentParser(description='Encrypt or decrypt an image using Image Manipulator.')
    parser.add_argument('-m', '--mode', choices=['e', 'd'], help='Mode: e for encrypt, d for decrypt')
    parser.add_argument('-p', '--path', help='The image path')
    parser.add_argument('-k', '--key', type=int, help='The key for encryption or decryption')

    args = parser.parse_args()

    # Print the logo
    logo.logo()

    if args.mode and args.path and args.key is not None:
        # If all command-line arguments are provided, use them
        mode = args.mode
        path = args.path
        key = args.key
    else:
        # Otherwise, fall back to interactive input
        mode = input("Choose one to continue! \n1. Encrypt-->e \n2.Decrypt-->d\n-->").lower()
        if 'e' in mode :print("=== encrypting mode ===")
        else: print("=== decrypting mode ===")
        path = input('Please enter the path to encrypt/decrypt!\n-->')
        key = int(input('Please enter key to encrypt/decrypt!\n-->'))

    if 'e' in mode:
        print(encrypt_decrypt.encrypt_decrypt(path, key))
    elif 'd' in mode:
        print(encrypt_decrypt.encrypt_decrypt(path, key))

if __name__ == '__main__':
    main()