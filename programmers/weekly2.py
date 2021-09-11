def solution(scores):
    trans = list(zip(*scores))
    myself = [scores[i][i] for i in range(len(scores))]

    mean_list = []
    for m, t in zip(myself, trans):
        s = sum(t)
        cnt = len(t)
        if (m == max(t)) & (t.count(max(t)) == 1):
            s = s - max(t)
            cnt -= 1
        if (m == min(t)) & (t.count(min(t)) == 1):
            s = s - min(t)
            cnt -= 1
        mean_list.append(s / cnt)

    li = []
    for score in mean_list:
        if score >= 90:
            li.append('A')
        elif 80 <= score < 90:
            li.append('B')
        elif 70 <= score < 80:
            li.append('C')
        elif 50 <= score < 70:
            li.append('D')
        else:
            li.append('F')

    return ''.join(li)