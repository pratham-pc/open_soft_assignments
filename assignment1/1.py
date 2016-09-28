#program to search common substring in A and B of length n

A=raw_input("Enter String A:")
B=raw_input("Enter String B:")
n=input("Enter n:")

print "%s\t%s\t%s" % ("Substring" , "Starting position in A" , "Starting position in B")

print

for i in range(0 , len(A)-n+1):
	for j in range(0 , len(B)-n+1):
		if A[i:i+n]==B[j:j+n] :
			print "%s\t%d\t%d" % (A[i:i+n] , i+1 , j+1)
