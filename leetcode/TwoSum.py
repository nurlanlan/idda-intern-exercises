from operator import index
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for char in nums:
            if target - char in nums:
                return [nums.index(char), nums.index(target - char)]
