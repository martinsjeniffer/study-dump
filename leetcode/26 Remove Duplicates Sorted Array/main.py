"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should 
be kept the same.

Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get
accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums 
contain the unique elements in the order they were present in 
nums initially. The remaining elements of nums are not important
as well as the size of nums.
- Return k.

"""

"""
    SOLUTIONS OBSERVATIONS

    We start the lft pointer in 1 because our array is sorted,
    so we are garanteed that our first position is not gonna be
    impacted in any way.
    Two pointers make the solution work even inside only one loop
    through the array, so it is O(n) on time complexity.
"""

def removeDuplicates(nums):
    lft = 1

    for r in range(1,len(nums)):
        if nums[r] != nums[r - 1]:
            nums[lft] = nums[r]
            lft += 1

        print(nums)
        print(f'nums[{lft}] = {nums[lft]} --- nums[{r}] = {nums[r]}')
        
    return lft

if __name__== "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]

    removeDuplicates(nums)

