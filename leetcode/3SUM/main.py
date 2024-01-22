# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

def threeSum(nums, target):
    nums.sort()
    print(nums)
    res = []

    for index, n in enumerate(nums):

        if index > 0 and n == nums[index-1]:
            continue
        
        l, r = index + 1, len(nums)-1

        while l < r:
            threeSum = n + nums[l] + nums[r]
            print(f'{n}, {nums[l]}, {nums[r]} => {threeSum}')

            if threeSum == target:
                return threeSum
            
            abs(threeSum - target)
            
            if threeSum > 0:
                r = r - 1
            elif threeSum < 0:
                l = l + 1
            else:
                res.append([n, nums[l], nums[r]])
                l = l + 1
                while nums[l] == nums[l - 1] and l < r:
                    l = l + 1

    return res


if __name__== "__main__":
    lst = [-1,2,1,-4]
    tg = 1

    print(threeSum(lst, tg))
