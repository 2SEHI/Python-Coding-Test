class MyCircularQueue:
    def __init__(self, maxlen):
        self.q = [None] * maxlen
        self.maxlen = maxlen
        self.f = 0 # 맨 앞 인덱스
        self.r = 0 # 맨 끝 인덱스

    def enQueue(self, input):
        i = self.r
        # 가득 차있으면 False반환
        if self.isFull() :
            return False
        # 채울 공간이 있으면 끝 인덱스 + 1
        else :

            if self.r >= len(self.q)-1 or self.isEmpty():
                self.r = 0
            else :
                self.r += 1

        self.q[self.r] = input
        print("삽입 후 queue:", self.q)
        return True

    def deQueue(self):
        # 삭제할 데이터가 존재하지 않으면 False반환
        if self.isEmpty():
            return False
        else :
            # 삭제할 데이터가 존재하면 삭제
            self.q[self.f] = None
            # 삭제 후 데이터가 없으면 self.f와 self.r을 0설정
            if self.isEmpty():
                self.f, self.r = 0, 0
            else :
                if self.r >= len(self.q) - 1 or self.isEmpty():
                    self.r = 0
                else:
                    self.r += 1
            print("삭제 후 queue:", self.q)
            return True

    def Rear(self):
        if self.isEmpty():
            return -1
        else :
            return self.q[self.r]

    def Front(self):
        print(self.q)
        if self.isEmpty():
            return -1
        else :
            return self.q[self.f]

    # 데이터가 1도 없으면 True반환
    def isEmpty(self):
        return self.q.count(None) == len(self.q)

    # 데이터가 가득 찼으면 True, 공간이 남았으면 False
    def isFull(self):

        return self.q.count(None) == 0



if __name__ == "__main__" :

    # myCircularQueue = MyCircularQueue(3)
    # print(myCircularQueue.enQueue(1))
    # print(myCircularQueue.enQueue(2))
    # print(myCircularQueue.enQueue(3))
    # print(myCircularQueue.enQueue(4))
    # print(myCircularQueue.Rear())
    # print(myCircularQueue.isFull())
    # print(myCircularQueue.deQueue())
    # print(myCircularQueue.enQueue(4))
    # print(myCircularQueue.Rear())
    #
    # circularQueue = MyCircularQueue(4)
    # print(circularQueue.enQueue(10))
    # print(circularQueue.enQueue(20))
    # print(circularQueue.enQueue(30))
    # print(circularQueue.enQueue(40))
    # print(circularQueue.enQueue(50))
    # print(circularQueue.Rear())
    # print(circularQueue.isFull())
    # print(circularQueue.deQueue())
    # print(circularQueue.deQueue())
    # print(circularQueue.enQueue(50))
    # print(circularQueue.enQueue(60))
    # print(circularQueue.Rear())
    # print(circularQueue.Front())
    #
    # circularQueue = MyCircularQueue(6)
    # print(circularQueue.enQueue(6))
    # print(circularQueue.Rear())
    # print(circularQueue.Rear())
    # print(circularQueue.deQueue())
    # print(circularQueue.enQueue(5))
    # print(circularQueue.Rear())
    # print(circularQueue.deQueue())
    # print(circularQueue.Front())
    # print(circularQueue.deQueue())
    # print(circularQueue.deQueue())
    # print(circularQueue.deQueue())

    circularQueue = MyCircularQueue(2)
    print(circularQueue.enQueue(1))
    print(circularQueue.enQueue(2))
    print(circularQueue.deQueue())
    print(circularQueue.enQueue(3))
    print(circularQueue.deQueue())
    print(circularQueue.enQueue(3))
    print(circularQueue.deQueue())
    print(circularQueue.enQueue(3))
    print(circularQueue.deQueue())
    print(circularQueue.Front())
