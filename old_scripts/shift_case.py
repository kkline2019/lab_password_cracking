from sys import argv
from datetime import datetime

now = datetime.now()
now = now.strftime("%H%M%S")
new_file = argv[1] + "_shift"

file = open(argv[1], "r")
new_file = open(new_file, "w")

for every_line in file.readlines():
	new_line = ""
	for every_char in range(len(every_line)):
		if not every_char % 2:
			new_line += every_line[every_char].upper()
		else:
			new_line += every_line[every_char].lower()
	new_file.write(new_line)

file.close()
new_file.close()
