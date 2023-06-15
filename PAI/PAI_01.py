# 유요한 팰린트롬, p138


# 풀이1 : 리스트 활용
class Solution(object):
    # 문자 or 숫자만 받고, 전부 소문자로 배열에 추가
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # 문자 or 숫자인 경우만 strs 배열에 추가
                strs.append(char.lower())

        # 팰린트롬인지 확인
        while len(strs) > 1:
            if strs.pop(0) != strs.pop(): # pop(0) = index 0이므로 첫문자, pop() = 마지막 문자 뽑아서 비교
                return False

        return True



# 풀이2 : deque로도 풀수 있음 pop(0) 대신 popleft

# deque의 popleft가 더 빠름.
# -> pop(0)은 pop하고 뒤에 인자들을 앞으로 이동시켜야(땡겨야) 하기 때문에 시간복잡도가 popleft()는 O(1), pop(0)은 O(n)
from collections import deque

class Solution(object):
    def isPalindrome(self, s:str) -> bool:
        strs = deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len (strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
