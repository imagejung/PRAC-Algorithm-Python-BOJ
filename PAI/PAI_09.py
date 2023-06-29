# 세 수의 합, p184

# 투 포인터로 합 계산
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):

            # 중복된 값 pass
            if i> 0 and nums[i] == nums[i - 1]:
                continue

            # 왼쪽 오른쪽에서 간격을 좁혀가며 합 sum 계산
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1  # sort 돼 있으니까 0보다 작으면 음수를 줄여줘야함
                elif sum > 0:
                    right -= 1
                else:  # sum이 0, 답인 경우
                    results.append([nums[i], nums[left], nums[right]])

                    # 중복된 값 pass
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 답 처리 다 했으니 투 포인터 옮겨주기
                    left += 1
                    right -= 1

        return results