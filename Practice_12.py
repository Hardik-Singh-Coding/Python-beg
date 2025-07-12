""" Question - Given a list of integers, return a new list with all the duplicates removed, 
but keep the first occurrence of each number in the same order as they appeared. """

def remove_duplicates(nums: list[int]) -> list[int]:
    seen = set()
    numslist = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            numslist.append(num)

    return numslist


nums1 = [1, 2, 2, 3, 4, 3, 5]
nums2 = [7, 7, 7, 7]
nums3 = [5, 4, 3, 2, 1]
print(remove_duplicates(nums1))
print(remove_duplicates(nums2))
print(remove_duplicates(nums3))



""" Mistake - couldn't preserve the order """