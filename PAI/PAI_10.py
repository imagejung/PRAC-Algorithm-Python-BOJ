# 배열 파티션1, p190

# 오른차순 풀이
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum = 0
        nums.sort()
        tmp = [] # sorting해서 앞에서 부터 2개씩 집어넣으면 답 나옴

        for n in nums:
            tmp.append(n)
            if len(tmp) == 2:
                sum += min(tmp)
                tmp = [] # 2개 집어 넣었으니까, tmp 초기화

        return sum


# 짝수 번째 값 계산
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum = 0
        nums.sort()

        for i in range(len(nums)):
            if i % 2 == 0: # nums 배열 0,2,4... index 만 더해주면 됨
                sum += nums[i]

        return sum