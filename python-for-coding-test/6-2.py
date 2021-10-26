#-*- coding:utf-8 -*-
# pivot 은 start 위치의 요소
# 종료조건 : 개수가 한개 남았을 경우
# 파라미터 : array, start, end
# return : array
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    # pivot 보다 큰 데이터를 찾는 포인터
    left = start + 1
    # pivot 보다 작은 데이터를 찾는 포인터
    right = end

    while left <= right:
        # pivot 보다 left 포인터의 데이터가 클때까지 left 포인터 증가
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot 보다 right 포인터의 데이터가 작을 때까지 right 포인터 증가
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # right 포인터의 데이터가 pivot 보다 작고
        # left 포인터의 데이터가 pivot 보다 크면서
        # left 포인터와 right 포인터의 위치가 엇갈린 경우
        # pivot 과 left 데이터를 교환한다
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        # right 포인터 데이터는 피벗보다 작고
        # left 포인터의 데이터는 pivot 보다 크면서
        # left 포인터와 right 포인터의 위치가 엇갈리지 않은 경우
        # left 포인터의 데이터와 right 포인터의 데이터를 교체한다
        else:
            array[left], array[right] = array[right], array[left]
    # pivot 을 기준으로 왼쪽과 오른쪽을 나누어서 정렬을 수행한다
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


if __name__ == "__main__":
    arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)