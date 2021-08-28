##
point = input('현재 위치를 입력하세요 : ')
# 현재 위치
px = point[0]
py = point[1]

# 체스판의 위치 리스트
cols = ['a','b','c','d','e','f','g','h']
rows = ['1','2','3','4','5','6','7','8']

# 현재위치의 인덱스
px = cols.index(point[0])
py = rows.index(point[1])

# 이동 가능한 패턴의 이동좌표
# 'LU', 'LD', 'RU', 'RD','UL','UR', 'DL','DR'
dx = [-2, -2, 2, 2, -2, -2, 2, 2]
dy = [-1, 1, -1, 1, -1, 1, -1, 1]

# 경우의 수
count = 0

# 이동 가능 패턴을 순회하며 확인
for i in range(len(dx)):
    # 이동 가능 패턴이 체스판을 넘어가는지 확인하고 넘어가면 경우의 수를 증가하지 않고 다음 패턴확인
    if (px + dx[i]) < 0 or (py + dy[i]) <0 or (px + dx[i]) > len(cols) or  (py + dy[i]) > len(cols):
        continue
    # 경우의 수를 증가
    count += 1
# 경우의 수 출력
print(count)