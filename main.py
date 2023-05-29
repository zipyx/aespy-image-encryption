# References
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
# https://stackoverflow.com/questions/61420893/python-3-encrypt-and-decrypt-image-using-aes
# https://stackoverflow.com/questions/41980931/image-encryption-and-decryption-using-pycrypto

import os.path
import time
from PIL import Image
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad 

def main():
    """
    Main function that run the program

    -> key: bytes 
    -> file_name: str 
    -> file_exists: bool
    """

    key = b"770A8A65DA156D24EE2A093277530142"
    keyHex = "770A8A65DA156D24EE2A093277530142"
    keyToByteArray = bytearray.fromhex(keyHex)
    keyToHex = bytes.fromhex(keyHex)

    print("[+] Key [Hex]:", keyHex)
    print("[+] Key [ByteArray]:", keyToByteArray)
    print("[+] Key [FromHex]:", keyToHex)

    file_name = "Image-Assignment2.bmp"
    file_exists = os.path.exists(file_name)

    if file_exists:
        start_time = time.time()
        print("[+] File exists... starting encryption")

        encrypt_file_using_aes_ecb(file_name, keyToHex)
        encrypt_file_using_aes_cbc(file_name, keyToHex)
        encrypt_file_using_aes_cfb(file_name, keyToHex)

        end_time = time.time()
        print("[!] AES Encryption took : ", end_time - start_time)


def get_file_stream_bytes(file_name: str) -> bytes:
    """ Return bytes

    Get the bytes of a file and store them in a variable
    and return the bytes of the file
    """

    with open(file_name, 'rb') as read_file:
        stream = read_file.read()
    read_file.close()
    return stream


def write_bytes_to_jpg_file(aes_mode: str, file_name: str, stream: bytes):
    """
    Write the bytes of a file to a new file
    """

    imageName = \
        aes_mode.upper() \
        + "__" \
        + os.path.splitext(file_name)[0] \
        + "__.jpg"
    image = Image.frombytes('RGB', (600, 600), stream)
    image.save(imageName, "JPEG")
    image.close()


def encrypt_file_using_aes_ecb(file_name: str, key: bytes):
    """
    Encrypt a file using AES in EBC mode
    """

    # Read file content
    file_bytes = get_file_stream_bytes(file_name)

    # Get cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Encrypt content stream of data from file
    encrypted_bytes = cipher.encrypt(pad(file_bytes, AES.block_size))
    write_bytes_to_jpg_file("ecb", file_name, encrypted_bytes)


def encrypt_file_using_aes_cbc(file_name: str, key: bytes):
    """
    Encrypt a file using AES in CBC mode
    """

    # Read file content
    file_bytes = get_file_stream_bytes(file_name)

    # Get cipher
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Encrypt content stream of data from file
    encrypted_bytes = cipher.encrypt(pad(file_bytes, AES.block_size))
    write_bytes_to_jpg_file("cbc", file_name, encrypted_bytes)


def encrypt_file_using_aes_cfb(file_name: str, key: bytes):
    """
    Encrypt a file using AES in CFB mode
    """

    # Read file content
    file_bytes = get_file_stream_bytes(file_name)

    # Get cipher
    cipher = AES.new(key, AES.MODE_CFB)
    
    # Encrypt content stream of data from file
    encrypted_bytes = cipher.encrypt(pad(file_bytes, AES.block_size))
    write_bytes_to_jpg_file("cfb", file_name, encrypted_bytes)


if __name__ == "__main__":
    main()
