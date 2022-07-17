class SplitString:

    def __init__(self, string):
        self.string = string

    def splitString(self, string):
        """
        Splits a string into a list of chars

        :param string: The string to split.
        :type string: str

        :return: the string split into individual chars
        :rtype: list of strings
        """
        return [char for char in string]
