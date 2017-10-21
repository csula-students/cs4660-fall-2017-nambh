"""Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """

    def get_mean(self, line_number):
        file = open("./test/fixtures/array.txt", "r")
        data = (file.readlines()[line_number])
        l = data.split(' ')
        l = list(map(int, l))
        avg = (float(sum(l))/len(l))
        return avg

    def get_max(self, line_number):
        file = open("./test/fixtures/array.txt", "r")
        data = (file.readlines()[line_number])
        l = data.split(' ')
        l = list(map(int, l))
        maxval = max(l)
        return maxval

    def get_min(self, line_number):
        file = open("./test/fixtures/array.txt", "r")
        data = (file.readlines()[line_number])
        l = data.split(' ')
        l = list(map(int, l))
        minval = min(l)
        return minval

    def get_sum(self, line_number):
        file = open("./test/fixtures/array.txt", "r")
        data = (file.readlines()[line_number])
        l = data.split(' ')
        l = list(map(int, l))
        return sum(l)