"""
    Given an integer array nums,
    rotate the array to the right by k steps,
    where k is non-negative.
"""

"""
    solution with 
    O(n) time complexity
    O(n) space alocation because it needs a aux array
"""
def rotate(nums, k):
    aux = nums[:]
    
    for i in range(0,len(nums)):
        mod_index = (i + k) % len(nums)
        print(mod_index)
        nums[mod_index] = aux[i]
    
    return nums


"""
    solution with
    O(3*n) = O(n) time complexity
    O(1) space alocation because it works inside the nums array

    --------
    achieved only by reversing parts of the array; example:
    nums = [-1,-100,3,99] k = 2
    
    invert positions -> -1 and 99, -100 and 3
    nums = [99, 3, -100, -1]
    
    then, correct the first k items, putting in the correct order simply inverting
    them the same way it was made in the last step
    nums = [3, 99, -100, -1]

    now do it for the remaining items of nums
    nums = [3, 99, -1, -100]
"""
def rotateByReversing(nums,k):
    k = k % len(nums)

    print(nums)
    revertArrayParts(nums, 0, len(nums) - 1)
    print(nums)
    revertArrayParts(nums, 0, k - 1)
    print(nums)
    revertArrayParts(nums, k, len(nums) - 1)
    print(nums)

    return nums

def revertArrayParts(nums, start, end):
    l, r = start, end

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    return nums


if __name__== "__main__":
    array = [1,2,3,4,5,6,7]
    k = 3
    rotateByReversing(array, k)

