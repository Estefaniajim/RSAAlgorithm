from random import randint


def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6
    return True


def generateNum(i):
    nums = set()
    while len(nums) != i:
        num = randint(0, 100)
        while not isPrime(num):
            num = randint(0, 100)
        nums.add(num)
    return nums


def getMod(t):
    e, d = generateNum(2)
    while ((e * d) % t) != 1:
        e, d = generateNum(2)
    return e, d


def generateKeys():
    keys = {}
    p, q = generateNum(2)
    n = p * q
    t = (p - 1) * (q - 1)
    e, d = getMod(t)
    keys["public"] = (e, n)
    keys["private"] = (d, n)
    return keys


def encrypt(publicKey, n):
    encryptedKey = []
    original = []
    for i in range(10):
        ranL = randint(0, 256)
        original.append(ranL)
        letter = (ranL ** publicKey) % n
        newLetter = chr(letter)
        encryptedKey.append(newLetter)
    return encryptedKey, original


def decrypt(privateKey, encryptedKey):
    decryptedKey = []
    key, n = privateKey
    for i in range(10):
        newChar = ord(encryptedKey[i])
        decryptedValue = (newChar ** key) % n
        decryptedKey.append(decryptedValue)
    return decryptedKey


# keys = generateKeys()
# print(keys)
# puKey, n = keys["public"]
# prKey = keys["private"]
# encrypted, original = encrypt(puKey, n)
# print(encrypted)
# print(original)
# print(decrypt(prKey, encrypted))
