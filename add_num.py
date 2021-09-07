import sys
print (sys.argv)

file_in = open(sys.argv[1], 'r')
file_out = open(sys.argv[2], 'w')

text1 = file_in.read().split('\n')
text2 = text1

for i in text1:
	if(len(i)>7):
		for j in range(0,10):
			for k in range(0,10):
				file_out.write(i+str(j)+str(k)+'\n')


file_in.close()
file_out.close()