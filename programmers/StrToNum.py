'''
2021 카카오 채용연계형 인턴십
숫자 문자열과 영단어
https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
'''
def solution(answer):
    g = {0:'zero', 1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    for key, value in g.items():
        answer = answer.replace(value, str(key) )
    return int(answer)