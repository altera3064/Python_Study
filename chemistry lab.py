# your code goes here

user_input = input()

minimum, maximum = user_input.split()
minimum, maximum = int(minimum), int(maximum)

user_input2 = input()
status = user_input2.split()

for i in status:
	if minimum <= int(i) and int(i) <= maximum:
		print("Nothing to report")
	elif int(i) == -999:
		break
	elif int(i) < minimum or int(i) > maximum:
		print("Alert")
		break


