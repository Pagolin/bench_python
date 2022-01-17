import math
import random
import tempfile

def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1

def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True


# Take from https://www.codeproject.com/Articles/691200/%2FArticles%2F691200%2FPrimality-test-algorithms-Prime-test-The-fastest-w
def MillerRabinPrimalityTest(number):
    '''
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( spcial case )
    if we get the number 1 we return false and any other even
    number we will return false.
    '''
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False

    ''' first we want to express n as : 2^s * r ( were r is odd ) '''

    ''' the odd part of the number '''
    oddPartOfNumber = number - 1

    ''' The number of time that the number is divided by two '''
    timesTwoDividNumber = 0

    ''' while r is even divid by 2 to find the odd part '''
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1

    '''
    since there are number that are cases of "strong liar" we 
    need to check more then one number
    '''
    for time in range(3):

        ''' choose "Good" random number '''
        while True:
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number) - 1
            if randomNumber != 0 and randomNumber != 1:
                break

        ''' randomNumberWithPower = randomNumber^oddPartOfNumber mod number '''
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)

        ''' if random number is not 1 and not -1 ( in mod n ) '''
        if (randomNumberWithPower != 1) and (
                randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1

            ''' while we can squre the number and the squered number is not -1 mod number'''
            while (iterationNumber <= timesTwoDividNumber - 1) and (
                    randomNumberWithPower != number - 1):
                ''' squre the number '''
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)

                # inc the number of iteration
                iterationNumber = iterationNumber + 1
            '''     
            if x != -1 mod number then it because we did not found strong witnesses
            hence 1 have more then two roots in mod n ==>
            n is composite ==> return false for primality
            '''
            if (randomNumberWithPower != (number - 1)):
                return False

    ''' well the number pass the tests ==> it is probably prime ==> return true for primality '''
    return True


def mersene_primes_to(n):
    p = 2
    count = 0
    while True:
        m = (2 << (p - 1)) - 1
        if MillerRabinPrimalityTest(m):
            count = count + 1
            if count == n:
                break
        # obtain next prime, p
        while True:
            p = p + 2 if (p > 2) else 3
            if MillerRabinPrimalityTest(p):
                break


def gen_random_space(xExt, yExt, zExt):
    xMin, xMax = -xExt, xExt
    yMin, yMax = -yExt, yExt
    zMin, zMax = -zExt, zExt
    randomSpace = []

def fannkuch(n):
    count = list(range(1, n+1))
    max_flips = 0
    m = n-1
    r = n
    check = 0
    perm1 = list(range(n))
    perm = list(range(n))

    while 1:
        if check < 30:
            check += 1

        while r != 1:
            count[r-1] = r
            r -= 1

        if perm1[0] != 0 and perm1[m] != m:
            perm = perm1[:]
            flips_count = 0
            k = perm[0]
            while k:
                perm[:k+1] = perm[k::-1]
                flips_count += 1
                k = perm[0]

            if flips_count > max_flips:
                max_flips = flips_count

        while r != n:
            perm1.insert(r, perm1.pop(0))
            count[r] -= 1
            if count[r] > 0:
                break
            r += 1
        else:
            return max_flips

def allocate_list(i):
    l = [random.randint(0, i) for _ in range(i)]
    l.sort()
    x = sum(l)
    return l,x

def allocate_and_sum_list(i):
    l = [random.randint(0, i) for _ in range(i)]
    l.sort()
    return sum(l)

def allocate_and_write_to_file(i):
    l = [random.randint(0, i) for _ in range(i)]
    temp = tempfile.TemporaryFile(mode='w')
    temp.write(str(l))
    return sum(l)
