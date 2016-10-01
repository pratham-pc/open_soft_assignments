t=input()
while t>0:
	n=input()
	b=raw_input().split()
	A={}
	val=1
	for i in b:
		A[i]=1
	for i in b:
		for j in range(0,len(i)):
			if A.has_key(i[0:j]):
				val=0
	if val==1:
		print "YES"
	else:
		print "NO"
	t-=1
