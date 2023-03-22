import random, math

LOW_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def isPrime(num):
    if (num < 2):
        return False
    for prime in LOW_PRIMES:
        if (num == prime):
            return True
        if (num % prime == 0):
            return False
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s until it is odd
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


# randomly test number from 1/2 the end to the end
def generateLargePrime(keysize):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if isPrime(num):
            return num
            break


def generatekey():
    keysize = int(input("How many bits do you want for your prime number?"))
    p = 0
    q = 0
    print("Generating Primes ...")
    while p == q:
        p = generateLargePrime(keysize)
        q = generateLargePrime(keysize)
    n = p * q
    print("\nPrivate Key p = " + str(p))
    print("\nPrivate Key q = " + str(q))
    print("\nPublic Key Modulus: " + str(n))
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if math.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    print("\nPublicKey e = " + str(e))
    return [n, e]


# mainline
publicKey = generatekey()
