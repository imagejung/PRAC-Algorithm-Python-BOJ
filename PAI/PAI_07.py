# 두 수의 합, p173

#브루트 포스로 계산
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
         for i in range(len(nums)-1):
             for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


#in을 이용한 탐색, 더 빠름
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
         for i in range(len(nums)):
             # 목표값 - n 이 nums에 있으면 더하기 만들수 있는 경우
             complement = target - nums[i]

             if complement in nums[i+1:]:
                 # index 출력해야함. 두번째 인자는 i+1부터 시작하니까 +(i+1) 해줌
                 return [i, nums[i+1:].index(complement)+(i+1)]
