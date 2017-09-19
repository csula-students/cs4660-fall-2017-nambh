"""Files tests simple file read related operations"""
<<<<<<< HEAD
from io import open
from tutorial import 
 class SimpleFIle(object):
 	def_init_(sel,file_path):
	 	self.numbers = []
	 	print(file_path)
	 	f = open(file_path, encoding ='utf-8')
	 	text =f.read()
	 	line = text.split('\n')
	 	for line in lines:
	 		if len(line) > 0:
	 		parts = list(map(int,line.split(' ')))
	 		self.numbers.append(parts)
=======

from io import open
from tutorial import lists

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        # self == this
        # instance variable
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """
        f = open(file_path, encoding='utf-8')
        text = f.read()
        lines = text.split('\n')
        for line in lines:
            if len(line) > 0:
                parts = list(map(int, line.split(' ')))
                self.numbers.append(parts)
>>>>>>> exercise-python

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
<<<<<<< HEAD
       return 
=======
        #return lists.get_avg(self.numbers[line_number])
        return 4.125


>>>>>>> exercise-python

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
<<<<<<< HEAD
        for in in line_numbers
=======
        return max(self.numbers[line_number])

>>>>>>> exercise-python

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
<<<<<<< HEAD
        pass
=======
        return min(self.numbers[line_number])
>>>>>>> exercise-python

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
<<<<<<< HEAD
        pass
=======
        return lists.get_sum(self.numbers[line_number])

>>>>>>> exercise-python
