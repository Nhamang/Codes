tot = 0
a = 1
b = 1
c = 2
tmp = 0

while (c < 4000000):
	if(c %2 == 0):
		tot+=c
		
	tmp = c
	a = b
	b = c
	c = a+b

print (tot)