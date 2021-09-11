def solution(absolutes, signs):
    answer = sum([-absolutes[i] if signs[i] == False else absolutes[i] for i in range(len(absolutes)) ])
    return answer