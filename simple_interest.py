# your code goes here
def simple_interest(p,r,t):
	result = p*r*t
	return result
	
def simple_interest_amount(p,r,t):
	result = p * (1 + r*t)
	return result
	
print(simple_interest(10000000, 0.03875, 5))
print(simple_interest(1100000, 0.05, 5/12))

print(simple_interest_amount(10000000, 0.03875, 5))
print(simple_interest_amount(1100000, 0.05, 5/12))
