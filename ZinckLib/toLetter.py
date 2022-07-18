from ZinckLib import *


class ToLetter:

    def __init__(self, valList,):
        self.valList = valList

    def ToLetter(self, valList):
        """
        Takes a list of ints and combines them into one string based (1 = a, 2 = b, ..., 26 = z)

        :param valList: The list of ints to convert
        :type valList: list of ints

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
