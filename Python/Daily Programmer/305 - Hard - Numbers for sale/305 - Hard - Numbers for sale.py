from itertools import combinations_with_replacement
from math import factorial
count = 0

for i in range(0, 6):
    count += ((-1)**i) * (factorial(15)/(factorial(i) * factorial(15-i))) * (factorial((83 - (i*10))) / (factorial(14) * factorial((83-(i*10)-14))))

print (count)
