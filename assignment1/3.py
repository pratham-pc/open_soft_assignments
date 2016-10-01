t=input()
for i in range(0 , t):
	s=raw_input()
	o=''
	for j in s:
		v=ord(j)-96
		if v==1:
			o=o+'a'
		elif v==2:
			o=o+'b'
		elif v<=4:
			o=o+'d'
		elif v<=8:
			o=o+'h'
		else:
			o=o+'p'	
	print o

