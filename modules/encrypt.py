
try:
    path = input("Enter path of Image: ")
    key = int(input("Enter Key for encryption of Image:"))
    print(f"The path of File, {path}") 
    print(f'Key For encryption, {key}')
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print('Encryption Done...')
except Exception:
    print(f'Error caught, {Exception.__name__}')