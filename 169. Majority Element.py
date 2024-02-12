# 169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
Input: nums = [3,2,3]
Output: 3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        # Step 1: Find the potential majority candidate
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Step 2: Verify the potential majority candidate
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
                
        if count > len(nums) // 2:
            return candidate
        else:
            return None  # No majority element found
