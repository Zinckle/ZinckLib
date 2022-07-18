from ZinckLib import *


def ToLetter(valList):
    """
    Takes a lits of ints and combines them into one string based (1 = a, 2 = b, ..., 26 = z)

    :param string: The list of ints to convert.
    :type string: list of ints

    :return: this list combined into a string
    :rtype: string
    """
    output = ""
    for val in valList:
        if 0 < val <= 26:
            val = chr(val)
        elif val == 0:
            val = " "
        output = output + str(val)
    return output



if __name__ == '__main__':
    toNumber('PyCharm')

