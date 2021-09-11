# 합이 0이 되는 배열 찾기
import time
start_time = time.time()

### 1. combinations사용
# Memory Limit Exceeded
class Solution:
    def threeSum(self, nums):
        from itertools import combinations
        # 3개의 수에 대한 조합리스트 저장
        nums_list = list(combinations(nums, 3))
        # 합이 0이 되는 조합을 저장하는 set
        result_list = set()
        # print(dir(result_list))
        # 조합리스트를 순회하며 합이 0일 경우의 조합을 출력
        while nums_list:
            num = nums_list.pop()
            if sum(num) == 0:
                result_list.add(tuple(sorted(num)))
        return result_list

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)

# 2.3중 for문 이용
# RTime Limit Exceeded
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                for k in range(j, len(nums)):
                    if j == k:
                        continue
                    sum3 = nums[i] + nums[j] + nums[k]
                    if sum3 == 0:
                        result_list.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return result_list


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right :
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left += 1
                elif sum > 0:
                    right -= 1
                else :
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -=1
        return results
