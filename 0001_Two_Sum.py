class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, number in enumerate(nums):
            complement = target - number
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[number] = i
