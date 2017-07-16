def findPalindrome():
	result = 0
	for num in range(999, 99, -1):
		for num2 in range(999, 99, -1):
			if(isPalindrome(str(num*num2)) == 1 and ((num*num2) > result)):
			result = (num*num2)
	print result


def isPalindrome(num):
	if(num == (num[::-1])):
		return 1
	return 0
	
findPalindrome()