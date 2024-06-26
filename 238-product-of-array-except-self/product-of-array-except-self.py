class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products and store them in the answer array
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        
        # Calculate suffix products on the fly and multiply with prefix products
        suffix_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        
        return answer