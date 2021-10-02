# programmers에 돌릴 때는 print문을 빼고 돌려야 됨
def solution(board, moves):
    stack = []
    answer = 0
    # moves 배열 크기만큼 순회
    while moves :
        # moves배열의 맨 앞 요소를 인덱스로 저장
        idx  = moves.pop(0)-1
        # 인형을 저장할 변수
        target = 0
        # 크레인 배열 만큼 순회
        for b in board :
            # 빈칸이 아니면 인형변수에 저장하고 크레인에서 빈칸으로 저장
            if b[idx] != 0:
                target, b[idx] = b[idx], 0
                break
        # 인형바구니 stack이 비어있지 않다면 target과 stack의 마지막 요소를 비교
        if len(stack) > 0 :
            if stack[-1] == target:
                print("target(", target, ") == stack의 마지막 요소(", stack[-1],") 이므로 제거 => ", end=" ")
                stack.pop()
                answer += 2
            else :
                print("target(", target, ") != stack의 마지막 요소(", stack[-1],") 이므로 저장 => ", end=" ")
                stack.append(target)
        else :
            # 인형바구니 stack이 비어있다면 target을 stack에 저장
            print("stack(empty) target (", target,") 저장 => ", end=" ")
            stack.append(target)
        print("stack의 상태 : ", stack, end="\n")
    return answer