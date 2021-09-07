from sys import argv
from datetime import datetime

new_file = argv[1] + "_replace"

current_password_list = open(argv[1], "r")

new_list = open(new_file, "w")

for every_password in current_password_list.readlines():
	every_password = every_password.replace(argv[2], argv[3])
	new_list.write(every_password)

current_password_list.close()
new_list.close()
