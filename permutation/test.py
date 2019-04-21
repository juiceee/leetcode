
def quicksort(nums, start, end):

    if  start>=end:
        return
    else:
        pivot_index = (start + end)//2
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

        p = start
        for index in range(start, end):
            if nums[index] < pivot_value:
                nums[index], nums[p] = nums[p], nums[index]
                p += 1

        nums[p], nums[end] = nums[end], nums[p]

        quicksort(nums, start, p-1)
        quicksort(nums, p+1, end)

if __name__=='__main__':
    nums = [2,3,232,34,5,3452,34,34534,5,23,423,3,12312]
    
    quicksort(nums,0, len(nums)-1)
    print(nums)
