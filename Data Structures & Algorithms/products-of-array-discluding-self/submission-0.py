class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        curr = 1

        for i in range(n):
            arr[i] *= curr
            curr *= nums[i]

        curr = 1
        for i in range(n-1, -1, -1):
            arr[i] *= curr
            curr *= nums[i]
        return arr