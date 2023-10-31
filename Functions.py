import random
import math
import os


def verifyPrime(num):
    print("Verifying prime")
    
    if num > 1:
        for i in range(2, int(num**0.5)+1):

            if (num % i) == 0:
                print(num, "is not a primenumber")
                return False
        print("Prime is verified")
        return True

    else:
        print(num, "Must be larger than 1")
        return False

def publickeyGenerator(p, q, modN):
    print("---Public key Generation started---")

    possibilities = [] 
    randomPublickey = []

    while possibilities == []:
        #vælger 10 random tal mellem 2 og n
        for x in range(10):

            num = random.randrange(3, modN)

            if num not in randomPublickey:
                randomPublickey += [num]
        print("Random publickey muligheder = ", len(randomPublickey))

        #Tjekker om nogen af tallene passer til kriterierne
        #for x in range(2, n):
        for x in randomPublickey:
            if x != p and x != q:

                if verifyPrime(x):
                    if x < modN:
                        if math.gcd(x, modN) == 1:
                            possibilities.append(x)
        print("reelle muligheder = ", len(possibilities))
    if possibilities != None:
        return random.choice(possibilities)


#---de 2 funktioner herunder er til at generere den private nøgle------
#euklids algorithme
def findModInverse(publicKey, modN):
    if math.gcd(publicKey, modN) != 1:
        return None
    u1, u2, u3 = 1, 0, publicKey
    v1, v2, v3 = 0, 1, modN
   
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % modN

def privatekeyGenerator(publicKey, modN):
    print("---Private key Generation started---")

    print("---Calculating d that is mod inverse of e---")
    d = findModInverse(publicKey, modN)
    publicKey = (publicKey)
    privateKey = (d)
    return (privateKey)


#--------------------
def Encrypter(encodedStr, publicKey, n):
    print("---Encrypting message---")
    encryptedStr = [(num ** publicKey) % n for num in encodedStr]

    return encryptedStr



def Decrypt(encryptedString, privateKey, n):
    decryptedList = []
    print("---Decrypting---")

    #---Fjerner komma, mellemrum og brackets---
    if type(encryptedString) == str:
        encryptedList = encryptedString.split()

        encryptedList = [elem.replace('[', '') for elem in encryptedList]
        encryptedList = [elem.replace(',', '') for elem in encryptedList]
        encryptedList = [elem.replace(']', '') for elem in encryptedList]

    else:
        encryptedList = encryptedString

    i = 0
    for x in encryptedList:

        i += 1

        decryptedChar = (int(x) ** privateKey) % n
        decryptedList.append(decryptedChar)


        os.system('cls')
        print(i/len(encryptedList)*100,"%")
        print(decryptedList)

    return decryptedList



def strEncoder(text):
    print("---Converting message to numbers---")

    charValues = []
    #string to numbers
    for char in text:
        charValues.append(ord(char))

    return charValues



def strDecoder(decryptedList):
    print("---Converting message to chars---")

    decodedMessage = []

    for x in decryptedList:
        decodedMessage.append(chr(x))

    besked = ''.join(decodedMessage)

    return besked


