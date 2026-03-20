class Solution:
    def singleNumber(self, nums):
        # Step 1: XOR all numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        # Step 2: Find rightmost set bit
        diff_bit = xor_all & (-xor_all)
        return diff_bit
        # Step 3: Divide into two groups
        num1 = 0
        num2 = 0     
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
s=Solution()
print(s.singleNumber([1,2,1,3,2,5]))