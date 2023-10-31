from os.path import exists
from Functions import *
import json

def CacheWriter(prime1, prime2, publicKey, privateKey, n, modN):
    cache = {"prime1": prime1, "prime2": prime2, "publicKey": publicKey, "privateKey": privateKey, "n": n, "modN": modN}

    with open("Cache.json", "w") as cachefile:
        json.dump(cache, cachefile)


def CacheChecker():
    if exists("Cache.json"):
        with open("Cache.json", "r") as cachefile:
            cache = json.load(cachefile)
            tester = [12, 34]
            print("---Testing cache for errors---")
            encryptedTester = Encrypter(tester, cache["publicKey"],cache["n"])
            decryptedTester = Decrypt(encryptedTester, cache["privateKey"], cache["n"])
            if tester == decryptedTester:
                return True
            else:
                return False


def CacheReader():
    with open("Cache.json", "r") as cachefile:
        cache = json.load(cachefile)
        return cache

