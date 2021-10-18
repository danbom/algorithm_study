def solution(a, b):
    # 1월 31일 / 2월 29일 / 3월 31일 / 4월 30일 / 5월 31일 / 6월 30일 / 
    # 7월 31일 / 8월 31일 / 9월 30일 / 10월 31일 / 11월 30일 / 12월 31일 
    
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    
    if a==1:
        return day[b%7]
    elif a==2:
        return day[(31+b)%7]
    elif a==3:
        return day[(60+b)%7]
    elif a==4:
        return day[(91+b)%7]
    elif a==5:
        return day[(121+b)%7]
    elif a==6:
        return day[(152+b)%7]
    elif a==7:
        return day[(182+b)%7]
    elif a==8:
        return day[(213+b)%7]
    elif a==9:
        return day[(244+b)%7]
    elif a==10:
        return day[(274+b)%7]
    elif a==11:
        return day[(305+b)%7]
    elif a==12:
        return day[(335+b)%7]
    
