from datetime import datetime
import random


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
