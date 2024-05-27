"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

"""

"""
    SOLUTIONS OBSERVATIONS

    hashmap works good, but optimal algorithm is the boyer-moore one.

"""

# HASHMAP
# O(1) operation
# O(n) memory
def majorityElement(nums):
    count = {}
    result, maxCount = 0, 0

    for n in nums:
        # get count[n]
        # if already exists, add 1,
        # if not, get 0 by default and add 1 to a new key in hashmap
        count[n] = 1 + count.get(n,0)
        print(n, "-----", count)

        if count[n] > maxCount:
            result = n
        maxCount = max(count[n], maxCount)

        print(">>", "result", result, "maxCount", maxCount, "\n")

    return result


# BOYER-MOORE
# HAS to have a majority element!!
def MajorityElementBoyerMoore(nums):
    result, count = 0, 0

    for n in nums:
        if count == 0:
            result = n

        if n == result:
            count += 1
        else:
            count -= 1

        # count += (1 if n == result else -1) TERNARY

        print(">>", "[", n, "]", "result", result, "count", count, "\n")
    return result

if __name__== "__main__":
    majorityElement([3,2,3,2,2])
    MajorityElementBoyerMoore([3,2,3,2,2])
