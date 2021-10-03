'''
2019 카카오 블라인드 테스트
오픈채팅방
https://programmers.co.kr/learn/courses/30/lessons/42888
'''
def solution(record):
    # 행동과 아이드를 저장할 리스트
    inout_list = []
    # 행동과 아이디를 저장하기 위한 키
    inout = ["Enter", "Leave"]
    # 아이디와 닉네임을 저장할 dictionary
    id_nicname = {}
    # 아이디와 닉네임을 저장하기 위한 키
    enterChange = ["Enter", "Change"]

    # 유저의 행동과 아이디, 닉네임을 저장
    for r in record :
        # Enter 또는 Leave 일 경우 행동과 아이디을 리스트에 저장
        if r.split(" ")[0] in inout:
            inout_list.append((r.split(" ")[0], r.split(" ")[1]))
        # Enter 또는 Change 일 경우 아이디와 별명을 dictionary에 저장
        if r.split(" ")[0] in enterChange:
            id_nicname[r.split(" ")[1]] = r.split(" ")[2]

    # 채팅방에 출력할 메세지 리스트
    result = []
    # 유저가 방을 들어갈때와 나갈때 출력할 공통메세지
    printer = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}
    # Enter, Leave의 문자열을 저장
    enter, leave = "Enter", "Leave"

    # 채팅방에 출력할 메세지 저장하기
    for inout in inout_list:
        # 메세지에 id에 매칭하는 닉네임을 저장
        message = id_nicname[inout[1]]
        # 유저가 들어왔을 때, 출력할 메시지를 닉네임과 연결
        if inout[0] == enter :
            message = message + printer[enter]
        # 유저가 나갔을 때, 출력할 메시지를 닉네임과 연결
        elif inout[0] == leave :
            message = message + printer[leave]
        # 출력할 메시지를 리스트에 저장
        result.append(message)
    return result