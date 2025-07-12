""" Question: Given a list arr, replace every element with the greatest element among the elements to its right, 
and replace the last element with -1. """

def replace_elements(arr: list[int]) -> list[int]:
    max_so_far = -1
    # Loop from right to left
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_so_far
        max_so_far = max(temp,max_so_far)
    return arr


arr = [17, 18, 5, 4, 6, 1]
print(replace_elements(arr))


""" Mistake - Couldn't loop from right to left """