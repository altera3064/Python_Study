def korean_number():
	a = int(input())
	list = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구", "십"]
	print(list[a - 1])
	return list[a - 1]
	
korean_number()