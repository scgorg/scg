import json
import sys

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

SETTING_FILE = ".setting.bin"
KEY_FILE = ".keys.ini"


def init_key(secret):
    random_salt = get_random_bytes(32)
    key = PBKDF2(secret, random_salt, dkLen=32)

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key


def read_key():
    try:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print(f"There is no {KEY_FILE} file, please do `scg init` first")
        sys.exit(0)


def encrypt(key, account, pwd):
    cipher = AES.new(key, AES.MODE_CBC)
    encoded_data = json.dumps({"ACCOUNT": account, "PASSWORD": pwd}).encode("utf-8")
    cipheredData = cipher.encrypt(pad(encoded_data, AES.block_size))
    with open(SETTING_FILE, "wb") as f:
        f.write(cipher.iv)
        f.write(cipheredData)


def decrypt(key):
    try:
        with open(SETTING_FILE, "rb") as f:
            iv = f.read(16)
            cipheredData = f.read()

        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

        original_data = unpad(cipher.decrypt(cipheredData), AES.block_size)
        setting = json.loads(original_data.decode("utf-8"))
        if setting["ACCOUNT"] and setting["PASSWORD"]:
            print("Account is all set")
        else:
            print("Your account is not set up")
    except FileNotFoundError:
        print(f"There is no {SETTING_FILE} file, please do `scg init` first")
        sys.exit(0)


if __name__ == "__main__":
    pass
