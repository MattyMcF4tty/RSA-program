from AdvancedFunctions import *
from CacheManager import *
from os import *

os.system('cls')
print("Welcome \nWith this program, you can Encrypt messages with RSA. \nYou can also Decrypt and Crack RSA encrypted messages\n")


choice = input("[Encrypt/Decrypt/KeyGenerator]: ")

if choice.lower() == "keygenerator" or choice.lower() == "key" or choice.lower() == "generator" or choice.lower() == "k" or  choice.lower() == "kg":
    Setup()
    
    

#------------------Encryption------------------------
if choice.lower() == "encrypt" or choice.lower() == "e":
    while True:
        print()
        FPublickey = int(input("Publickey:"))
        Fn = int(input("n:"))
        unEncryptedStr = input("Write your message here:")
        EncodedStr = strEncoder(unEncryptedStr)
        print(Encrypter(EncodedStr, FPublickey, Fn))


#-------------------Decryption----------------------------
if choice.lower() == "decrypt" or choice.lower() == "d":
    print("Do you wish to use new or old values?")
    choice = input("[New, Old]: ")
    print(choice)

    if choice.lower() == "new" or choice.lower() == "n":

        encryptedList = input("Encrypted list: ")
        privateKey = int(input("private key: "))
        ModN = int(input("Modulus (n): "))
        
        decryptedList = Decrypter(encryptedList, privateKey, ModN)
        print(decryptedList)
        print(strDecoder(decryptedList))



    elif choice.lower() == "old" or choice.lower() == "o":

        if CacheChecker():
            while True:
                print()
                cache = CacheReader()
                decryptMsg = input("Message to decrypt: ")
                print(Decrypter(decryptMsg, cache["privateKey"], cache["n"]))   
                os.system('pause') 
    
        else:
            print("It seems you dont have the required information \n You will therefore need to manually write the required information")
            
            encryptedList = input("Encrypted list: ")
            privateKey = int(input("private key: "))
            n = int(input("Modulus (n): "))

            print(Decrypter(encryptedList, privateKey, n))

            os.system('pause')

    else:
        print("Error decrypting")
            


   
