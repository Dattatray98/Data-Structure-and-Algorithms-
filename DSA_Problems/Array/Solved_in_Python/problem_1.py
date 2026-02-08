"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

#  Method 1 : Brute Force


class Solution1:

    def twoSum(self, nums: list[int], target: int) -> list:
        l = len(nums)

        for i in range(0, l):
            for j in range(1, l):
                if i != j and nums[i] + nums[j] == target:
                    print(i, j)
                    return
                else:
                    pass


if __name__ == "__main__":
    S1 = Solution1()
    # S.twoSum(nums=[2,5,5,11], target=10)


# Method 2 : Hash map


class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list:
        d = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d.keys():
                return d[comp], i
            else:
                d[nums[i]] = i


if __name__ == "__main__":
    S2 = Solution2()
    S2.twoSum(nums=[3,2,3], target=6)


# Method 3 : 