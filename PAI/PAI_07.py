# 두 수의 합, p173

#브루트 포스로 계산
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
         for i in range(len(nums)-1):
             for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]