import sys

# Argument 1 - file name
fi = open(str(sys.argv[1]), "r")
fo = open("pass_w_concat.txt", "w")

words1 = fi.read().split('\n')
words2 = words1

for start_word in words1:
	for end_word in words2:
		fo.write(start_word[:3] + end_word[:3] + "\n")

fi.close()
fo.close()