""" Question - Given a list of integers nums, return a new list running_sum where running_sum[i] is the sum of 
all elements from index 0 to i in nums. """

def running_sum(nums: list[int]) -> list[int]:
    result = []
    sum = 0
    for i in nums:
        sum+=i
        result.append(sum)
    return result    

nums = [1, 2, 3, 4]

print(running_sum(nums))