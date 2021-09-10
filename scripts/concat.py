"""
Author:  <Michael Bardin>
Date:    07SEP2021
Contact: <mbardin2018@my.fit.edu>
"""

from sys import argv

old_file = open(argv[1], "r")
new_file = open("../dictionaries/" + argv[0][:-3] + ".dict", "w")

lines = old_file.readlines()

for i in lines:
	for j in lines:
		new_file.write(i+j+'\n')

old_file.close()
new_file.close()
