class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * k # deque크기 지정
        self.r = -1 # 데이터가 없으면 -1
        self.f = -1 # 데이터가 없으면 -1
        self.k = k # deque의 길이

    # None의 개수가 deque의 길이와 같으면 True
    # None의 개수가 deque의 길이와 다르면 False
    def isEmpty(self) -> bool:
        return self.deque.count(None) == self.k

    # None의 개수가 0이면 True
    # None의 개수가 0이 아니면 False
    def isFull(self) -> bool:
        return self.deque.count(None) == 0

    # 데이터가 없으면 f(-1)반환
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.f]

    # 데이터가 없으면 r(-1)반환
    def getRear(self) -> int:
        if self.isEmpty():
            return self.r
        #  데이터가 존재하면 r지점에 있는 데이터를 반환
        return self.deque[self.r]

    #  데크 마지막에 아이템을 추가
    def insertLast(self, value: int) -> bool:
        r = self.r + 1
        # isFull이 True라면 False반환
        if self.isFull():
            return False

        # isEmpty가 True라면 f를 1 증가
        if self.isEmpty():
            self.f = self.f + 1
        # r이 k보다 작으면 r+1 지점에 input을 저장
        if r < self.k:
            self.r = self.r + 1
        else :
            # r이 k과 같으면 0 지점에 input을 저장
            self.r = 0
        self.deque[self.r] = value
        return True

    # 맨앞의 데이터 삭제
    def deleteFront(self) -> bool:
        # 삭제할 데이터가 없으면 False반환
        if self.isEmpty():
            return False
        # f 지점의 데이터 삭제
        self.deque[self.f] = None

        # 데이터 삭제후 데이터가 존재하지 않으면 f와 r에 -1설정
        if self.isEmpty():
            self.f = -1
            self.r = -1
        else :
            # 데이터 삭제후에도 데이터가 존재하고,
            # f에 1을 증가해도 index범위를 벗어나지 않으면 그대로 증가시킴
            f = self.f + 1
            if f < self.k:
                self.f = f
            else :
                # f에 1을 증가해서 index범위를 벗어나면 0으로 설정
                self.f = 0
        return True

    def deleteLast(self) -> bool:
        # 삭제할 데이터가 없으면 False반환
        if self.isEmpty():
            return False
        # r지점의 데이터를 삭제
        self.deque[self.r] = None

        # 데이터 삭제후 데이터가 존재하지 않으면 f와 r에 -1설정
        if self.isEmpty():
            self.r = -1
            self.f = -1
        else :
            # 데이터 삭제후에도 데이터가 존재하고,
            # r에 1을 감소시켜서 index범위를 벗어나면 k-1로 설정
            r = self.r - 1
            if r < 0 :
                self.r = self.k-1
            else :
                # r에 1을 감소해도 index범위를 벗어나지않으면 그대로 감소시킴
                self.r = r

        return True


    # 맨 앞에 데이터 추가
    def insertFront(self, value: int) -> bool:
        # 추가할 공간이 없으면 False반환
        if self.isFull():
            return False
        
        f = self.f
        # f가 -1이면(데이터가 없으면) f, r에 1을 추가한 지점에 데이터 추가
        if f < 0 :
            self.f = self.f + 1
            self.r = self.r + 1
        elif f == 0:
            # f가 0이면(데이터 존재), k-1에 데이터 추가
            self.f = self.k - 1
        elif f > 0 :
            # f가 0보다 크면(데이터 존재), f-1에 데이터 추가
            self.f = self.f - 1
        self.deque[self.f] = value
        return True









