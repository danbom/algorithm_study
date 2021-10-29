def solution(new_id):
    # 1단계 : 대문자 -> 소문자
    new_id = new_id.lower()
    # 2단계 : a-z, 0-9, -, _, . 제외 삭제
    answer = []
    for i in new_id:
        if i in "abcdefghijklmnopqrstuvwxyz0123456789-_.":
            answer += i
    # 3단계 : . 두번 이상이면 하나로 치환
    continuity = 0
    for i in range(len(answer)):
        if answer[i]==".":
            continuity += 1
            if continuity > 1:
                answer[i] = ""
        else:
            continuity = 0
    # 4단계 : . 가 처음이나 끝일때 제거
    answer = "".join(answer)
    if answer[0] == ".":
        answer = answer[1:]
    elif answer[len(answer)-1] == ".":
        answer = answer[:len(answer)-1]
    # 5단계 : 빈 문자열이 된 경우 "a" 대입
    if answer == "":
        answer = "a"
    # 6단계 : 16자 이상이면 첫 15자 이외 모두 삭제 + 4단계
    if len(answer) >15:
        answer = answer[:15]
    if answer[len(answer)-1] == ".":
        answer = answer[:len(answer)-1]
    # 7단계 : 2자 이하면 마지막 문자를 길이 3될때까지 반복
    if len(answer) <3:
        answer += answer[-1]*(3-len(answer))
    return answer
