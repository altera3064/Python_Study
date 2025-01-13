# your code goes here

newz = ['철수', '영희', '민수', '지현', '서연']
aiv = ['영희', '민수', '지수', '서연', '하나']
espa = ['철수', '지현', '지수', '서연', '나영']

na_result = []
count = 0

for nf in newz:
	if nf == aiv[count]:
		na_result.append(nf)
		print(nf)
		count = count + 1
count = 0	

for na in na_result:
	if na == espa[count]:
		na_result.pop()
		print(na_result)
		count = count + 1
			