# Question - to extract integers from a given list and sort them in ascending order
# def extract_and_sort_numbers(string_list: list) -> list:
#     result = []
#     for item in string_list:
#         if item.lstrip('-').isdigit():  # handles negative numbers
#             result.append(int(item))
#     return sorted(result)


# print(extract_and_sort_numbers(["apple", "42", "banana", "-5", "100", "3.14"]))


# Some more examples of lstrip() function
num = "444abc12345"
print(num.lstrip('4')) # strips only "444" 