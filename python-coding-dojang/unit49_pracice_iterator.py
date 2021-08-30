# iterator 클래스 생성
class TimeIterator:
    def __init__(self,start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        # 23:59:59보다 크면 시작시간과 종료시간을 0부터 다시 시작
        if self.start > 86399 and self.stop > 86399:
            self.start = self.start - 86400
            self.stop = self.stop - 86400

        # 시작 시간 임시할당
        r = self.start

        # 시작 시간이 종료 시간보다 적으면
        # 시작시간에 1을 더하여 시작시간에 할당
        if self.start < self.stop:            
            self.start = r + 1
            # 시간을 hh:mm:ss의 형태로 변환하여 반환
            return sec_to_strtime(r)
        else :
            # 시작 시간이 종료시간보다 커지면 예외발생시키기
            raise StopIteration 

    def __getitem__(self, index):
        
        # 시작시간에 호출하려는 인덱스를 더하여 반환
        # 23:59:59보다 작으면
        # 시간을 hh:mm:ss의 형태로 변환하여 반환
        if self.start + index < 86399 :
            return sec_to_strtime(self.start + index)
        else : 
            # 23:59:59보다 크면
            # 시간을 0:0:0부터 시작하도록 하고
            # hh:mm:ss의 형태로 변환하여 반환
            return sec_to_strtime(self.start + index - 86400)
        

# 숫자가 10보다 작으면 10의 자리수에 0을 붙이고 반환
def add_zero(num):
    str_time = ''
    if num < 10:
        str_time = '0' + str(num)
    else :
        str_time = str(num)
    return str_time


# 초시간을 hh:mm:ss의 str형태로 변환해주는 함수
def sec_to_strtime(input_sec):
    
    # 입력 초시간을 60으로 나눈 나머지를 초시간으로 할당
    sec = input_sec % 60
    # 입력 초시간을 60으로 나눈 몫을 분시간으로 할당
    minute = input_sec // 60
    
    # 분시간을 60분보다 작을 경우
    if minute < 60:
        hour = 0
        minute = int(minute)
    else :
        # 분시간이 60분을 초과할 경
        # 분시간을 60으로 나눈 몫을 시간으로 할당
        hour = int(minute // 60)
        
        # 분시간을 60으로 나눈 나머지를 분시간으로 할당
        minute = int(minute % 60)
    # 시간을 hh:mm:ss의 str형태로 변환하여 반환
    return add_zero(hour) + ':' + add_zero(minute) + ':' + add_zero(sec)

# 시간입력받기
# start : 시작하는 초
# stop : 반복을 끝낼 초
# index : 시작하는 초로부터 index번째
start, stop, index = map(int, input("시간을 입력하세요 : ").split())

# iterator객체 TimeIterator을 반복하며 시간 값을 출력
for i in TimeIterator(start, stop):
    print(i)

# 시작하는 초로부터 index번째의 시간을 출력함
print('\n', TimeIterator(start, stop)[index], sep='')