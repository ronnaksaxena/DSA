def qSort(nums, left, right):
    if left < right:
        pivot = partition(nums, left, right)
        qSort(nums, left, pivot - 1)
        qSort(nums, pivot + 1, right)

def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i

def sort(nums):
    qSort(nums, 0, len(nums) - 1)
    return nums

test1 = [1, 5, 21, 4, 6, 10]
print(sort(test1))
