def solution(numbers, hand):
    # key_pad의 좌표 저장
    k = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]]
    # 왼쪽 손가락의 위치
    lf = [3, 0]
    # 오른쪽 손가락의 위치
    rf = [3, 2]
    # 사용한 손가락 방향
    result = ""
    # 입력할 key만큼 순회
    for n in numbers:
        # 오른쪽 손가락
        if n in [3, 6, 9]:
            # 오른쪽 손가락의 위치를 저장
            rf = k[n]
            # 사용한 손가락을 저장
            result = result + "R"
        elif n in [1, 4, 7]:
            lf = k[n]
            # 사용한 손가락을 저장
            result = result + "L"
        else:
            # 왼쪽 손가락과 눌러야할 key의 거리
            ld = abs(k[n][0] - lf[0]) + abs(k[n][1] - lf[1])
            # 오른쪽 손가락과 눌러야할 key의 거리
            rd = abs(k[n][0] - rf[0]) + abs(k[n][1] - rf[1])
            # 오른쪽 손가락과 눌러야할 key의 거리가 더 짧은 경우
            if ld > rd:
                # 오른쪽 손가락의 좌표 이동
                rf = k[n]
                # 오른쪽 손가락을 결과에 저장
                result = result + "R"
            elif rd > ld:
                # 왼쪽 손가락의 좌표 이동
                lf = k[n]
                # 왼쪽 손가락을 결과에 저장
                result = result + "L"
            else:
                # 거리가 같은 경우
                # 오른손잡이인 경우
                if hand == "right":
                    # 오른쪽 손가락의 좌표 이동
                    rf = k[n]
                    # 오른쪽 손가락을 결과저장
                    result = result + "R"

                else:
                    # 왼쪽 손가락의 좌표 이동
                    lf = k[n]
                    # 왼쪽 손가락을 결과저장
                    result = result + "L"
    # 결과 반환
    return result