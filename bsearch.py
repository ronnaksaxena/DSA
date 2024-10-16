'''
What is the search space?
How to reduce search space?
When to return?

'''



def bSearch(nums, target):
    # Find a garunteed target in array
    l, r = 0, len(nums)-1
    while l <= r:
        m = l + (r-l)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

def condition(i):
    return True
def bSearch(nums):
    # Find unknown element in nums
    l, r = 0, len(nums) # truncase down
    while l < r:
        m = l + (r-l)//2
        if condition(m):
            l = m
        else:
            r = m - 1
    return l