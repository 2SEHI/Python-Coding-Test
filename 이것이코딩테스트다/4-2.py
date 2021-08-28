# 시각
N = int(input('시간을 입력하세요'))
# 3이 포함된 횟수 초기화
count = 0
# 시간, 분, 초를 증기하며 3이 포함된 시간 찾기
# 시간
for hour in range(N+1):
    # 분
    for m in range(60):
        # 초
        for s in range(60):
            # 시분초를 문자열로 변환하여 이어준다
            time = str(hour) + str(m) + str(s)
            # 시간에 3이 포함되면 횟수를 1 증가
            if '3' in time:
                count+=1
# 3치 포함된 횟수 출력
print(count)