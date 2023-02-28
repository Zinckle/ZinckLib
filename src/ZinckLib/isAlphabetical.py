def isAlphabetical(toCheck: str):
    """
   test
    """
    if type(toCheck) is not str:
        raise TypeError('Only strings are allowed')
    toCheck = toCheck.lower()
    lastOrd = 96
    for char in toCheck:
        orded = ord(char)
        if 97 <= orded <= 122:
            if lastOrd > orded:
                return False
            lastOrd = orded
    return True
