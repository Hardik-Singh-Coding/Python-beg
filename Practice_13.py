""" Question - Given a list of integers, move all 0s to the end while maintaining the relative order of the non-zero elements.
You must do this in-place, meaning don’t create a new list — modify the original list if possible. """

def move_zeros(nums: list[int]) -> None:
    non_zero_index = 0
    
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0

    print(nums)

nums = [0, 1, 0, 3, 12]
move_zeros(nums)