# 문자열 뒤집기, p145

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            # 이렇게 하면 값 교환 가능 (튜플로 패킹 -> 언패킹 방식이라서??...)
            s[left], s[right] = s[right], s[left]

            # 두줄로 나눠쓸꺼면 tmp 써야함.
            # tmp = s[left]
            # s[left] = s[right]
            # s[right] = tmp

            left += 1
            right -= 1


