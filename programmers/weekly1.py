def solution(price, money, count):
    # 횟수에 따른 가격을 list에 저장
    price_list = [price * i for i in range(1,count+1) ]
    # 가진 돈에서 사용한 돈을 뺀다
    remain = money - sum(price_list)
    # 남은 돈이 0보다 작을 경우, 필요한 액수를 반환
    # 남은 돈이 0보다 클 경우,  0을 반환
    answer = abs(remain * (remain < 0))
    return answer