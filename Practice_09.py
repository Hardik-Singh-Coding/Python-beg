""" Question: Write a function that returns the second largest unique number in a list of integers. If there is no second largest 
(e.g., all elements are the same), return None. """

def second_largest(nums: list[int]) -> int | None:
    first = second = float('-inf') # Sets the variables to negative infinity
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num

    return second if second != float('-inf') else None


nums = [10, 5, 20, 20, 10]

print(second_largest(nums))