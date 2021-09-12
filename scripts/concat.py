"""
Author:  <Michael Bardin>
Date:    07SEP2021
Contact: <mbardin2018@my.fit.edu>
"""

from sys import argv

if len(argv) == 3:
    output_file = argv[2]
else:
    output_file = argv[0][:-3]

old_file = open(argv[1], "r")
new_file = open("../dictionaries/" + output_file + ".dict", "w")

lines = old_file.readlines()

for i in lines:
    for j in lines:
        new_file.write(i.rstrip()+j.rstrip()+'\n')

old_file.close()
new_file.close()
