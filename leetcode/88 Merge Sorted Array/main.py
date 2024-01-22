"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""


"""
    SOLUTION OBSERVATIONS

    This solution has O(n) complexity because the arrays are sorted and 
    we are garanteed that num1 has n + m size.
    So, we just fix a merge pointer in the last position of num1 and we
    iterate through num1 and num2 using n and m.

"""

def merge(nums1, m, nums2, n):
    merge_pointer = (m + n) - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[merge_pointer] = nums1[m - 1]
            print(f'> {m}')
            m -= 1
        else:
            nums1[merge_pointer] = nums2[n - 1]
            print(f'<= {n}')
            n -= 1

        merge_pointer -= 1
        print(f'---- {nums1}')
    
    while n > 0:
        nums1[merge_pointer] = nums2[n - 1]
        n -= 1
        merge_pointer -= 1

    print(f'{nums1}')


if __name__== "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3

    nums2 = [2,5,6]
    n = 3

    merge(nums1, m, nums2, n)
