from pysmx.SM3 import hash_msg
from pysmx.SM2 import generate_keypair
from gmssl import sm2, func

if __name__ == "__main__":
    file = open("sm3.pdf", "rb")
    data = file.read()

    print(hash_msg(data) + "\n")

    with open("sm3pdf-hash.txt", "w", encoding="utf-8") as hash_file:
        hash_file.write(hash_msg(data))

    pk, sk = generate_keypair()
    print(pk.hex() + "\n")
    print(sk.hex() + "\n")

    sm2_crypt = sm2.CryptSM2(public_key=pk.hex(), private_key=sk.hex())

    with open("sm2.pem", "w", encoding="utf-8") as sm2:
        sm2.write(sk.hex())
    with open("sm2Pub.pem", "w", encoding="utf-8") as sm2Pub:
        sm2Pub.write(pk.hex())

    data = bytes.fromhex(hash_msg(data))
    random_hex_str = func.random_hex(sm2_crypt.para_len)

    sign = sm2_crypt.sign(data, random_hex_str)
    print(sign + "\n")
    with open("sm3pdf-sign.txt", "w", encoding="utf-8") as sm3PdfSign:
        sm3PdfSign.write(sign)

    if sm2_crypt.verify(sign, data):
        print("right")
    else:
        print("wrong")
