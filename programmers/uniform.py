def solution(n, lost, reserve):
    # lost에서 reserve와 중복된 사람을 제거하여 저장
    lost_reverse = sorted([i for i in lost if i not in reserve])
    # reserve에서 lost와 중복된 사람을 제거하여 저장
    reverse_lost = sorted([i for i in reserve if i not in lost])
    # 체육복을 빌린 사람을 담는 배열
    borrow_list = []

    for lo in lost_reverse:
        for re in reverse_lost:
            # 도난 당한 사람과 여분이 있는 사람을 순회하며 빌려줄 수 있는지(앞과 뒤에 있는지) 체크
            if re - 1 <= lo <= re + 1:
                # borrow_list 배열에 담기
                borrow_list.append(lo)
                # 여유분을 빌려준 사람을 제거하기
                reverse_lost.remove(re)
    # 수업을 들을 수 있는 사람 = 전체사람수 - 도난당한 사람 + 체육복을 빌린 사람
    answer = n - len(lost_reverse) + len(borrow_list)
    return answer