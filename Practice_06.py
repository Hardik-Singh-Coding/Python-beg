def count_trues(b_list: list) -> int: 
    # global count 
    # count = 0
    # for i in b_list:
    #     if i is True:
    #         count+=1
    
    # return count

    return boolean_list.count(True)


# global boolean_list
boolean_list = [True, False, True, True, True]

print(boolean_list)
print("No of true values in this list are:", count_trues(boolean_list))
