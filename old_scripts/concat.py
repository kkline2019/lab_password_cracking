import sys
print (sys.argv)

file_in = open(sys.argv[1], 'r')
file_out = open(sys.argv[2], 'w')

text1 = file_in.read().split('\n')
text2 = text1

#print([text1])

print(text1[0]+text2[0])

concat=[]

for i in text1:
	for j in text2:
		#concat.append(i+j)
		file_out.write(i+j+'\n')


file_in.close()
file_out.close()