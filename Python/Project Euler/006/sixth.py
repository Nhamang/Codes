tot1 = 0
tot2 = 0
sumtot = 0

for num in range(1, 101):
	tot1 += (num*num)
	tot2 += num
	
tot2 *= tot2
sumtot = tot2-tot1

print("tot1: ", tot1, " tot2: ", tot2, " sumtot: ", sumtot)
