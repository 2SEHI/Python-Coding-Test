# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 두수의 합을 list로만 구현할 경우
class Solution:
    def addTwoNumbers(self, l1, l2):
        # 순서 뒤집기
        l1.reverse()
        l2.reverse()
        # 두 수의 합을 담을 리스트
        answer = []
        # 다음 자릿수로 넘어갈 숫자
        extra = 0
        # 리스트의 길이가 0인지 체크하는 함수
        # 0이면 False, 0아니면 True
        len_check = lambda x: len(x) != 0

        # 두 리스트의 길이가 0이 될때까지 반복
        while l1 or l2:
            # l1리스트의 기본값
            a1 = 0
            # l1리스트의 길이가 0이 아닐 경우
            if len_check(l1):
                # l1리스트로부터 값을 추출함
                a1 = l1.pop()

            # l2리스트의 기본값
            a2 = 0
            # l2리스트의 길이가 0이 아닐 경우
            if len_check(l2):
                # l2리스트로부터 값을 추출함
                a2 = l2.pop()

            # 두수의 합과 초과된 값을 더함
            add = a1 + a2 + extra
            # 더한 값이 10보다 크거나 같으면, 다음 자릿수에 1을 넘기고
            # 더한값에서 10을 뺀다
            if add >= 10 :
                add = add - 10
                extra = 1
            # 결과리스트에 두수를 더한 값을 저장
            answer.append(add)
        # 초과값이 남았으면 결과리스트에 저장
        if extra :
            answer.append(extra)
        return answer


    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 다음 자릿수로 넘어갈 숫자
        extra = 0
        #
        root = head = ListNode(0)
        while l1 or l2:
            a1, a2 = 0, 0
            if l1 :
                a1 = l1.val
                l1 = l1.next
            if l2:
                a2 = l2.val
                l2 = l2.next

            plus = a1 + a2 + extra

            if plus >= 10:
                plus = plus -10
                extra = 1

            head.next = ListNode(plus)
            head = head.next
        if extra :
            head.next = ListNode(extra)

        return root.next


if __name__ == '__main__':
    # 1.list로 구현 : addTwoNumbers(self, l1, l2) 호출
    solution = Solution()
    l1 = list(map(int,input('list1을 입력하세요 : ').split()))
    l2 = list(map(int,input('list2을 입력하세요 : ').split()))
    result = solution.addTwoNumbers(l1, l2)
    print(result)
    for i in result :
        print(i)



    # 2. ListNode로 구현하기
    # ListNode에 데이터 생성하기
    # list1 -> list2 -> list3 -> None
    list1 = ListNode(2)
    list2 = ListNode(4)
    list3 = ListNode(3)
    list1.next = list2
    list2.next = list3
    # list4 -> list5 -> list6 -> None
    list4 = ListNode(5)
    list5 = ListNode(6)
    list6 = ListNode(4)
    list4.next = list5
    list5.next = list6

    
    solution = Solution()
    # ListNode를 이용한 solution함수 호출
    result = solution.addTwoNumbers2(list1, list4)
    for i in range(3):
        print(result.val)
        result = result.next