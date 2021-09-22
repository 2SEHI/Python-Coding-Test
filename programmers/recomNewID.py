'''
2021 카카오 블라인드 테스트
신규 아이디 추천
https://programmers.co.kr/learn/courses/30/lessons/72410
'''
def solution(new_id):
    # 1단계 : 소문자로 변환
    new_id = new_id.lower()

    # 2단계 : - _ . 소문자 이외는 제거
    useword = ['-', '_', '.']
    step2 = [i for i in new_id if i.isalnum() or i in useword]

    # 3단계 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    step3 = []
    for i, s in enumerate(step2):
        if len(step3) > 0:
            if step3[-1] == '.' and s == '.':
                continue
        step3.append(s)
    new_id = ''.join(step3)

    # 4단계 : 처음이나 마지막에 있는 . 제거
    new_id = new_id.strip('.')

    # 5단계 : 빈문자열이면 a 대입
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) > 15:
        # 6단계: new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
        new_id = new_id[:15]
    # 양끝의 . 제거
    new_id = new_id.strip('.')

    # 7단계 : new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]
    return new_id