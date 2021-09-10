"""
Author:  Adonay Pichardo
Date:    07SEP2021
Contact: apichardo2019@my.fit.edu
"""

from sys import argv # Used for command line arguments

old_file = open(argv[1], "r")                               # The original dictionary
new_file = open("../dictionaries/l337.dict", "w") # The new altered dictionary

for every_line in old_file.readlines():
		every_line = every_line.replace("a", "4")
		every_line = every_line.replace("A", "4")
		every_line = every_line.replace("b", "6")
		every_line = every_line.replace("B", "8")
		every_line = every_line.replace("e", "3")
		every_line = every_line.replace("E", "3")
		every_line = every_line.replace("g", "9")
		every_line = every_line.replace("i", "1")
		every_line = every_line.replace("l", "1")
		every_line = every_line.replace("o", "0")
		every_line = every_line.replace("O", "0")
		every_line = every_line.replace("s", "5")
		every_line = every_line.replace("S", "5")
		every_line = every_line.replace("t", "7")
		every_line = every_line.replace("T", "7")
		new_file.write(every_line)

old_file.close()
new_file.close()
