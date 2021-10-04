'''
위클리 챌린지 8주차
최소직사각형
https://programmers.co.kr/learn/courses/30/lessons/86491
'''

# 처음에 제출한 풀이
# 통과는 했지만 실행시간이 좀 긴 것같음
def solution(sizes):
    # 높은 길이는 0번 인덱스쪽에, 작은 길이는 1번 인덱스쪽에 배치
    changed = [[x[0],x[1]] if x[0] >= x[1] else [x[1],x[0]] for x in sizes ]
    # 0번인덱스와 1번 인덱스 각각의 그룹으로 list만들기
    trans = list(zip(*changed))
    # 0번 인덱스 중에서 가장 긴 길이 저장
    w = max(trans[0])
    # 1번 인덱스 중에서 가장 긴 길이 저장
    h = max(trans[1])
    # 가장 긴 길이를 곱하여 반환
    return w * h

# 다시 제출한 풀이;
# 위에꺼보다 수행속도가 약간 조금더 빠름
def solution(sizes):
    # 높은 길이는 0번 인덱스쪽에, 작은 길이는 1번 인덱스쪽에 배치
    sizes = [[w, h] if w >= h else [h, w] for w, h in sizes ]
    w = max(sizes, key = lambda x : x[0])
    h = max(sizes, key = lambda x : x[1])

    # 가장 긴 길이를 곱하여 반환
    return  w[0] * h[1]