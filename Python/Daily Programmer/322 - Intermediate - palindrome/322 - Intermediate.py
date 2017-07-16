from math import pow
#Find to largest palindrome with both factors of n-size

n = int(input("Input integer: "))
maxN = int(pow(10, n))
minN = int(pow(10, n-1))
maxPal = 0
integer1 = 0
integer2 = 0

def isPalindrome(test):
    return (test == test[::-1])


for i in range(maxN, minN, -1):
    if(i*i < maxPal):
        break
    for j in range(maxN, minN, -1):
        if(isPalindrome(str(i*j)) and (j*i) > maxPal):
            maxPal = (i*j)
            integer1 = i
            integer2 = j

print maxPal, " is the product ", integer1, "x", integer2
