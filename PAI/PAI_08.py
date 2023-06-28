# 빗물 트래핑, p180

# 투 포인터 풀이
class Solution:
    def trap(self, height: list[int]) -> int:

        # 변수 설정
        volume = 0
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]

        # 양쪽 끝에서 제일 높은 쪽으로 모임
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # rigth_max가 높으면 left_max ~ 오른쪽 어딘가에 물을 막아줄 기둥이 있다는 뜻 -> volume 채워주기
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            # left_max도 마찬가지
            else:
                volume += right_max - height[right]
                right -= 1

        return volume