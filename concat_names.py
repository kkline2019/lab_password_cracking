from datetime import datetime

now = datetime.now()
now = now.strftime("%H%M%S")
new_file = argv[1] + str(now)

current_password_list = open(argv[1], "r")

new_list = open(new_file, "w")

for every_password in current_password_list.readlines():
	for every_name in current_password
	every_password = every_password.replace(argv[2], argv[3])
	new_list.write(every_password)

current_password_list.close()
new_list.close()
