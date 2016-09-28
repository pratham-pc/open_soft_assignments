n=input()
A={}
for i in range(0 , n):
	a=b=''
	cnt=0
	c=raw_input()
	for j in c:
		if cnt==0 :
			if j!=' ':
				a=a+j
			else:
				cnt=1
		else:
			b=b+j	
	if a.lower()=='space':
		a=' '
	A[b]=a;
encoded=raw_input()
start=0
end=0
print A
print encoded
decoded=""
for i in range(0,len(encoded)):
	end=i
	if A.has_key(encoded[start:end+1]):
		decoded=decoded+A[encoded[start:end+1]]
		start=end+1
print decoded
