from collections import Counter


def solution(lottos, win_nums):
    best_rank = 1
    worst_rank = 6

    # 확실한 당첨 번호의 개수
    atari = len([i for i in win_nums if i in lottos])

    # zero의 개수를 구하기
    zero_cnt = lottos.count(0)

    if zero_cnt == 0:
        best_rank = rank(atari)
        worst_rank = rank(atari)
    elif 1 <= zero_cnt < 6:
        worst_rank = rank(atari)
        best_rank = rank(zero_cnt + atari)
    return [best_rank, worst_rank]


# ranking 구하는 함수
def rank(count):
    ranking = 6
    if count == 2:
        ranking = 5
    elif count == 3:
        ranking = 4
    elif count == 4:
        ranking = 3
    elif count == 5:
        ranking = 2
    elif count == 6:
        ranking = 1
    return ranking