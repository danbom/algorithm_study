# 입력
# 1번 톱니바퀴의 상태(12시 방향부터 시계방향 순서대로 / N극 0 / S극 1)
# 2번 톱니바퀴의 상태
# 3번 톱니바퀴의 상태
# 4번 톱니바퀴의 상태
# 회전 횟수 (1 <= K <=100)
# 회전시킨 톱니바퀴의 번호, 방향(시계방향 1 / 반시계방향 -1)

# 출력
# 1번 톱니바퀴 12시 S극이면 +=1
# 2번 톱니바퀴 12시 S극이면 +=2
# 3번 톱니바퀴 12시 S극이면 +=4
# 4번 톱니바퀴 12시 S극이면 +=8


from collections import deque

gear1 = deque(list(map(int, input())))
gear2 = deque(list(map(int, input())))
gear3 = deque(list(map(int, input())))
gear4 = deque(list(map(int, input())))
k = int(input())

def rotateGear(gear, dir):
    gear.rotate(dir);

for i in range(k) :

    gear_r, dir = map(int,input().split())

    # 첫번째 톱니바퀴가 돌 경우
    if (gear_r == 1) :
        # 두번째 톱니바퀴가 도는지 검사
        if (gear1[2] != gear2[6]):
            # 다른 극인 경우 두번째 톱니바퀴 돈다
            # 돌기 전에 세번째 톱니바퀴가 도는지 검사
            if (gear2[2] != gear3[6]):
                # 다른 극인 경우 세번째 톱니바퀴 돈다
                # 돌기 전에 네번째 톱니바퀴가 도는지 검사
                if (gear3[2] != gear4[6]):
                    # 다른 극인 경우 네번째 톱니바퀴 돈다
                    # 네번째 바퀴가 도는 방향은 항상 첫번째 톱니바퀴가 도는 방향과 반대
                    rotateGear(gear4, -dir)
                # 세번째 바퀴가 도는 방향은 항상 첫번재 톱니바퀴가 도는 방향과 같음
                rotateGear(gear3, dir)
            # 두번째 바퀴가 도는 방향은 항상 첫번재 톱니바퀴가 도는 방향과 반대
            rotateGear(gear2, -dir)
        # 첫번째 바퀴 돔
        rotateGear(gear1, dir)

    # 두번째 톱니바퀴가 돌 경우
    if (gear_r == 2) :
        # 첫번째 톱니바퀴가 도는지 검사
        if (gear1[2] != gear2[6]):
            # 다른 극인 경우 첫번째 톱니바퀴 돈다
            rotateGear(gear1, -dir)
        # 세번째 톱니바퀴가 도는지 검사
        if (gear2[2] != gear3[6]):
            # 다른 극인 경우 세번째 톱니바퀴 돈다
            # 돌기 전에 네번째 톱니바퀴가 도는지 검사
            if (gear3[2] != gear4[6]):
                rotateGear(gear4, dir)
            rotateGear(gear3, -dir)
        rotateGear(gear2, dir)

    # 세번째 톱니바퀴가 돌 경우
    if (gear_r == 3) :
        # 네번째 톱니바퀴가 도는지 검사
        if (gear3[2] != gear4[6]):
            # 다른 극인 경우 네번째 톱니바퀴 돈다
            rotateGear(gear4, -dir)
        # 두번째 톱니바퀴가 도는지 검사
        if (gear2[2] != gear3[6]):
            # 다른 극인 경우 두번째 톱니바퀴 돈다
            # 돌기 전에 첫번째 톱니바퀴가 도는지 검사
            if (gear1[2] != gear2[6]):
                rotateGear(gear1, dir)
            rotateGear(gear2, -dir)
        rotateGear(gear3, dir)

    # 네번째 톱니바퀴가 돌 경우
    if (gear_r == 4) :
        # 세번째 톱니바퀴가 도는지 검사
        if (gear3[2] != gear4[6]):
            # 다른 극인 경우 세번째 톱니바퀴 돈다
            # 돌기 전에 두번째 톱니바퀴가 도는지 검사
            if (gear2[2] != gear3[6]):
                # 다른 극인 경우 두번째 톱니바퀴 돈다
                # 돌기 전에 첫번째 톱니바퀴가 도는지 검사
                if (gear1[2] != gear2[6]):
                    # 다른 극인 경우 첫번째 톱니바퀴 돈다
                    # 첫번째 바퀴가 도는 방향은 항상 네번째 톱니바퀴가 도는 방향과 반대
                    rotateGear(gear1, -dir)
                # 두번째 바퀴가 도는 방향은 항상 네번재 톱니바퀴가 도는 방향과 같음
                rotateGear(gear2, dir)
            # 세번째 바퀴가 도는 방향은 항상 첫번재 톱니바퀴가 도는 방향과 반대
            rotateGear(gear3, -dir)
        # 네번째 바퀴 돔
        rotateGear(gear4, dir)

print(gear1[0]+gear2[0]*2+gear3[0]*4+gear4[0]*8)
