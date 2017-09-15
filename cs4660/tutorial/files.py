"""Files tests simple file read related operations"""
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

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
       return 

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        for in in line_numbers

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        pass

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        pass
