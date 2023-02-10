def numberToText(num: int):
    """
    s

    :param num:
    :type num:

    :return:
    :rtype:
    """
    if (type(num) is not int) or num < 0 or num > 999999999999999999999999999999999999:
        raise TypeError('Only positive integers less than 999 decillion are allowed')


    if num == 0:
        return "zero"
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion"]

    if num < 20:
        return ones[num]
    elif num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
    elif num < 1000:
        return ones[num // 100] + ' hundred' + ('' if num % 100 == 0 else ' ' + numberToText(num % 100))
    else:
        i = 0
        words = ''
        while num > 0:
            if num % 1000 != 0:
                words = numberToText(num % 1000) + ' ' + thousands[i] + ' ' + words
            num = num // 1000
            i += 1
        return words.strip()
    return ' '.join(words.split())







