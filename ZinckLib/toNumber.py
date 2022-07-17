from ZinckLib import *


class ToNumber:

    def __init__(self, toConv, ):
        self.toConv = toConv

    def toNumber(self, toConv, asList=False):
        """
        converts a string to either a list or string separated by spaces of number representing the number
        (i.e. 1 = a, 2 = b, ..., 26 = z) with 0 representing any spaces and any non letter values not being converted. if
        only one letter is in the string then an int will be returned.

        :param toConv: The string to be converted.
        :type toConv: str

        :param asList: Controls if the return will be as a string or a list.
        :type asList: bool

        :return: the string/list/number that represents the given string.
        :rtype: if one char is given then it is int, otherwise it is based of the asList value to be
        """
        toConv = toConv.upper()
        toConv = splitString(toConv)
        if len(toConv) == 1:
            num = ord(toConv[0]) - 64
            if 0 < num <= 26:
                return num
            elif num == -32:
                return 0
            return toConv[0]
        out = ""
        for char in toConv:
            val = ord(char) - 64
            if 0 < val <= 26:
                out = out + str(val) + " "
                continue
            elif val == -32:
                out = out + "0" + " "
                continue
            out = out + char + " "
        out = out.split(" ") if asList else out
        return out[:1]
