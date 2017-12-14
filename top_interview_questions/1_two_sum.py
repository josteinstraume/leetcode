# Given an array of integers,
# return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Initial solution
# Not accepted since returns a string
# O(n-squared) run time
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    n = len(nums)
    for i in range(1, n):
        for j in range(2, n):
            if nums[i] + nums[j] == target:
                result = '[%d,%d]'%(i,j)
                print(result)
                return result


nums = [2, 7, 11, 15]
target = 9

# O(n) run time
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        n = len(nums)
        for i in range(n):
        	# target is 9, first num in nums is 2, so we're looking for 9-2=7 in nums
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return map[nums[i]], i
        # does not add up to the given target
        return -1, -1
