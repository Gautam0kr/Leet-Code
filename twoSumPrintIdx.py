#input list of nums and a target. 
# Return the idx of two nums in list whose sum is target as a list
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    res=[i, j]
                    return res
nums=list(map(int, input().split()))
target=int(input())                  
nums1=Solution()
print(nums1.twoSum(nums, target))
