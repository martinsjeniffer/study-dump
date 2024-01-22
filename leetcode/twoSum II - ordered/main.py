# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twoSum(nums, target):
	i = 0
	j = len(nums)-1

	while i < j:
		num_sum = nums[i]+nums[j]
		print(f'pos -> i {i} j {j} => {num_sum}')

		if num_sum == target:
			return [i, j]
		
		if num_sum > target:
			j=j-1
		else:
			i=i+1

	return []

if __name__== "__main__":
    lst = [2,7,11,15]
    tg = 9

    print(twoSum(lst, tg))