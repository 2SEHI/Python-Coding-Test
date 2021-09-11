import collections


class Solution:
    ### list로 구현
    def isPalindrome(self, s: str) -> bool:
        # 문자열을 소문자로 변환하고 한 글자씩 숫자, 영문자인 경우에만 리스트에 저장
        new_s = [c for c in s.lower() if c.isalnum()]

        # 팰린드롬여부 반환값 - True:팰린드롬, False:팰린드롬아님
        flag = True
        # 문자열이 None이 아니면서 문자열의
        while new_s and 1 <= len(new_s)/2:
            # 문자열의 앞과 뒤에서 한 글자씩 추출하여 비교
            if new_s.pop(0) != new_s.pop():
                # 같지 않으면 프래그를 False로 저장하고 반복문을 빠져나옴
                flag = False
                break
        # 결과 반환
        return flag

    ### deque로 구현 : list구현보다 runtime속도가 확연히 줄어듦
    def isPalindrome2(self, s: str) -> bool:
        q = collections.deque()
        # 문자열을 소문자로 변환하고 한 글자씩 숫자, 영문자인 경우에만 리스트에 저장
        for c in s.lower():
            if c.isalnum():
                q.append(c)

        # 팰린드롬여부 반환값 - True:팰린드롬, False:팰린드롬아님
        flag = True
        # 문자열이 None이 아니면서 문자열의
        while q and 1 <= len(q)/2:
            # 문자열의 앞과 뒤에서 한 글자씩 추출하여 비교
            if q.popleft() != q.pop():
                # 같지 않으면 프래그를 False로 저장하고 반복문을 빠져나옴
                flag = False
                break
        # 결과 반환
        return flag
if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"

    # result = solution.isPalindrome(s)
    # print(result)
    result = solution.isPalindrome2(s)
    print(result)
