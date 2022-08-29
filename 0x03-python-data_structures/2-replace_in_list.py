def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if i < 0:
            return my_list
        elif i > len(my_list):
            return my_list

        if i == idx:
            my_list[idx] = element
            return my_list
