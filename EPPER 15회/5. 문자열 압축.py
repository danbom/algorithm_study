def solution(str):
	# 맨 앞에 0인지 1인지 구별할 변수
	header = ""
	
	# ABC 담을 배열
	answer = []
	
	# 문자열의 맨 앞이 1인 경우 1 붙이기
	if str[0] == "1":
		header = "1"
		
	# 연속되는 0 또는 1 개수 담을 변수
	# 문자 -> 숫자 : ord
	# 숫자 -> 문자 : chr
	continuity = ord('A')
	
	# input 문자열 담을 list
	list = []
	
	for i in str:
		# input 문자열을 list에 append
		list.append(i)
		
		# 문자열의 길이가 1인 경우 비교할 필요 없음
		if (len(list) != 1):
			index = len(list)
			# 0, 1이 연속될 경우
			if (list[index-1] == list[index-2]):
				continuity +=1
			# 0, 1이 연속되지 않을 경우
			else :
				# 정답 배열에 continuity를 문자로 변환해서 append
				answer.append(chr(continuity))
				# continuity 초기화
				continuity = ord('A')
		
		# 마지막 문자 출력하기 위해
		if (len(str) == len(list)) :
			answer.append(chr(continuity))
				
	# ''.join 으로 answer 배열 문자열로 만들기
	return header + ''.join(answer)
				
				
	

str = input()
print(solution(str))
