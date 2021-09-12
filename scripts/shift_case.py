"""
Author:  Kyle
Date:    07SEP2021
Contact: Kyle
"""

from sys import argv # Used for command line arguments

if len(argv) == 3:
    output_file = argv[2]
else:
    output_file = argv[0][:-3]

old_file = open(argv[1], "r")                                    # The original dictionary
new_file = open("../dictionaries/" + output_file + ".dict", "w") # The new altered dictionary

for every_line in old_file.readlines():
	new_line = ""
	for every_char in range(len(every_line)):
		if not every_char % 2:
			new_line += every_line[every_char].upper()
		else:
			new_line += every_line[every_char].lower()
	new_file.write(new_line)

old_file.close()
new_file.close()
