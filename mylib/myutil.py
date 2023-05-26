from datetime import datetime
import random
from django.http import HttpResponse
import wolframalpha
import math

IMPROPER = 0
PROPER = 1
MIXED = 2

def get_msec():
    now = datetime.now()
    return (now.microsecond)


def get_sec():
    now = datetime.now()
    return (now.second)


def get_randoms(count, min, max):
    """Create a list of random numbers.
    """
    msec = get_msec()
    random.seed(msec)
    randoms = []
    for i in range(count):
        randoms.append(random.randint(min, max))
    return randoms


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
