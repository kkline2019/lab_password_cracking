"""
Author:  <team member name>
Date:    07SEP2021
Contact: <email>
"""

from sys import argv

if len(argv) == 3:
    output_file = argv[2]
else:
    output_file = argv[0][:-3]

old_file = open(argv[1], "r")
new_file = open("../dictionaries/" + output_file + ".dict", "w")

lines = old_file.readlines()

for every_line1 in lines:
    for every_line2 in lines:
        new_file.write(every_line1[:3] + every_line2[:3] + "\n")

old_file.close()
new_file.close()
