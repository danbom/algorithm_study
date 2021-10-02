def solution(user_input):
	# 먼저 정답이 될 total_score 변수 만들기
	total_score = 0
	
	# 연속된 O의 개수 담을 변수 만들기
	continuity = 0
	
	# user_input에서 O 감지하기
	# user_input을 돌면서
	## user_input의 내용을 인덱싱해서 받기 위해 ㅣㅑㄴㅅ
	for i in list(user_input):
		# O를 만났을 때 continuity +=1
		# 큰따옴표 안에 넣기
		# 아아 list[i]가 아니라 i가 list 자체이기 때문에 그냥 i
		if i == "O":
			continuity += 1
			
		else:
			# 아 헐 이게 위치가 여기면 마지막이 O로 끝날 경우 continuity가 더해지지 않는다
			# total_score += continuity
			continuity = 0
			
		# 한 문제마다 total_score에 더해지도록 여기에 위치시킨다!
		total_score += continuity
			
	return total_score

if __name__=='__main__':
    user_input = input()
    if len(user_input) > 1000:
        print('입력 범위를 초과하였습니다.\n')
        exit(1)
    print(solution(user_input))
