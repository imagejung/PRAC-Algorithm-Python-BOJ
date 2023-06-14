# 유요한 팰린트롬, p138

class Solution(object):
    # 문자 or 숫자만 받고, 전부 소문자로 배열에 추가
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # 문자 or 숫자인 경우만 strs 배열에 추가
                strs.append(char.lower())

        # 팰린트롬인지 확인
        while len(strs) > 1:
            if strs.pop(0) != strs.pop(): # 첫문자, 마지막 문자 pop해서 비교
                return False

        return True