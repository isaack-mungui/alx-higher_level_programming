#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if idx < 0 or idx > len(list_copy):
        return my_list
    else:
        list_copy[idx] = element
        return list_copy


# res = new_in_list([1, 2, 3, 4, 5], 3, 9)
# print(res)
