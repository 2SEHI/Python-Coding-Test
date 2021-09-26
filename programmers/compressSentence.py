def solution(s):
    result = s
    for i in range(1, len(s) // 2 + 1):
        # 단위마다 압축된 결과를 저장할 변수
        new_s = ""  
        # 단위마다 문자열의 맨 앞부터 비교
        start = 0
        # target이 연속되는 수
        cnt = 1
        
        # target의 끝 인덱스가 문자열보다 작을 때까지 반복
        while start + i <= len(s) :
            # target 문자를 설정
            if cnt == 1:
                target = s[start:start + i]
            # target과 비교할 문자를 설정
            next = s[start + i: start + 2 * i]
            # target과 비교할 문자가 같을 경우 cnt 1증가
            if target == next:
                cnt += 1
            else:
                # target과 비교할 문자가 같지 않을 경우
                # cnt가 2이상인 경우에 cnt를 target앞에 연결하여 문자열 저장
                if cnt > 1:
                    new_s = new_s + str(cnt) + target
                else:
                    # cnt가 1인 경우 문자열에 target을 저장
                    new_s = new_s + target
                # target가 연속되지 않으므로 새로운 target을 설정하기 위해 cnt 초기화
                cnt = 1

            # 다음 비교 문자의 끝 인덱스가 문자열의 길이를 넘어가면 나머지 문자를 모두 이어 붙이기
            if start + 2 * i > len(s):
                new_s = new_s + s[start + i:len(s)]
            # 시작 인덱스를 단위만큼 증가시킴
            start = start + i
            # 압축문자열 출력
            # print(new_s)
        # 매 단위마다 압축문자열 비교하여 더 짧은 압축문자열을 저장
        if len(new_s) < len(result):
            result = new_s
    # 가장 짧은 압축문자열을 반환
    return len(result)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

