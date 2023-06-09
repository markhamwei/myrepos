from datetime import datetime
import random
from django.http import HttpResponse
import wolframalpha
import math
import base64
from itertools import cycle

IMPROPER = 0
PROPER = 1
MIXED = 2

def get_msec():
    now = datetime.now()
    return (now.microsecond)


def get_sec():
    now = datetime.now()
    return (now.second)

def get_random(min, max):
    """Create a single random number between min & max (inclusive)
    """
    msec = get_msec()
    random.seed(msec)
    return random.randint(min, max)


def get_randoms(count, min, max):
    """Create a list of random numbers between min & max (inclusive)
    """
    msec = get_msec()
    random.seed(msec)
    randoms = []
    for i in range(count):
        randoms.append(random.randint(min, max))
    return randoms

def get_randoms_unique(count, min, max):
    """create a list of unique random numbers between min & max (inclusive)
    """
    return random.sample(range(min, max+1), count)


def math_query(query):
    client = wolframalpha.Client("GLYJRW-TEH7UK7VYL")
    # Send query to Wolfram API
    try:
        res = client.query(query)
        return (next(res.results).text)
    except Exception:
        # Return a bad request response if the request data cannot be decoded or parsed
        return ('Invalid query string')

def get_improper_fraction(min, max):
    """min, max is the range for numerator and denominator.
    """
    randoms = get_randoms(2, min, max)
    num1 = randoms[0]
    num2 = randoms[1]
    if(num1 == num2):
        num1 = num2 + 1
    commonFactor = math.gcd(num1, num2)
    fraction = [0, 0]
    if(num1 > num2):
        fraction[0] = int(num1/commonFactor)
        fraction[1] = int(num2/commonFactor)
    else:
        fraction[0] = int(num2/commonFactor)
        fraction[1] = int(num1/commonFactor)
    if(fraction[1] == 1):
        fraction[1] = 2
        if(fraction[0]%2 == 0):
            fraction[0] += 1
    return fraction
    
def get_proper_fraction(min, max):
    """min, max is the range for numerator and denominator.
    """
    randoms = get_randoms(2, min, max)
    num1 = randoms[0]
    num2 = randoms[1]
    if(num1 == num2):
        num1 = num2 + 1
    commonFactor = math.gcd(num1, num2)
    fraction = [0, 0]
    if(num1 > num2):
        fraction[0] = int(num2/commonFactor)
        fraction[1] = int(num1/commonFactor)
    else:
        fraction[0] = int(num1/commonFactor)
        fraction[1] = int(num2/commonFactor)
    return fraction

def get_mixed_fraction(maxInt, min, max):
    """the integer part is in range 1~maxInt,
       min, max is the range for numerator and denominator.
    """
    fraction = [0, 0, 0]
    randoms = get_randoms(1, 1, maxInt)
    fraction[0] = randoms[0]
    tmp = get_proper_fraction(min, max)
    fraction[1] = tmp[0]
    fraction[2] = tmp[1]
    return fraction
    
def add_fractions(int1, numerator1, denominator1, int2, numerator2, denominator2):
    """ calculate the addition of two fractions
    """
    tmpdenominator = int(math.lcm(denominator1, denominator2))
    tmpnumerator = int((numerator1 * (tmpdenominator / denominator1)) + (numerator2 * (tmpdenominator / denominator2)))
    gcd = math.gcd(tmpnumerator, tmpdenominator)
    denominator = tmpdenominator / gcd
    numerator = tmpnumerator / gcd
    result_int = int1 + int2
    if(numerator >= denominator):
        result_int += int(numerator/denominator)
        numerator %= denominator
        if(numerator == 0):
            denominator = 0 #use both 0 to represent no fraction part
    result = [0, 0, 0]
    result[0] = result_int
    result[1] = numerator
    result[2] = denominator
    return result

def subtract_fractions(int1, numerator1, denominator1, int2, numerator2, denominator2):
    """ calculate the subtraction of two fractions, assume the fraction 1 is greater
    """
    tmpdenominator = int(math.lcm(denominator1, denominator2))
    tmpnumerator = int(((numerator1 + (int1 * denominator1)) * (tmpdenominator / denominator1)) -
                        ((numerator2 + (int2 * denominator2)) * (tmpdenominator / denominator2)))
    gcd = math.gcd(tmpnumerator, tmpdenominator)
    denominator = tmpdenominator / gcd
    numerator = tmpnumerator / gcd
    result_int = int(numerator / denominator)
    numerator %= denominator
    if(numerator == 0):
        denominator = 0 #use both 0 to represent no fraction part
    result = [0, 0, 0]
    result[0] = result_int
    result[1] = numerator
    result[2] = denominator
    return result

def compare_fractions(int1, numerator1, denominator1, int2, numerator2, denominator2):
    """ Return 1 if fraction1 is greater than franction2
        Return 0 if fraction1 is equal to fraction2
        Return -1 if fraction1 is smaller than fraction2
    """
    tmpdenominator = int(math.lcm(denominator1, denominator2))
    num1 = (numerator1 + (int1 * denominator1)) * (tmpdenominator / denominator1)
    num2 = (numerator2 + (int2 * denominator2)) * (tmpdenominator / denominator2)
    ret = 0
    if(num1 > num2):
        ret = 1
    else:
        if(num1 < num2):
            ret = -1
    return ret

def multiply_fractions(int1, numerator1, denominator1, int2, numerator2, denominator2):
    """ franction1 multiply franction2
    """
    tmpnumerator = (int1 * denominator1 + numerator1) * (int2 * denominator2 + numerator2)
    tmpdenominator = denominator1 * denominator2
    commFactor = math.gcd(tmpnumerator, tmpdenominator)
    numerator = int(tmpnumerator / commFactor)
    denominator = int(tmpdenominator / commFactor)
    int_result = int(numerator / denominator)
    numerator %= denominator
    fraction = [0, 0, 0]
    fraction[0] = int_result
    fraction[1] = numerator
    fraction[2] = denominator
    return fraction

def divide_fractions(int1, numerator1, denominator1, int2, numerator2, denominator2):
    """ franction1 divide franction2
    """
    tmpnumerator = (int1 * denominator1 + numerator1) * denominator2
    tmpdenominator = denominator1 * (int2 * denominator2 + numerator2)
    commFactor = math.gcd(tmpnumerator, tmpdenominator)
    numerator = int(tmpnumerator / commFactor)
    denominator = int(tmpdenominator / commFactor)
    int_result = int(numerator / denominator)
    numerator %= denominator
    fraction = [0, 0, 0]
    fraction[0] = int_result
    fraction[1] = numerator
    fraction[2] = denominator
    return fraction

def get_decimal(intRange, decimalRange):
    """ intRange: 1 for range (0, 9), 2 for range (0, 99)
        decimalRange: 1 for range (0, 9), 2 for range (0, 99), 3 for range (0, 999)
        return a list which has two pieces, int piece, and decimal piece.
    """
    devision = 1
    for _ in range(0, intRange):
        devision *= 10
    intPiece = get_random(0, devision-1)
    
    devision = 1
    for _ in range(0, decimalRange):
        devision *= 10
    decimalPiece = (get_random(0, devision-1)) / devision
    decimal = [0, 0]
    decimal[0] = intPiece
    decimal[1] = decimalPiece
    return decimal
    
def get_decimal2(decimalRange):
    """ decimalRange: represent how many digits after the decimal point
        1, means 1 digits; 2, means 2 digits, and so on;
        return a decimal directly.
    """
    devision1 = 1
    devision2 = 1
    for _ in range(0, decimalRange):
        devision1 *= 10
        devision2 *= 10
    devision2 *= 100
    tmpInt = get_random(devision1+1, devision2-1)
    if((tmpInt % 10) == 0):
        tmpInt += 1
    return (round((tmpInt/devision1), decimalRange))

def scramble(s):
    """ scramble: obfuscates the characters in a string in a way that is reversible. Used to hide answers. Guaranteed to work on ascii characters: no guarantee for anything else
    """
    return base64.b64encode(bytes(a^b for a, b in zip(s.encode(), cycle(b'scramble')))).decode()

def unscramble(s):
    """ unscramble: reverses the operation of scramble
    """
    return (bytes(a^b for a, b in zip(base64.b64decode(s.encode()), cycle(b'scramble')))).decode()

def myList2Str(mylist, order):
    """ order: True for reverse the input list
    """
    mystr = ""
    number = len(mylist)
    if(order == False):
        i = 0
        while(i < number):
            mystr += str(mylist[i])
            i += 1
            if(i < number):
                mystr += ","
        return mystr
    else:
        i = number - 1
        while(i >= 0):
            mystr += str(mylist[i])
            i -= 1
            if(i >= 0):
                mystr += ","
        return mystr
        

def myStr2List(mystr):
    mylist = mystr.split(',')
    return mylist
    
def getFactors(number):
    """ returen a list which contains all the factors of the specified number
    """
    factors = []
    for i in range(1, number+1):
        if((number % i) == 0):
            factors.append(i)
    return factors

def isPrime(number):
    """ return True if number is a prime number, otherwise return False
    """
    factors = getFactors(number)
    if(len(factors) == 2):
        return True
    else:
        return False
    
def getPrimeFactors(number):
    """ return a list which contains all the factors of the specified number
    """
    factors = []
    for i in range(1, number+1):
        if(((number % i) == 0) and (True == isPrime(i))):
            factors.append(i)
    return factors

def getItemsCount(mylist):
    """ return a dictionary which represent the count for each unique number in mylist
    """
    thisdict = {}
    mysize = len(mylist)
    for i in range(mysize):
        item = mylist[i]
        if item in thisdict.keys():
            thisdict[item] += 1
        else:
            thisdict[item] = 1
    return thisdict
