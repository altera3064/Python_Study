def palindrome(x):
	reversed_x = x[::-1]
	result = True
	if x != reversed_x:
			result = False
	return result
	
print(palindrome("anana"))
	
		
