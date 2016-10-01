def dec_to_bin(x):
    return bin(x)[2:]
def fun(a , r):
	mini=1
	minhd=100
	pos=0
	for i in a:
		v=i^r
		cnt=0
		for j in dec_to_bin(v):
			if j=='1':
				cnt+=1
		if cnt<minhd:
			minhd=cnt
			mini=pos
		pos+=1
	return (minhd , mini)
a=[857,958,838,606,348,185]
r=862
print fun(a , r)
a=[1,2,3,4,0,47,16]
r=7
print fun(a , r)
a=[719,101,1008,767]
r=510
print fun(a , r)

