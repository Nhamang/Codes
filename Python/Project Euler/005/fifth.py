def isDevisable(num):
	for n in range(11, 20):
		if((num%n) != 0):
			return False
	return True
	
num = 2520

while not isDevisable(num):
	num += 2520
	
print (num)

#232792560