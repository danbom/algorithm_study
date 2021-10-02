# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

## 돈의개수 n과 크기가 n인 수열 M이 주어졌을 때 
## 주울 수 있는 최대 돈을 구하는 함수
def solution(n, M):
	
	# 다이나믹 프로그래밍(dp)
	# 동적계획법
	
	# 마지막 돈을 기준으로 있을 수 있는 경우는 세가지
	# o x o
	# x o o
	# (지금까지의 최대값) x
	
	# 정리하면 i번째를 기준으로 한다면
	# max[i-2] + i번째돈
	# max[i-3] + (i-1)번째돈 + i번째돈
	# max[i-1]
	
	best = [0]*30001
	best[0] = M[0]
	best[1] = M[0] + M[1]
	best[2] = max(best[1], M[0]+M[2], M[1]+M[2])
	
	# for문 range(a,b) 에서 b는 포함되지 않는다
	for i in range(3, len(M)):
		best[i] = max(best[i-2]+M[i], best[i-3]+M[i-1]+M[i], best[i-1])
		
	return best[len(M)-1]
	
def main():
	n = int(input())
	M = [int(x) for x in input().split()]
	print(solution(n,M))
	
	
main()
