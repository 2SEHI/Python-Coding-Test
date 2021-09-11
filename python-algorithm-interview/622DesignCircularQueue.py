class MyCircularQueue:
    def __init__(self, maxlen):
        self.q = [None] * maxlen
        self.maxlen = maxlen
        self.f = -1 # 맨 앞 인덱스
        self.r = -1 # 맨 끝 인덱스

    # 저장 가능 공간(None의 개수)이 0개이면 True
    # 저장 가능 공간(None의 개수)이 0개보다 크면 False
    def isFull(self):
        return self.q.count(None) == 0

    # 저장 가능 공간(None의 개수)이 큐의 크기와 같으면 True
    # 저장 가능 공간(None의 개수)이 큐의 크기보다 작으면 False
    def isEmpty(self):
        return self.q.count(None) == self.maxlen

    # 큐의 맨앞 데이터를 반환
    # isEmpty가 True일 경우 -1 반환
    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.q[self.f]

    # 큐의 맨뒤 데이터를 반환
    # isEmpty가 True일 경우 -1 반환
    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.q[self.r]

    def enQueue(self, input):
        r = self.r + 1
        # isFull이 True라면 False반환
        if self.isFull():
            return False

        # isEmpty가 True라면 f를 1 증가
        if self.isEmpty():
            self.f = self.f + 1
        # r이 maxlen보다 작으면 r+1 지점에 input을 저장
        if r < self.maxlen:
            self.r = self.r + 1
        else :
            # r이 maxlen과 같으면 0 지점에 input을 저장
            self.r = 0
        self.q[self.r] = input
        return True

    def deQueue(self):
        f = self.f + 1
        print('삭제하기 전 : ', self.q)
        # isEmpty이 True이면 False반환
        if self.isEmpty():
            return False

        self.q[self.f] = None
        # 데이터 삭제후 isEmpty가 True이면 f와 r에 -1저장
        if self.isEmpty():
            self.f = -1
            self.r = -1
        else :
            if f < self.maxlen:
                self.f = self.f + 1
            else :
                self.f = 0
        print('삭제후 : ', self.q)
        return True

