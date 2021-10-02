# -*- coding: utf-8 -*-
# 프로그래머스에서는 main함수 및 입출력문이 필요하지 않습니다. 대신 solution함수만 작성하면 됩니다.

def solution(r, c, zr, zc, words):
	answer = []
	
	# 원본 크기 r c
	# 확대 크기 zr zc
	
	# words 에서 행을 어떻게 구분하지
	# 아 words[i][j] 형식
	
	# 먼저 words[0][0] ~ words[0][n]을 zc번 반복 - 1번째 행
	# 그다음 1번째 행을 zr번 반복
	# 위를 반복하는 방식?
	# 행, 열 반복
	## 아 여기서 n은 c구나
	
	# 먼저 정답을 넣을 배열을 만들고
	# 파이썬은 ; 안쓴다 ..
	answer = []
	
	# 행을 담을 배열도 만들고
	## 아님! 한 행이기 때문에 그냥 string으로 받아도됨
	# tmp = ""
	
	# 파이썬의 반복문
	for i in range(r):
		# 여기에 tmp 만들자
		tmp = ""
		
		for j in range(c):
			
			for k in range(zc):
					tmp += words[i][j]
			
		# 아 여긴 이제 열 정보가 필요없고 결과적으로 나온 tmp를
		# zr만큼 반복해주면 되는거니까 이 위치
		for m in range(zr):
				# 배열에 더할땐 arr.append(tmp) 형식
				answer.append(tmp)
			
				

	return answer

r,c,zr,zc = input().split()
r=int(r)
c=int(c)
zr=int(zr)
zc=int(zc)

words=[]
	
for i in range(r):
	temp=input()
	if(len(temp)>c):
		print("입력 범위를 초과하였습니다.\n")
		exit(1)
	words.append(temp)

answer = solution(r,c,zr,zc,words);
  
for i in range(r*zr):
	print(answer[i])
