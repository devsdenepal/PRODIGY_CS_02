def encrypt_decrypt(path,key):
    """
    Encrypts/decrypts the given image with key provided.

    Parameters:
    path (str): The path of image to be encrypted.
    key (int): The encryption key for the image.
    Returns: Process Completed! or error
    """
    try:
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        return 'Process Completed!'
    except Exception:
        print(f'Error caught, {Exception.__name__}')
# encrypt("../image.png",23)