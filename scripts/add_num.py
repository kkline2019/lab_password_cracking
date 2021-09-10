"""
Author:  <Michael Bardin>
Date:    07SEP2021
Contact: <mbardin2018@my.fit.edu>
"""

from sys import argv

file_in = open(argv[1], 'r')
file_out = open("../dictionaries/" + argv[0][:-3] + ".dict", "w")

text1 = file_in.read().split('\n')
text2 = text1

for i in text1:
	if(len(i)>7):
		for j in range(0,10):
			for k in range(0,10):
				file_out.write(i+str(j)+str(k)+'\n')

file_in.close()
file_out.close()
