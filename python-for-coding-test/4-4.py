'''
이것이 코딩 테스트다 파이썬
p118
3.게임 개발
'''

# 2차 배열의 크기 입력받기
n, m = tuple(map(int, input().split()))
# 캐릭터의 현재 위치(x,y)와 방향
x, y, pd = map(int, input().split())

# n*m 크기의 2차 배열을 생성
dt = [[0] * m for i in range(n)]
for i in range(len(dt)):
    dt[i] = list(map(int, input().split()))

# 방문한 칸의 개수를 저장할 변수
result = 1

# Up, Right, Down, Left
# 북, 서, 남, 동
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    # 현재 위치를 방문 처리
    dt[x][y] = 1
    # 모두 안가본 곳으로 초기 설정
    exp = [0] * 4

    # 4가지 방향에 대해 이동가능한지 확인
    for i in range(len(direction)):

        # 현재 방향에서 왼쪽 방향으로 회전
        pd -= 1
        # 현재의 방향이 북쪽이면 서쪽으로 변경
        if pd < 0:
            pd = 3
        # 회전된 방향이 이동가능한 경우, 이동
        sx = x + direction[pd][0]
        sy = y + direction[pd][1]
        print("이동위치: ", sx, sy)

        # 육지인 경우
        if 0 <= sx < n and 0 <= sy < m and dt[sx][sy] == 0:
            x, y = sx, sy
            result += 1
            break
        else:
            exp[pd] = 1

    # 이동가능한 방향이 없는 경우
    if sum(exp) == 4:
        # 뒤쪽 위치
        sx = x - direction[pd][0]
        sy = y - direction[pd][1]

        # 뒤쪽 위치가 바다인 경우, 종료
        if sx < 0 or sy < 0 or sx >= n or sy >= m or dt[sx][sy] == 1:
            print("break")
            break
        else:
            # 바다가 아닌 경우,
            result += 1
            x, y = sx, sy
        print('현재위치 : ', x, y)

# 이동칸의 개수를 출력
print(result)
