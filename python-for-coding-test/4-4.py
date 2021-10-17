'''
이것이 코딩 테스트다 파이썬
p118
3.게임 개발
'''


# x,y : 위치 좌표
# pd : 현재 방향
# dt : 이동위치 맵
# arr : 육지, 바다 맵
def solution(x, y, pd, dt, arr):
    # 방문한 칸의 개수를 저장할 변수
    result = 1
    # 현재의 위치를 가본 곳이라고 저장
    dt[x][y] = 1
    # Up, Right, Down, Left
    # 북, 서, 남, 동
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 회전 횟수
    turn_time = 0

    while True:
        # 현재의 방향을 1감소
        pd -= 1
        # 0보다 작으면 3으로 저장
        if pd < 0:
            pd = 3
        # 이동할 위치 저장
        sx = x + direction[pd][0]
        sy = y + direction[pd][1]
        # 안가본 곳이면서 육지인 경우
        if arr[sx][sy] == 0 and dt[sx][sy] == 0:
            # 이동 칸의 개수를 증가
            result += 1
            # 이동 위치를 갱신
            x, y = sx, sy
            # 이동위치 맵에 가본 곳이라고 저장
            dt[x][y] = 1
            # 이동했으므로, 이동 횟수를 0으로 초기화
            turn_time = 0

        else:
            # 가본 곳이거나 바다인 경우
            # 회전 횟수를 증가
            turn_time += 1
        # 4면이 모두 가본 곳이거나 바다인 경우
        if turn_time == 4:
            # 방향을 유지한채 뒤로 한칸 이동
            sx = x - direction[pd][0]
            sy = y - direction[pd][1]

            # 뒤가 바다인 경우, 종료
            if arr[sx][sy] == 1:
                break
            else:
                # 뒤가 바다가 아닌 경우, 회전횟수를 초기화
                turn_time = 0
                x, y = sx, sy
    return result


def main():
    # 2차 배열의 크기 입력받기
    n, m = tuple(map(int, input().split()))

    # 캐릭터의 현재 위치(x,y)와 방향
    x, y, pd = map(int, input().split())

    # n*m 크기의 2차 배열을 생성
    dt = [[0] * m for _ in range(n)]

    # 육지와 맵을 저장할 배열
    arr = []
    # 행의 수만큼 육지(0), 바다(1)을 입력받기
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    # 전체 맵 정보를 입력받기
    result = solution(x, y, pd, dt, arr)
    # 이동한 칸의 수 출력
    print(result)

if __name__ == "__main__":
    main()
