"""Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums. Return k."""

def removeElement(self, nums, val):
    insert = 0
    for i in nums:
        if i != val:
            nums[insert] = i
            insert += 1

    return insert
