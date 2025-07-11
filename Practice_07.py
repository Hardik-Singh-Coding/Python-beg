""" Question - Remove even numbers from a list """

def remove_even_numbers(nums: list[int]) -> list[int]:
    return [num for num in nums if num%2 != 0]

nums = [1, 2, 3, 4, 5, 6]

print(remove_even_numbers(nums))