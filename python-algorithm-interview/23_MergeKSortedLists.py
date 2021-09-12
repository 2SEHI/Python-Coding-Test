import heapq

class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: LinkedList) ->  LinkedList:
        # 요소를 연결할 변수
        root = result = LinkedList(None)

        # 요소를 저장할 리스트
        heap = []
        # 각 연결리스트의 가장 작은 요소를 heap에 저장
        for i in range(len(lists)):
            if lists[i]:
                # 각 LinkedList의 첫번째 인자값, 인덱스 번호, 첫번째 연결리스트객체
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        # heap이 존재할 때까지 순회
        while heap:
            # heap에서 가장 작은 요소를 pop
            node = heapq.heappop(heap)
            # 요소의 index를 저장
            idx = node[1]
            # result.next에 요소를 연결
            result.next = node[2]

            # result가 요소를 가리키도록 함
            result = result.next
            # result.next가 존재하면, result.next를 heap에 저장
            if result.next :
                heapq.heappush(heap, (result.next.val, idx, result.next))
        # root : LinkedList(0) -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> 6 이므로 
        # root.next를 반환
        return root.next


if __name__ == "__main__" :
    a1 = LinkedList(3)
    a2 = LinkedList(4)
    a3 = LinkedList(5)    
    a1.next = a2
    a2.next = a3

    b1 = LinkedList(1)
    b2 = LinkedList(3)
    b3 = LinkedList(4)    
    b1.next = b2
    b2.next = b3

    c1 = LinkedList(2)
    c2 = LinkedList(6)  
    c1.next = c2

    lists = []
    lists.append(a1)
    lists.append(b1)
    lists.append(c1)
    solution = Solution()
    result = solution.mergeKLists(lists)

    while result : 
        print(result.val)
        result = result.next