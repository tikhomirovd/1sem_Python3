det,d,dk,signum = 1, [], [], 1
n=int(input('yyy'))
#d = [[1,1/3,3**(-2)],[3**(-3),3**(-4),3**(-5)],[3**(-6),3**(-7),3**(-8)]]
#dk = [[1,1/3,3**(-2)],[3**(-3),3**(-4),3**(-5)],[3**(-6),3**(-7),3**(-8)]]
for i in range(n):
	d.append([])
	dk.append([])
	for i2 in range(n):
		d[i].append(float(input('jj ')))
		dk[i].append(d[i][i2])
	
for i in range(n-1):
	if d[i][i] == 0:
		for j in range(i+1,n):
			if d[j][i] != 0:
				d[i],d[j] = d[j],d[i]
				signum *= -1
	if d[i][i] == 0:
		det = 0
		break
	for i2 in range(i+1,n):
		k = -d[i2][i]/d[i][i]
		for i3 in range(i,n):d[i2][i3]=d[i2][i3]+d[i][i3]*k
	det *= d[i][i]
det *= d[n-1][n-1]*signum
print('{:3.5f}'.format(det))

def minor(m):
	de = 0
	lm = len(m)
	if lm == 2: return m[0][0]*m[1][1] - m[0][1]*m[1][0]
	else:
		for i in range(lm):
			mi = []
			for i2 in range(lm):
				if i != i2: mi.append(m[i2][1:])
			de += (-1)**i*m[i][0]*minor(mi)	
	return de
print ('{:3.5f}'.format(minor(dk)))

