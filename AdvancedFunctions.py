from Functions import *
from CacheManager import *
import os  


def Setup():
    os.system('cls')
    print("Welcome to the keypair generator")
    
 #--------Tjekker om første tal er et primtal------
    prime1 = int(input("1st prime: "))
    while verifyPrime(prime1) != True:
        print("\n")
        prime1 = int(input("1st prime: "))
    
 #--------Tjekker om andet tal er et primtal-------
    prime2 = int(input("2nd prime: "))
    while True:
        if prime1 != prime2:
            if verifyPrime(prime2):
                break
        print("\n")
        prime2 = int(input("2nd prime: "))

    print("---Primes verified---")

    print("---Generating n and mod(n)---")
    n = prime1*prime2
    modN = int((prime1-1)*(prime2-1))
    print("n: ", n, "    mod(n): ", modN)
    print()


    publicKey = publickeyGenerator(prime1, prime2, modN)
    print("public key: ", publicKey)
    print()

    privateKey = privatekeyGenerator(publicKey, modN)
    print("private key: ", privateKey)
    print()
    CacheWriter(prime1, prime2, publicKey, privateKey, n, modN)

    print("Publickey: ", publicKey)
    print("Privatekey: ", privateKey)
    print("n: ", n)
    print("modN: ", modN)

    return(publicKey, privateKey, modN, n)


# --- Decryption function ---
def Decrypter(encryptedStr, privateKey, ModN):
    decryptedStr = Decrypt(encryptedStr, privateKey, ModN)
    print("Dekrypteret besked:", decryptedStr)

    decodedStr = strDecoder(decryptedStr)
    print("Decoded string:", decodedStr)
