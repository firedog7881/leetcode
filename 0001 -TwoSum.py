'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

nums = [3,2,4]
target = 6

def twoSum(nums, target):
    answer = []
    numDict = {}

    for i in range(len(nums)):
        otherNum = target - nums[i]
        if otherNum in numDict.keys():
            otherIndex = nums.index(otherNum)
            if i != otherIndex:
                return sorted([i, otherIndex])
        numDict.update({nums[i]: i})




print(twoSum(nums, target))
