def solution(n,r,c):
    mid = (2**n)//2;
    dist = 0
    while mid > 0:
        while mid > 1:
            if (r<mid and c<mid):
                dist += 0
            elif (r<mid and c>=mid):
                dist += mid**2
                c -= mid
            elif (r>=mid and c<mid):
                dist += (mid**2)*2
                r -= mid
            elif (r>=mid and c>=mid):
                dist += (mid**2)*3
                r -= mid
                c -= mid
            mid = mid//2
            
        if mid == 1:
            if (r==0 and c==0):
                dist += 0
            elif (r==0 and c==1):
                dist += 1
            elif (r==1 and c==0):
                dist += 2
            elif (r==1 and c==1):
                dist += 3
                
        print(dist)
        return dist

n, r, c = map(int, input().split())

solution(n,r,c)
