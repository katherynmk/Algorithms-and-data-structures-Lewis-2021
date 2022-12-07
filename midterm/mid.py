def is_sorted(my_list):
    #creat a copy of the list and use pythons sort method
    my_list2 = my_list[:]
    my_list2.sort()
    if my_list2 == my_list: #test to see if the original list is sorted or not
        return True
    else:
        return  False
# time complexity:
# space complexity:
