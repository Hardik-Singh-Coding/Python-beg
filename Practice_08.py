def running_sum(nums: list[int]) -> list[int]:
    result = []
    sum = 0
    for i in nums:
        sum+=i
        result.append(sum)
    return result    

nums = [1, 2, 3, 4]

print(running_sum(nums))