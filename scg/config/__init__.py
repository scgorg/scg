from Crypto.Protocol.KDF import PBKDF2

{"ACCOUNT": "", "PASSWORD": ""}

salt = b"|\xe1VJ\x16E\xeaP\x9e\xbd\xf6x\xd7\x18\x1a\xd1\xc3\x1by\x8dY\x90\x8d\x8a\xda$M\xcd\xe5w\xc8\x90"

pw = "scg"

key = PBKDF2(pw, salt, dkLen=32)
